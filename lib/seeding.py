#the process enables semi-automation of the process
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker , relationship
from patients import Base , Patient

if __name__ == '__main__':
     engine = create_engine('sqlite:///heartmonitor.db')
     Base.metadata.create_all(engine)
     Session = sessionmaker(bind=engine)
     session = Session()

patient2 = Patient(
        firstname="nickson",
        lastname="mutheri",
        age=50,
        gender="Male",
        address="797",
        phone="687",
        email="dagy@fmail.com",
        diabetes=True,
        family_history=False,
        weight=80.0,
        height=180.0,
        hypertension=True,
        smoking=False,
        heart_failure=True
    )
session.add(patient2)
session.commit()

patient = session.query(Patient).filter_by(id=patient2.id).first()
print("Patient Details:")
print(f"ID: {patient.id}")
print(f"Name: {patient.firstname} {patient.lastname}")
print(f"Age: {patient.age}")
print(f"Gender: {patient.gender}")
print(f"Address: {patient.address}")
print(f"Phone: {patient.phone}")
print(f"Email: {patient.email}")
print(f"Diabetes: {patient.diabetes}")
print(f"Family History: {patient.family_history}")
print(f"Weight: {patient.weight}")
print(f"Height: {patient.height}")
print(f"Hypertension: {patient.hypertension}")
print(f"Smoking: {patient.smoking}")
print(f"Heart Failure: {patient.heart_failure}")
print("Risk Category:", patient.risk_category)

