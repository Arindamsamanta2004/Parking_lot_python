#!/usr/bin/env python3
from typing import Optional

from parking_lot.parking_lot import ParkingLot
from parking_lot.models.vehicle import Vehicle, VehicleType


def parse_vehicle_type(s: str) -> VehicleType:
    s = s.strip().upper()
    return VehicleType[s] if s in VehicleType.__members__ else VehicleType.CAR


def print_help():
    print("Commands:")
    print("  create <capacity>")
    print("  park <reg_no> <color> [type]")
    print("  leave <slot>")
    print("  status")
    print("  find_reg_by_color <color>")
    print("  find_slot_by_reg <reg_no>")
    print("  help")
    print("  exit")


def main():
    lot: Optional[ParkingLot] = None
    print("Simple Parking Lot CLI. Type 'help' for commands.")
    while True:
        try:
            cmd = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break
        if not cmd:
            continue
        parts = cmd.split()
        op = parts[0].lower()
        args = parts[1:]

        try:
            if op == "help":
                print_help()
            elif op == "exit":
                print("Bye!")
                break
            elif op == "create":
                if len(args) != 1:
                    print("Usage: create <capacity>")
                    continue
                lot = ParkingLot(int(args[0]))
                print(f"Created parking lot with {lot.capacity} slots")
            elif op == "park":
                if lot is None:
                    print("Create a lot first: create <capacity>")
                    continue
                if len(args) < 2:
                    print("Usage: park <reg_no> <color> [type]")
                    continue
                vtype = parse_vehicle_type(args[2]) if len(args) >= 3 else VehicleType.CAR
                ticket = lot.park(Vehicle(registration_number=args[0], color=args[1], type=vtype))
                if ticket:
                    print(f"Allocated slot number: {ticket.slot}")
                else:
                    print("Sorry, parking lot is full")
            elif op == "leave":
                if lot is None:
                    print("Create a lot first: create <capacity>")
                    continue
                if len(args) != 1:
                    print("Usage: leave <slot>")
                    continue
                ok = lot.leave(int(args[0]))
                print("Slot freed" if ok else "Invalid slot")
            elif op == "status":
                if lot is None:
                    print("Create a lot first: create <capacity>")
                    continue
                for line in lot.status():
                    print(line)
            elif op == "find_reg_by_color":
                if lot is None:
                    print("Create a lot first: create <capacity>")
                    continue
                if len(args) != 1:
                    print("Usage: find_reg_by_color <color>")
                    continue
                regs = lot.find_by_color(args[0])
                print(", ".join(regs) if regs else "Not found")
            elif op == "find_slot_by_reg":
                if lot is None:
                    print("Create a lot first: create <capacity>")
                    continue
                if len(args) != 1:
                    print("Usage: find_slot_by_reg <reg_no>")
                    continue
                slot = lot.find_slot_by_reg(args[0])
                print(slot if slot is not None else "Not found")
            else:
                print("Unknown command. Type 'help'.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
