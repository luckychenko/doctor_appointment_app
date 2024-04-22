from fastapi import APIRouter

from schemas.doctors import DoctorAvailable, DoctorCreateEdit
from services.doctors import doctor_services


doctors_router = APIRouter()


@doctors_router.get('/', status_code=200)
def get_doctors():
    data = doctor_services.parse_doctors()
    return {'message':'successful', 'data': data} 

@doctors_router.get('/{doctor_id}', status_code=200)
def get_doctor(doctor_id: int):
    data = doctor_services.get_doctor_by_id(doctor_id)
    return {'message':'successful', 'data': data}

@doctors_router.post('/', status_code=201)
def create_doctor(payload: DoctorCreateEdit):
    data = doctor_services.create_doctor(payload)
    return {'message':'created', 'data': data}

@doctors_router.put('/{doctor_id}', status_code=200)
def edit_doctor(doctor_id: int, payload: DoctorCreateEdit):
    data = doctor_services.edit_doctor(doctor_id, payload)
    return {'message': 'doctor edited successfully', 'data': data}

@doctors_router.patch("/{doctor_id}/availability/", status_code= 200)
def set_doctor_availability(doctor_id: int, available: DoctorAvailable):
    data = doctor_services.set_availability(doctor_id, available)
    return {"message": f"doctor availability set to {data}"}

@doctors_router.delete('/{doctor_id}', status_code=204)
def delete_doctor(doctor_id: int):
    doctor_services.delete_doctor(doctor_id)
    return {'message': 'doctor deleted successfully.'}