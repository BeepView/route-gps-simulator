import mapbox
from geojson import FeatureCollection, Feature


class Mapbox_service:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_coordinates(self, location: str) -> Feature:
        geocoding = mapbox.Geocoder(access_token=self.api_key)

        response = geocoding.forward(location)
        json = response.json()
        if not json.get("features"):
            raise ValueError(f"Location {location} not found")

        feature_collection = FeatureCollection(**json)

        return feature_collection.features[0]

    def get_directions(
        self, from_location: Feature, to_location: Feature
    ) -> tuple[
        float, float, list[float], list[float], list[float], list[tuple[float, float]]
    ]:
        directions = mapbox.Directions(access_token=self.api_key)

        response = directions.directions(
            [from_location, to_location],
            profile="mapbox/driving",
            alternatives=False,
            annotations=["speed", "duration", "distance"],
            continue_straight=False,
            geometries="geojson",
            overview="full",
            steps=False,
            notifications=None,
        )

        json = response.json()

        if not json.get("routes"):
            raise ValueError("No route found")
        if not json["routes"][0].get("legs"):
            raise ValueError("No legs found")
        if not json["routes"][0]["legs"][0].get("annotation"):
            raise ValueError("No annotations found")
        if not json["routes"][0].get("geometry"):
            raise ValueError("No geometry found")

        total_distance = json["routes"][0]["distance"]
        total_duration = json["routes"][0]["duration"]
        speeds = json["routes"][0]["legs"][0]["annotation"]["speed"]
        durations = json["routes"][0]["legs"][0]["annotation"]["duration"]
        distances = json["routes"][0]["legs"][0]["annotation"]["distance"]
        coordinates = json["routes"][0]["geometry"]["coordinates"]

        return (
            total_distance,
            total_duration,
            speeds,
            distances,
            durations,
            coordinates,
        )
