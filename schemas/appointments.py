from datetime import date
from typing import Annotated, ClassVar
from pydantic import BaseModel, Field

from schemas.doctors import Doctor
from schemas.patients import Patient



'''
The Appointment Class autogenerates the Appointment id attribute on initializing (when a appointment is created)
'''

class Appointment(BaseModel):

    # Override init method to keep track of last Appointment id
    def __init__(self, **data):
        super().__init__(**data)
        Appointment.last_id += 1

        
    last_id: ClassVar[int] = 0
    id: Annotated[int, Field(default_factory=lambda: Appointment.last_id)]
    patient: int | Patient
    doctor: int | Doctor
    date: date


class AppointmentCreateEdit(BaseModel):
    patient: int | Patient
    doctor: int | Doctor
    date: date

class AppointmentPayload(BaseModel):
    date: date


appointments: dict[int, Appointment] = {
    0: Appointment(id=0, patient=2, doctor=0, date="2024-04-22"),
    1: Appointment(id=1, patient=0, doctor=2, date="2024-05-01")
}