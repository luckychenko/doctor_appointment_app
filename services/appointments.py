
import copy
from fastapi import HTTPException
from schemas.appointments import Appointment, appointments
from schemas.doctors import doctors
from schemas.patients import patients
from utils.helpers import Helpers


class AppointmentsServer:

    @staticmethod
    def parse_appointments():
        data: list = []
        for doc in appointments:            
            data.append(appointments[doc])
        return AppointmentsServer.parser(data)
    
    # get the patient and doctor details
    def parser(db: list[Appointment]):
        clone = copy.deepcopy(db)

        for row in clone:
            row.patient = patients.get(row.patient)
            row.doctor = doctors.get(row.doctor)
        return clone

    @staticmethod
    def get_appointment_by_id(id:int):
        appointment = appointments.get(id)
        if not appointment:
            raise HTTPException(detail='appointment not found.', status_code=404)
        
        data: list = []
        data.append(appointments[id])
        return AppointmentsServer.parser(data)
        

    @staticmethod
    def cancel_appointment(appointment_id: int):
        appointment = Helpers.check_appointment(appointment_id)
        del appointments[appointment.id]


    @staticmethod
    def finalize_appointment(appointment_id: int):
        appointment = Helpers.check_appointment(appointment_id)
        return appointment




appointment_services = AppointmentsServer()