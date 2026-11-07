"""Independent tests for the portfolio implementation."""
import unittest
from drone import Drone
from delivery_drone import DeliveryDrone
from survey_drone import SurveyDrone
from drone_hub import DroneHub
from drone_exceptions import DuplicateIDError, CargoLimitError

class DroneFleetTests(unittest.TestCase):
    def setUp(self):
        Drone._registered_ids.clear()

    def test_base_drone_initialization_and_movement(self):
        drone = Drone("D-1", 90, (41.0, 29.0))
        self.assertEqual(drone.current_location, (41.0, 29.0))
        drone.move_to((40.0, 28.0))
        self.assertEqual(drone.current_location, (40.0, 28.0))
        self.assertEqual(drone.get_type(), "Generic Drone")

    def test_duplicate_id_is_rejected(self):
        Drone("D-1", 90, (0.0, 0.0))
        with self.assertRaises(DuplicateIDError):
            Drone("D-1", 80, (1.0, 1.0))

    def test_invalid_base_drone_values(self):
        with self.assertRaises(ValueError):
            Drone("", 90, (0.0, 0.0))
        with self.assertRaises(ValueError):
            Drone("D-2", 0, (0.0, 0.0))

    def test_delivery_drone_cargo_lifecycle(self):
        drone = DeliveryDrone("D-1", 90, (0.0, 0.0), 10)
        drone.load_cargo(4)
        self.assertEqual(drone.current_cargo, 4)
        drone.deliver_cargo()
        self.assertEqual(drone.current_cargo, 0)
        self.assertEqual(drone.get_type(), "Delivery Drone")

    def test_delivery_capacity_limit(self):
        drone = DeliveryDrone("D-1", 90, (0.0, 0.0), 10)
        drone.load_cargo(7)
        with self.assertRaises(CargoLimitError):
            drone.load_cargo(4)
        self.assertEqual(drone.current_cargo, 7)

    def test_invalid_cargo_is_rejected(self):
        drone = DeliveryDrone("D-1", 90, (0.0, 0.0), 10)
        with self.assertRaises(ValueError):
            drone.load_cargo(0)

    def test_survey_drone_records_multiple_scans(self):
        drone = SurveyDrone("S-1", 80, (0.0, 0.0), "4K")
        first, second = [(1.0, 2.0)], [(3.0, 4.0), (5.0, 6.0)]
        drone.scan_area(first)
        drone.scan_area(second)
        self.assertEqual(drone.survey_data, first + second)
        self.assertEqual(drone.get_type(), "Survey Drone")

    def test_hub_adds_and_lists_drones(self):
        hub = DroneHub("Central")
        hub.add_drone(DeliveryDrone("D-1", 90, (0.0, 0.0), 10))
        self.assertEqual(len(hub.drones), 1)
        self.assertIn("D-1", hub.list_drones()[0])

    def test_hub_rejects_duplicate_registration(self):
        hub = DroneHub("Central")
        drone = Drone("D-1", 90, (0.0, 0.0))
        hub.add_drone(drone)
        with self.assertRaises(ValueError):
            hub.add_drone(drone)

    def test_hub_relocates_entire_fleet(self):
        hub = DroneHub("Central")
        first = DeliveryDrone("D-1", 90, (0.0, 0.0), 10)
        second = SurveyDrone("S-1", 80, (1.0, 1.0), "HD")
        hub.add_drone(first)
        hub.add_drone(second)
        destination = (41.0, 29.0)
        hub.relocate_all_drones(destination)
        self.assertEqual(first.current_location, destination)
        self.assertEqual(second.current_location, destination)

if __name__ == "__main__":
    unittest.main()
