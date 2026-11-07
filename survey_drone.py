"""Survey drone model for recording scanned coordinates."""
from drone import Drone

class SurveyDrone(Drone):
    """A drone that records coordinates from area surveys."""
    def __init__(self, drone_id: str, max_speed: int, current_location: tuple[float, float], camera_quality: str) -> None:
        if not camera_quality.strip():
            raise ValueError("Camera quality cannot be empty.")
        super().__init__(drone_id, max_speed, current_location)
        self.camera_quality = camera_quality
        self.survey_data: list[tuple[float, float]] = []

    def scan_area(self, area_coordinates: list[tuple[float, float]]) -> None:
        self.survey_data.extend(area_coordinates)

    def get_type(self) -> str:
        return "Survey Drone"
