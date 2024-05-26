#!/usr/bin/env python3

# for argument parsing
import argparse

# for reading the defaults file
import json

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
    args = parser.parse_args()

    from_location = args.start
    to_location = args.end
    interval = args.interval
    duration = args.duration
    api_key = args.api_key
