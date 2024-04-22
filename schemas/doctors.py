from typing import Annotated, ClassVar
from pydantic import BaseModel, Field, StringConstraints, field_validator

from utils.helpers import Helpers


'''
The Doctor Class autogenerates the Doctor id attribute on initializing (when a doctor is created)
'''

class Doctor(BaseModel):

    # Override init method to keep track of last doctor id
    def __init__(self, **data):
        super().__init__(**data)
        Doctor.last_id += 1

        
    last_id: ClassVar[int] = 0
    id: Annotated[int, Field(default_factory=lambda: Doctor.last_id)]
    name: str
    specialization: str
    phone: Annotated[str, StringConstraints(strip_whitespace=True)]  
    is_available: bool = Field(default=True)


    @field_validator('phone')    
    def validate(cls,v):
        return Helpers.check_phone_number(cls, v)


class DoctorCreateEdit(BaseModel):
    name: str
    specialization: str
    phone: Annotated[str, StringConstraints(strip_whitespace=True)] 
    is_available: bool = Field(default=True)


    @field_validator('phone')    
    def validate(cls,v):
        return Helpers.check_phone_number(cls, v)
    

class DoctorAvailable(BaseModel):
    is_available: bool


doctors: dict[int, Doctor] = {
    0: Doctor(id=0, name="Mark Ogbor", specialization="Pediatrics", phone="08139585870", is_available=False),
    1: Doctor(id=1, name="Samchi Akpan", specialization="Ophthalmology", phone="09136985450", is_available=True),
    2: Doctor(id=2, name="Zainab Musa", specialization="Dermatology", phone="09055665881", is_available=False)
}