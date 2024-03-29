from sqlalchemy import create_engine, Column, Integer, String, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from cli import create_user


Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'
    id = Column("id", Integer, primary_key=True)
    firstname = Column("firstname",String)
    lastname = Column("lastname",String)
    age = Column("age",Integer)
    gender = Column("gender",String)
    address = Column("address",String)
    email = Column("email",String)
    phone = Column("phone",String)
    diabetes = Column("diabetes",Boolean)
    family_history = Column("family_history",Boolean)
    hypertension = Column("hypertension",Boolean)
    weight = Column("weight",Float)
    height = Column("height",Float)
    smoking = Column("smoking",Boolean)
    heart_failure = Column("heart_failure",Boolean)
    risk_score = Column("risk_score",Integer)
    risk_category = Column("risk_category",String)
    #doctor_id = Column(Integer, ForeignKey("doci.id"))
    #fitness_expert_id = Column(Integer, ForeignKey('fitness.id'))
   # doctor = relationship("Doctor", back_populates="patients")
    #fitness_expert = relationship("FitnessExpert", back_populates="patients")

    def __init__(self, firstname, lastname, age, gender, address="", phone="", email="",
                 diabetes=False, hypertension=False, smoking=False, weight=0.0, height=0.0,
                 family_history=False, heart_failure=False):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.address = address
        self.phone = phone
        self.email = email
        self.diabetes = diabetes
        self.hypertension = hypertension
        self.smoking = smoking
        self.weight = weight
        self.height = height
        self.heart_failure = heart_failure
        self.family_history = family_history
        self.calculate_risk_score()
        self.get_risk_category()

    def calculate_risk_score(self):
        self.risk_score = int(self.age >= 65) + int(self.diabetes) + int(self.hypertension) + int(self.smoking)
        if self.weight:
            bmi = self.weight / ((self.height / 100) ** 2)  # Calculate BMI
            if bmi < 18.5 or bmi >= 25:
                self.risk_score += 1
        self.risk_score += int(self.family_history) + int(self.heart_failure)

    def get_risk_category(self):
        if self.risk_score >= 4:
            self.risk_category = "HIGH RISK: Please consult a doctor for further evaluation and management."
        elif self.risk_score >= 2:
            self.risk_category = "MODERATE RISK: Consider lifestyle modifications and consult a doctor for advice."
        else:
            self.risk_category = "LOW RISK: Maintain healthy habits and schedule regular checkups."

