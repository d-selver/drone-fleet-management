"""Run a short demonstration of drone fleet operations."""
from delivery_drone import DeliveryDrone
from drone_hub import DroneHub
from survey_drone import SurveyDrone

def main() -> None:
    hub = DroneHub("Central Fleet")
    delivery = DeliveryDrone("D-1001", 100, (41.0082, 28.9784), 12.5)
    survey = SurveyDrone("S-1001", 80, (41.0082, 28.9784), "4K")
    delivery.load_cargo(5.0)
    survey.scan_area([(41.01, 28.98), (41.02, 28.99)])
    hub.add_drone(delivery)
    hub.add_drone(survey)
    print(hub)
    print("Survey points recorded:", len(survey.survey_data))
    hub.relocate_all_drones((41.015, 28.985))
    print("Fleet relocated to:", delivery.current_location)

if __name__ == "__main__":
    main()
