from fastapi import APIRouter

from schemas.appointments import AppointmentsCreateEdit, Appointments
from services.appointments import appointment_services


appointments_router = APIRouter()


@appointments_router.get('/', status_code=200)
def get_appointments():
    data = appointment_services.parse_appointments(Appointments)
    return {'message':'successful', 'data': data} 

@appointments_router.get('/{appointment_id}', status_code=200)
def get_appointment(appointment_id: int):
    data = appointment_services.get_appointment_by_id(appointment_id)
    return {'message':'successful', 'data': data}

@appointments_router.post('/', status_code=201)
def create_appointment(payload: AppointmentsCreateEdit):
    data = appointment_services.create_appointment(payload)
    return {'message':'created', 'data': data}

@appointments_router.put('/{appointment_id}', status_code=200)
def edit_appointment(appointment_id: int, payload: AppointmentsCreateEdit):
    data = appointment_services.edit_appointment(appointment_id, payload)
    return {'message': 'appointment edited successfully', 'data': data}

@appointments_router.delete('/{appointment_id}', status_code=204)
def delete_appointment(appointment_id: int):
    appointment_services.delete_appointment(appointment_id)
    return {'message': 'appointment deleted successfully.'}