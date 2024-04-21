
from fastapi import HTTPException
from schemas.appointments import Appointments, appointments, AppointmentsCreateEdit


class AppointmentsServer:

    @staticmethod
    def parse_appointments(Appointments_dict):
        data: list = []
        for doc in Appointments_dict:
            data.append(appointments[doc])
        return data
    
    @staticmethod
    def get_appointment_by_id(id:int):
        appointment: dict = appointments.get(id)
        if not appointment:
            raise HTTPException(detail='appointment not found.', status_code=404)
        return appointment


    @staticmethod
    def create_appointment(payload: AppointmentsCreateEdit):
        # create a new appointment resource using the AppointmentsCreateEdit Model with payload data
        # since the Appointments Model autogenerate id for each instance

        new_appointment = Appointments(**payload.model_dump())
        appointments[new_appointment.id] = new_appointment
        return new_appointment
    

    @staticmethod
    def edit_appointment(appointment_id: int, payload: AppointmentsCreateEdit):
        #find the appointment from the DB
        app_found = appointments.get(appointment_id)
        # if found update the info else raise exception
        if not app_found:
            raise HTTPException(status_code=404, detail="appointment not found")
        else:            
            app_found.name = payload.name
            app_found.age = payload.age
            app_found.sex = payload.sex
            app_found.weight = payload.weight
            app_found.height = payload.height
            app_found.phone = payload.phone
        
        return app_found
        

    @staticmethod
    def delete_appointment(appointment_id: int):
        #find the appointment from the DB
        app_found = appointments.get(appointment_id)
        # if found delete record else raise exception
        if not app_found:
            raise HTTPException(status_code=404, detail="appointment not found")
        else: 
            del appointments[appointment_id]





appointment_services = AppointmentsServer()