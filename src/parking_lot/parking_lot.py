from datetime import datetime
from typing import Dict, Optional, List

from .models.vehicle import Vehicle
from .models.ticket import Ticket


class ParkingLot:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self.capacity = capacity
        self.slots: Dict[int, Optional[Vehicle]] = {i: None for i in range(1, capacity + 1)}
        self.tickets: Dict[str, Ticket] = {}

    def park(self, vehicle: Vehicle) -> Optional[Ticket]:
        for slot, v in self.slots.items():
            if v is None:
                self.slots[slot] = vehicle
                ticket = Ticket(slot=slot, vehicle_reg_no=vehicle.registration_number, issued_at=datetime.now())
                self.tickets[vehicle.registration_number] = ticket
                return ticket
        return None

    def leave(self, slot: int) -> bool:
        if slot not in self.slots or self.slots[slot] is None:
            return False
        vehicle = self.slots[slot]
        if vehicle is not None:
            self.tickets.pop(vehicle.registration_number, None)
        self.slots[slot] = None
        return True

    def status(self) -> List[str]:
        lines = ["Slot No.    Registration No    Color"]
        for slot in sorted(self.slots.keys()):
            v = self.slots[slot]
            if v:
                lines.append(f"{slot:<12}{v.registration_number:<18}{v.color}")
        return lines

    def find_by_color(self, color: str) -> List[str]:
        return [v.registration_number for v in self.slots.values() if v and v.color.lower() == color.lower()]

    def find_slot_by_reg(self, reg_no: str) -> Optional[int]:
        for slot, v in self.slots.items():
            if v and v.registration_number == reg_no:
                return slot
        return None
