from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, relationship
from patients import Patient , create_user



Base = declarative_base()

class Doctor(Base):
    __tablename__ = "doci"

    id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    gender = Column(String)
    email = Column(String) 
    address = Column(String)  
    phone_number = Column(String)  
    working_hours = Column(Integer)
    salary = Column(Float, nullable=False)
    patients = relationship("Patient", backref="doctor")

    def __init__(self, firstname, lastname, age, gender, address, email, phone_number, salary, working_hours=0):
        self.firstname = firstname 
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.address = address
        self.email = email
        self.phone_number = phone_number
        self.working_hours = working_hours
        self.salary = salary 
        self.calculate_salary()

    def calculate_salary(self):
        self.salary = 2000 * self.working_hours

    def consult(self, patient):
        if patient.risk_category.startswith("HIGH RISK") or patient.risk_category.startswith("MODERATE RISK"):
            return f"Doctor {self.firstname} {self.lastname} is ready to consult with {patient.firstname} {patient.lastname}."
        else:
            return f"Patient {patient.firstname} {patient.lastname} does not need a doctor's consultation at the moment."

# Example usage:
engine = create_engine('sqlite:///heartmonitor.db')
Base.metadata.create_all(engine)
