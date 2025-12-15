from parking_lot.models.vehicle import Vehicle, VehicleType


def test_vehicle_defaults_to_car():
    v = Vehicle(registration_number="KA-01-HH-1234", color="White")
    assert v.type == VehicleType.CAR


def test_vehicle_with_explicit_type():
    v = Vehicle(registration_number="KA-02-PP-0001", color="Red", type=VehicleType.BIKE)
    assert v.type == VehicleType.BIKE
