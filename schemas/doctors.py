import re
from typing import Annotated, ClassVar
from fastapi import HTTPException
from pydantic import BaseModel, Field, StringConstraints, field_validator


'''
The Doctor Class autogenerates the Doctor id attribute on initializing (when a doctor is created)
'''

class Doctors(BaseModel):

    # Override init method to keep track of last doctor id
    def __init__(self, **data):
        super().__init__(**data)
        Doctors.last_id += 1

        
    last_id: ClassVar[int] = 0
    id: Annotated[int, Field(default_factory=lambda: Doctors.last_id)]
    name: str
    specialization: str
    phone: Annotated[str, StringConstraints(strip_whitespace=True)] 
    is_available: bool = True 


    @field_validator('phone')
    def check_phone_number(cls, v):
        # Custom validation to ensure phone number format is valid
        if not re.match(r'^0\d{10}$', v):
            raise HTTPException(detail='Invalid phone number format', status_code=400)
        return v


class DoctorsCreateEdit(BaseModel):
    name: str
    specialization: str
    phone: str
    is_available: bool = True



doctors: dict[int, Doctors] = {
    0: Doctors(id=0, name="Mark Ogbor", specialization="Pediatrics", phone="08139585870"),
    1: Doctors(id=1, name="Samchi Akpan", specialization="Ophthalmology", phone="09136985450"),
    2: Doctors(id=2, name="Zainab Musa", specialization="Dermatology", phone="09055665881"),
}