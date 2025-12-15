# Parking Lot

Simple CLI application to manage a parking lot: create a lot, park vehicles, free slots, and query status.

## Setup

- Prerequisites: Python 3.10+
- Optional but recommended: use a virtual environment

```bash
cd "/home/arinsamn/Documents/RedHat_Tasks /Parking_Lot"
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run

```bash
python src/main.py
```

You will see a prompt. Type `help` to see available commands.

## Commands

- `create <capacity>`: Initialize the lot with a number of slots.
- `park <reg_no> <color> [type]`: Park a vehicle. `type` is optional; defaults to `CAR`. Valid types: `CAR`, `BIKE`, `TRUCK`.
- `leave <slot>`: Free a slot by its number.
- `status`: Show occupied slots.
- `find_reg_by_color <color>`: List registration numbers of vehicles with the given color.
- `find_slot_by_reg <reg_no>`: Show slot number for a given registration number.
- `help`: Show command summary.
- `exit`: Quit the CLI.

## Examples

```bash
python src/main.py
> help
> create 6
> park KA-01-HH-1234 White CAR
> status
Slot No.    Registration No    Color
1           KA-01-HH-1234     White
> leave 1
> status
> exit
```

## Notes

- Vehicle model uses `registration_number`, `color`, and `type` (enum).
- If you use VS Code, set the interpreter to `.venv/bin/python` for best linting and run support.
