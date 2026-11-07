"""Delivery drone model with cargo-capacity management."""
from drone import Drone
from drone_exceptions import CargoLimitError

class DeliveryDrone(Drone):
    """A drone that carries and delivers cargo."""
    def __init__(self, drone_id: str, max_speed: int, current_location: tuple[float, float], cargo_capacity: float) -> None:
        if cargo_capacity <= 0:
            raise ValueError("Cargo capacity must be positive.")
        super().__init__(drone_id, max_speed, current_location)
        self.cargo_capacity = float(cargo_capacity)
        self.current_cargo = 0.0

    def load_cargo(self, weight: float) -> None:
        if weight <= 0:
            raise ValueError("Cargo weight must be positive.")
        if self.current_cargo + weight > self.cargo_capacity:
            raise CargoLimitError()
        self.current_cargo += weight

    def deliver_cargo(self) -> None:
        self.current_cargo = 0.0

    def get_type(self) -> str:
        return "Delivery Drone"
