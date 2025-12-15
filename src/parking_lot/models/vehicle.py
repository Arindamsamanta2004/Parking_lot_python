from dataclasses import dataclass
from enum import Enum


class VehicleType(Enum):
    CAR = "CAR"
    BIKE = "BIKE"
    TRUCK = "TRUCK"


@dataclass(frozen=True)
class Vehicle:
    registration_number: str
    color: str
    type: VehicleType = VehicleType.CAR
