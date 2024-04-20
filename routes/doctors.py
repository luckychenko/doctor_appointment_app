from fastapi import APIRouter

from schemas.doctors import DoctorsCreateEdit, doctors
from services.doctors import doctor_services


doctors_router = APIRouter()


@doctors_router.get('/', status_code=200)
def get_doctors():
    data = doctor_services.parse_doctors(doctors)
    return {'message':'successful', 'data': data} 

@doctors_router.get('/{doctor_id}', status_code=200)
def get_doctor(doctor_id: int):
    data = doctor_services.get_doctor_by_id(doctor_id)
    return {'message':'successful', 'data': data}

@doctors_router.post('/', status_code=201)
def create_doctor(payload: DoctorsCreateEdit):
    data = doctor_services.create_doctor(payload)
    return {'message':'created', 'data': data}

@doctors_router.put('/{doctor_id}', status_code=200)
def edit_doctor(doctor_id: int, payload: DoctorsCreateEdit):
    data = doctor_services.edit_doctor(doctor_id, payload)
    return {'message': 'doctor edited successfully', 'data': data}

@doctors_router.delete('/{doctor_id}', status_code=204)
def delete_doctor(doctor_id: int):
    doctor_services.delete_doctor(doctor_id)
    return {'message': 'doctor deleted successfully.'}