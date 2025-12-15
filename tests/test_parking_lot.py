import pytest

from parking_lot.parking_lot import ParkingLot
from parking_lot.models.vehicle import Vehicle, VehicleType


def make_vehicle(reg_no: str, color: str, type: VehicleType = VehicleType.CAR) -> Vehicle:
    return Vehicle(registration_number=reg_no, color=color, type=type)


def test_create_parking_lot_capacity_positive():
    lot = ParkingLot(3)
    assert lot.capacity == 3


def test_create_parking_lot_invalid_capacity():
    with pytest.raises(ValueError):
        ParkingLot(0)


def test_park_allocates_first_available_slot():
    lot = ParkingLot(2)
    t1 = lot.park(make_vehicle("KA-01-HH-1234", "White"))
    t2 = lot.park(make_vehicle("KA-01-HH-9999", "Black"))
    assert t1 is not None and t1.slot == 1
    assert t2 is not None and t2.slot == 2


def test_park_returns_none_when_full():
    lot = ParkingLot(1)
    _ = lot.park(make_vehicle("KA-01-AA-0001", "Blue"))
    t2 = lot.park(make_vehicle("KA-01-AA-0002", "Red"))
    assert t2 is None


def test_leave_frees_slot_and_removes_ticket():
    lot = ParkingLot(2)
    _ = lot.park(make_vehicle("KA-01-HH-1234", "White"))  # slot 1
    ok = lot.leave(1)
    assert ok is True
    # Now slot 1 should be free; next park gets slot 1 again
    t2 = lot.park(make_vehicle("KA-01-HH-0001", "Green"))
    assert t2 is not None and t2.slot == 1


def test_leave_invalid_slot():
    lot = ParkingLot(2)
    assert lot.leave(3) is False


def test_status_lists_only_occupied_slots():
    lot = ParkingLot(3)
    _ = lot.park(make_vehicle("KA-01-HH-1234", "White"))  # slot 1
    _ = lot.park(make_vehicle("KA-01-HH-9999", "Black"))  # slot 2
    lines = lot.status()
    assert lines[0].startswith("Slot No.")
    # Only 2 occupied slots should be listed after header
    assert len(lines) == 3
    assert "KA-01-HH-1234" in lines[1]
    assert "KA-01-HH-9999" in lines[2]


def test_find_by_color_and_slot_by_reg():
    lot = ParkingLot(3)
    _ = lot.park(make_vehicle("KA-01-AB-1111", "Red"))     # slot 1
    _ = lot.park(make_vehicle("KA-01-AB-2222", "Red"))     # slot 2
    _ = lot.park(make_vehicle("KA-01-AB-3333", "Blue"))    # slot 3

    regs = lot.find_by_color("Red")
    assert set(regs) == {"KA-01-AB-1111", "KA-01-AB-2222"}

    slot = lot.find_slot_by_reg("KA-01-AB-3333")
    assert slot == 3

    not_found_slot = lot.find_slot_by_reg("NO-SUCH-REG")
    assert not_found_slot is None
