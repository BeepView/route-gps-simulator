import numpy as np


class TrackerSim:
    def __init__(
        self,
        speeds: list[float],
        distances: list[float],
        durations: list[float],
        coordinates: list[tuple[float, float]],
    ) -> None:
        self.speeds = speeds
        self.distances = distances
        self.durations = durations
        self.coordinates = coordinates

        self.segment_times = np.divide(self.distances, self.speeds)
        self.cumulative_times = np.cumsum(self.segment_times)

    def get_coords(self, elapsed_time: int) -> tuple[float, float]:
        # Binary search for target segment
        target_segment_index = np.searchsorted(self.cumulative_times, elapsed_time)

        if target_segment_index > 0:
            start_coords = self.coordinates[target_segment_index - 1]
            end_coords = self.coordinates[target_segment_index]
            segment_duration = self.segment_times[target_segment_index - 1]
            cumulative_time_before_segment = (
                self.cumulative_times[target_segment_index - 2]
                if target_segment_index > 1
                else 0
            )

            estimated_lat = (
                start_coords[0]
                + (end_coords[0] - start_coords[0])
                * (elapsed_time - cumulative_time_before_segment)
                / segment_duration
            )
            estimated_lng = (
                start_coords[1]
                + (end_coords[1] - start_coords[1])
                * (elapsed_time - cumulative_time_before_segment)
                / segment_duration
            )
            return estimated_lat, estimated_lng
        else:
            return self.coordinates[0]
