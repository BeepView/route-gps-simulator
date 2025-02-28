#!/usr/bin/env python3

import argparse
import json
from time import sleep

from tqdm import tqdm

from utils.mapbox_service import Mapbox_service
from utils.tracker_sim import TrackerSim
from utils.utils import post

if __name__ == "__main__":
    # Load the default values from the config file
    with open("defaults.json") as f:
        config = json.load(f)

    parser = argparse.ArgumentParser(description="Simulate a GPS tracker")
    parser.add_argument(
        "--start",
        help="Start location",
        required=config.get("start") is None,
        default=config.get("start"),
    )
    parser.add_argument(
        "--end",
        help="End location",
        required=config.get("end") is None,
        default=config.get("end"),
    )
    parser.add_argument(
        "--interval",
        type=int,
        help="Interval in seconds",
        required=config.get("interval") is None,
        default=config.get("interval"),
    )
    parser.add_argument(
        "--duration",
        type=int,
        help="Duration in seconds (0 to simulate the route once & -1 to loop the route infinitely)",
        required=config.get("duration") is None,
        default=config.get("duration"),
    )
    parser.add_argument(
        "--api_key",
        help="MapBox API key",
        required=config.get("api_key") is None,
        default=config.get("api_key"),
    )
    parser.add_argument(
        "--webhook_url",
        help="Webhook URL to which the simulated coordinates JSON are POSTed",
        required=config.get("webhook_url") is None,
        default=config.get("webhook_url"),
    )
    parser.add_argument(
        "--tracker_id",
        help="Tracker ID which will be sent in the POST request",
        required=config.get("tracker_id") is None,
        default=config.get("tracker_id"),
    )
    parser.add_argument(
        "--webhook_api_key",
        help="Api key for the webhook",
        required=config.get("webhook_api_key") is None,
        default=config.get("webhook_api_key"),
    )
    args = parser.parse_args()

    from_location = args.start
    to_location = args.end
    interval = args.interval
    duration = args.duration
    api_key = args.api_key
    webhook_url = args.webhook_url
    trackerId = args.tracker_id
    webhook_api_key = args.webhook_api_key

    # Load the MapBoxService class
    mapbox_service = Mapbox_service(api_key)
    from_addr_feature = mapbox_service.get_coordinates(from_location)
    to_addr_feature = mapbox_service.get_coordinates(to_location)

    total_distance, total_duration, speeds, distances, durations, coordinates = (
        mapbox_service.get_directions(from_addr_feature, to_addr_feature)
    )

    tracker_sim = TrackerSim(speeds, distances, durations, coordinates)

    duration = duration if duration > 0 else int(total_duration)

    print(
        f"""
SIMULATING ROUTE
TRACKER ID: {trackerId}
FROM: {from_location} (lat: {from_addr_feature['geometry']['coordinates'][1]}, lng: {from_addr_feature['geometry']['coordinates'][0]})
TO: {to_location} (lat: {to_addr_feature['geometry']['coordinates'][1]}, lng: {to_addr_feature['geometry']['coordinates'][0]})

Total route distance: {total_distance}m
Total route duration: {total_duration}s

Simulated duration: {duration}s
Update intervals: {interval}s

TO EXIT, press Ctrl+C

"""
    )

    # Create a progress bar to display the elapsed time and the estimated coordinates
    pbar = tqdm(range(0, duration, interval))
    for time in pbar:
        estimated_coords = tracker_sim.get_coords(time)
        pbar.set_description(f"Elapsed time: {time}s, Coords: {estimated_coords}")
        request_body = {
            "id": trackerId,
            "coordinates": {"lat": estimated_coords[1], "lng": estimated_coords[0]},
        }
        response = post(webhook_url, request_body, webhook_api_key)
        if not (response.status_code >= 200 and response.status_code < 300):
            print(
                f"Failed to POST the simulated coordinates to the webhook URL: {webhook_url} {response.status_code}"
            )
        sleep(interval)
