from pydantic import BaseModel
from enum import Enum

class Status(str, Enum):
    pending = "pending"
    confirmed = "confirmed"
    cancelled = "cancelled"

class AppointmentCreate(BaseModel):
    patient_name: str
    date: str

class Appointment(AppointmentCreate):
    id: int
    status: Status