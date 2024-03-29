from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from patients import Patient

Base = declarative_base()

class FitnessExpert(Base):
    from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from patients import Patient

Base = declarative_base()

class FitnessExpert(Base):
    __tablename__ = 'fitness'

    fitness_expert_id = Column(Integer, primary_key=True)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    gender = Column(String)
    working_hours = Column(Integer)
    salary = Column(Float)
    patients = relationship(Patient, back_populates='fitness_expert') 

engine = create_engine('sqlite:///heartmonitor.db')


Base.metadata.create_all(engine)


connection = engine.connect()
def __init__(self, firstname, lastname, age, gender, address="", email="", phone_number="", working_hours=0, salary=None):
        self.firstname = firstname 
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.address = address
        self.email = email
        self.phone_number = phone_number
        self.working_hours = working_hours
        self.salary = self.calculate_salary(working_hours)

def calculate_salary(self, working_hours):
        base_salary = 1000.00  
        hourly_rate = 50.00  
        total_salary = base_salary + (working_hours * hourly_rate)
        return total_salary

def consult(self, patient):
        if hasattr(patient, 'risk_category') and patient.risk_category.startswith("MODERATE RISK"):
            return f"Fitness expert {self.firstname} {self.lastname} is ready to consult with {patient.firstname} {patient.lastname}."
        else:
            return f"Patient {patient.firstname} {patient.lastname} does not need a fitness consultation at the moment."

# Example usage:
engine = create_engine('sqlite:///heartmonitor.db')
Base.metadata.create_all(engine)