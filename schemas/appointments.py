from datetime import date
from typing import Annotated, ClassVar
from pydantic import BaseModel, Field



'''
The Appointment Class autogenerates the Appointment id attribute on initializing (when a appointment is created)
'''

class Appointments(BaseModel):

    # Override init method to keep track of last Appointment id
    def __init__(self, **data):
        super().__init__(**data)
        Appointments.last_id += 1

        
    last_id: ClassVar[int] = 0
    id: Annotated[int, Field(default_factory=lambda: Appointments.last_id)]
    patient: int
    doctor: int
    date: date


class AppointmentsCreateEdit(BaseModel):
    patient: int
    doctor: int
    date: date



appointments: dict[int, Appointments] = {
    0: Appointments(id=0, patient=2, doctor=2, date="2024-04-22"),
    1: Appointments(id=1, patient=0, doctor=1, date="2024-05-01")
}