from typing import Annotated, ClassVar
from pydantic import BaseModel, Field, StringConstraints, field_validator

from utils.helpers import Helpers


'''
The Patient Class autogenerates the Doctor id attribute on initializing (when a doctor is created)
'''

class Patient(BaseModel):

    # Override init method to keep track of last patient id
    def __init__(self, **data):
        super().__init__(**data)
        Patient.last_id += 1

        
    last_id: ClassVar[int] = 0
    id: Annotated[int, Field(default_factory=lambda: Patient.last_id)]
    name: str
    age: int
    sex: str
    weight: Annotated[float, Field(strict=True, gt=0)] = None
    height: Annotated[float, Field(strict=True, gt=0)] = None
    phone: Annotated[str, StringConstraints(strip_whitespace=True)] 


    @field_validator('phone')
    def validate(cls,v):
        return Helpers.check_phone_number(cls, v)


class PatientCreateEdit(BaseModel):
    name: str
    age: int
    sex: str
    weight: Annotated[float, Field(strict=True, gt=0)] = None
    height: Annotated[float, Field(strict=True, gt=0)] = None
    phone: Annotated[str, StringConstraints(strip_whitespace=True)] 

    @field_validator('phone')
    def validate(cls,v):
        return Helpers.check_phone_number(cls, v)



patients: dict[int, Patient] = {
    0: Patient(id=0, name="Samuel Adaku", age=35, sex="Male", weight=75.2, height=181.55, phone="08139585870"),
    1: Patient(id=1, name="Ladun Ozor", age=62, sex="Female", weight=82.33, height=131.10, phone="09136985450"),
    2: Patient(id=2, name="Benita Nkemowo", age=20, sex="Female", weight=63, height=146.0,  phone="09055665881")
}