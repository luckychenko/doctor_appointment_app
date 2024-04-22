

import re
from fastapi import HTTPException


class Helpers:

    @staticmethod
    def check_phone_number(cls, v):
        # Custom validation to ensure phone number format is valid
        if not re.match(r'^0\d{10}$', v):
            raise HTTPException(detail='Invalid phone number format', status_code=400)
        return v
    

    @staticmethod
    def check_appointment(appointment_id):        
        from schemas.doctors import doctors
        from schemas.appointments import appointments
        
        appointment = next((appointment for appointment in appointments.values() if appointment.id == appointment_id), None)
        if not appointment:
            raise HTTPException(status_code=404, detail="appointment not found")      
             
        doctor = next((doctor for doctor in doctors.values() if doctor.id == appointment.doctor), None)
        if not doctor:
            raise HTTPException(status_code=404, detail="doctor not found")
        
        doctor.is_available = True

        return appointment
    

