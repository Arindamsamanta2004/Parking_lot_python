from dataclasses import dataclass
from datetime import datetime

@dataclass
class Ticket:
    slot: int
    plate: str
    issued_at: datetime
    left_at: datetime | None = None

    def close(self, left_at: datetime) -> None:
        self.left_at = left_at
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Ticket:
    slot: int
    vehicle_reg_no: str
    issued_at: datetime
