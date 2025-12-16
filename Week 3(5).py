
class Patient:
    def __init__(self, patient_id, name, age, gender, contact):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact

    def is_senior(self):
        return self.age > 65


class Doctor:
    def __init__(self, doctor_id, name, specialization, contact):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.contact = contact


class Clinic:
    def __init__(self):
        self.patients = []
        self.doctors = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def list_senior_patients(self):
        print("\nSenior Patients (Age > 65):")
        for patient in self.patients:
            if patient.is_senior():
                print(f"ID: {patient.patient_id}, "
                      f"Name: {patient.name}, "
                      f"Age: {patient.age}, "
                      f"Gender: {patient.gender}, "
                      f"Contact: {patient.contact}")

    def count_ophthalmology_doctors(self):
        count = 0
        for doctor in self.doctors:
            if doctor.specialization.lower() == "ophthalmology":
                count += 1
        return count


# MAIN PROGRAM 

clinic = Clinic()

# Adding Patients
clinic.add_patient(Patient(1, "John Smith", 70, "Male", "021111111"))
clinic.add_patient(Patient(2, "Emma Brown", 45, "Female", "021222222"))
clinic.add_patient(Patient(3, "David Lee", 68, "Male", "021333333"))

# Adding Doctors
clinic.add_doctor(Doctor(101, "Dr Allen", "Ophthalmology", "022111111"))
clinic.add_doctor(Doctor(102, "Dr Green", "Cardiology", "022222222"))
clinic.add_doctor(Doctor(103, "Dr White", "Ophthalmology", "022333333"))

# Output
clinic.list_senior_patients()
print("\nTotal Ophthalmology Doctors:",
      clinic.count_ophthalmology_doctors())
