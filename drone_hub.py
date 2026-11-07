"""Fleet container for registering and coordinating drones."""
from drone import Drone

class DroneHub:
    """Manage a collection of drone instances."""
    def __init__(self, name: str) -> None:
        if not name.strip():
            raise ValueError("Hub name cannot be empty.")
        self.name = name
        self.drones: list[Drone] = []

    def add_drone(self, drone: Drone) -> None:
        if any(existing.id == drone.id for existing in self.drones):
            raise ValueError(f"Drone {drone.id} is already registered in this hub.")
        self.drones.append(drone)

    def list_drones(self) -> list[str]:
        return [str(drone) for drone in self.drones]

    def relocate_all_drones(self, new_location: tuple[float, float]) -> None:
        for drone in self.drones:
            drone.move_to(new_location)

    def __str__(self) -> str:
        lines = [f"--- DroneHub {self.name}: {len(self.drones)} drones docked ---"]
        lines.extend(f"[{index}]: {drone.id} {drone.get_type()}" for index, drone in enumerate(self.drones))
        return "\n".join(lines)
