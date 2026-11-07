# Drone Fleet Management System

A Python portfolio project demonstrating object-oriented design for a small fleet of delivery and survey drones.

## Features
- A shared `Drone` base class with unique-ID protection and location updates
- Specialized `DeliveryDrone` and `SurveyDrone` subclasses
- Custom exceptions for duplicate IDs and cargo-capacity violations
- A `DroneHub` class for fleet registration, listing, and bulk relocation
- A runnable demonstration and automated unit tests

## Project structure
```text
.
├── drone.py
├── delivery_drone.py
├── survey_drone.py
├── drone_hub.py
├── drone_exceptions.py
├── demo.py
└── tests/
    └── test_fleet.py
```

## Requirements
- Python 3.10+
- No third-party dependencies

## Run the demo
```bash
python demo.py
```

## Run tests
```bash
python -m unittest discover -s tests -v
```

## Concepts demonstrated
Object-oriented programming, inheritance, method overriding, custom exceptions, type hints, validation, and unit testing.

## Academic integrity and project scope
This is a portfolio-oriented implementation based on programming concepts practiced in academic work. It is maintained separately from course submission repositories and does not include course handouts or instructor-provided test files.
