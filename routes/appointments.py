from fastapi import APIRouter
from services.appointments import appointment_services


appointments_router = APIRouter()


@appointments_router.get('/', status_code=200)
def get_appointments():
    data = appointment_services.parse_appointments()
    return {'message':'successful', 'data': data} 

@appointments_router.get('/{appointment_id}', status_code=200)
def get_appointment(appointment_id: int):
    data = appointment_services.get_appointment_by_id(appointment_id)
    return {'message':'successful', 'data': data}

@appointments_router.patch("/{appointment_id}/status/", status_code=200)
def complete_appointment(appointment_id: int):
    appointment_services.finalize_appointment(appointment_id)    
    return {'message': 'appointment completed'}

@appointments_router.delete("/{appointment_id}/cancel/", status_code=204)
def cancel_appointment(appointment_id: int):
    appointment_services.cancel_appointment(appointment_id)    
    return {'message': 'appointment cancelled'}