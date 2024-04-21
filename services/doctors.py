
from fastapi import HTTPException
from schemas.doctors import Doctor, DoctorCreateEdit, doctors


class DoctorsServer:

    @staticmethod
    def parse_doctors(doctors_dict):
        data: list = []
        for doc in doctors_dict:
            data.append(doctors[doc])
        return data
    
    @staticmethod
    def get_doctor_by_id(id:int):
        doctor: dict = doctors.get(id)
        if not doctor:
            raise HTTPException(detail='doctor not found.', status_code=404)
        return doctor


    @staticmethod
    def create_doctor(payload: DoctorCreateEdit):
        # create a new doctor resource using the DoctorsCreateEdit Model with payload data
        # since the Doctors Model autogenerate id for each instance

        new_doctor = Doctor(**payload.model_dump())
        doctors[new_doctor.id] = new_doctor
        return new_doctor
    

    @staticmethod
    def edit_doctor(doctor_id: int, payload: DoctorCreateEdit):
        #find the doctor from the DB
        doc_found = doctors.get(doctor_id)
        # if found update the info else raise exception
        if not doc_found:
            raise HTTPException(status_code=404, detail="doctor not found")
        else:            
            doc_found.name = payload.name
            doc_found.specialization = payload.specialization
            doc_found.phone = payload.phone
            doc_found.is_available = payload.is_available
        
        return doc_found
        
    def set_availability(doctor_id: int, is_available: bool):
        doctor = next((doctor for doctor in doctors if doctor.id == doctor_id), None)
        if not doctor:
            raise HTTPException(status_code=404, detail="doctor not found")
        
        doctor.is_available = is_available
        return is_available

    @staticmethod
    def delete_doctor(doctor_id: int):
        #find the doctor from the DB
        doc_found = doctors.get(doctor_id)
        # if found delete record else raise exception
        if not doc_found:
            raise HTTPException(status_code=404, detail="doctor not found")
        else: 
            del doctors[doctor_id]





doctor_services = DoctorsServer()