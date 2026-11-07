"""Domain-specific exceptions for drone fleet operations."""

class DroneError(Exception):
    """Base exception for drone-related errors."""

class DuplicateIDError(DroneError):
    """Raised when a drone identifier is already registered."""
    def __init__(self, drone_id: str) -> None:
        super().__init__(f"Drone id {drone_id} already exists!")

class CargoLimitError(DroneError):
    """Raised when a delivery drone would exceed its cargo capacity."""
    def __init__(self, message: str = "Weight exceeds maximum capacity!") -> None:
        super().__init__(message)
