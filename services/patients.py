
from fastapi import HTTPException
from schemas.appointments import Appointment, AppointmentPayload, appointments
from schemas.patients import Patient, patients, PatientCreateEdit
from schemas.doctors import doctors


class PatientsServer:

    @staticmethod
    def parse_patients():
        data: list = []
        for doc in patients:
            data.append(patients[doc])
        return data
    
    @staticmethod
    def get_patient_by_id(id:int):
        patient: dict = patients.get(id)
        if not patient:
            raise HTTPException(detail='patient not found.', status_code=404)
        return patient


    @staticmethod
    def create_patient(payload: PatientCreateEdit):
        # create a new patient resource using the patientsCreateEdit Model with payload data
        # since the patients Model autogenerate id for each instance

        new_patient = Patient(**payload.model_dump())
        patients[new_patient.id] = new_patient
        return new_patient
    

    @staticmethod
    def edit_patient(patient_id: int, payload: PatientCreateEdit):
        #find the patient from the DB
        pat_found = patients.get(patient_id)
        # if found update the info else raise exception
        if not pat_found:
            raise HTTPException(status_code=404, detail="patient not found")
        else:            
            pat_found.name = payload.name
            pat_found.age = payload.age
            pat_found.sex = payload.sex
            pat_found.weight = payload.weight
            pat_found.height = payload.height
            pat_found.phone = payload.phone
        
        return pat_found
        

    @staticmethod
    def delete_patient(patient_id: int):
        #find the patient from the DB
        pat_found = patients.get(patient_id)
        # if found delete record else raise exception
        if not pat_found:
            raise HTTPException(status_code=404, detail="patient not found")
        else: 
            del patients[patient_id]



    @staticmethod
    def create_appoint(patient_id: int, payload: AppointmentPayload):
        available_doctors = [doctor for doctor in doctors.values() if doctor.is_available]
        if not available_doctors:
            raise HTTPException(status_code=404, detail="No available doctors")
        
        
        #find the patient from the DB
        pat_found = patients.get(patient_id)
        # if found update the info else raise exception
        if not pat_found:
            raise HTTPException(status_code=404, detail="patient not found")
        
        doc_id = available_doctors[0].id 
        appointment = Appointment(patient=patient_id, doctor=doc_id, **payload.model_dump())        
        appointments[appointment.id] = appointment

        # Set doctor as unavailable
        available_doctors[0].is_available = False
        
        return appointment
    


patient_services = PatientsServer()