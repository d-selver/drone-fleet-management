"""Base model shared by all drone types."""
from drone_exceptions import DuplicateIDError

class Drone:
    """Represent a drone with an ID, speed, and geographic location."""
    _registered_ids: set[str] = set()

    def __init__(self, drone_id: str, max_speed: int, current_location: tuple[float, float]) -> None:
        if not drone_id.strip():
            raise ValueError("Drone ID cannot be empty.")
        if drone_id in Drone._registered_ids:
            raise DuplicateIDError(drone_id)
        if max_speed <= 0:
            raise ValueError("Maximum speed must be positive.")
        self.id = drone_id
        self.max_speed = max_speed
        self.current_location = current_location
        Drone._registered_ids.add(drone_id)

    def move_to(self, new_location: tuple[float, float]) -> None:
        """Update the drone's latitude/longitude pair."""
        if len(new_location) != 2:
            raise ValueError("A location must contain latitude and longitude.")
        self.current_location = new_location

    def get_type(self) -> str:
        return "Generic Drone"

    def __str__(self) -> str:
        return f"Drone ID: {self.id} Type: {self.get_type()}"
