from fastapi import APIRouter

from schemas.patients import PatientCreateEdit, patients
from services.patients import patient_services


patients_router = APIRouter()


@patients_router.get('/', status_code=200)
def get_patients():
    data = patient_services.parse_patients(patients)
    return {'message':'successful', 'data': data} 

@patients_router.get('/{patient_id}', status_code=200)
def get_patient(patient_id: int):
    data = patient_services.get_patient_by_id(patient_id)
    return {'message':'successful', 'data': data}

@patients_router.post('/', status_code=201)
def create_patient(payload: PatientCreateEdit):
    data = patient_services.create_patient(payload)
    return {'message':'created', 'data': data}

@patients_router.put('/{patient_id}', status_code=200)
def edit_patient(patient_id: int, payload: PatientCreateEdit):
    data = patient_services.edit_patient(patient_id, payload)
    return {'message': 'patient edited successfully', 'data': data}

@patients_router.delete('/{patient_id}', status_code=204)
def delete_patient(patient_id: int):
    patient_services.delete_patient(patient_id)
    return {'message': 'patient deleted successfully.'}