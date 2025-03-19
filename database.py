from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Get database URL from environment
DATABASE_URL = os.getenv('DATABASE_URL')

# Create database engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create declarative base
Base = declarative_base()

class DiagnosisRecord(Base):
    __tablename__ = "diagnosis_records"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    disease = Column(String(100))
    confidence = Column(Float)
    image_path = Column(String(255))  # Store path to saved image
    treatment_plan = Column(Text)

# Create all tables
Base.metadata.create_all(bind=engine)

def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def save_diagnosis(disease: str, confidence: float, image_path: str, treatment_plan: str):
    """Save a new diagnosis record"""
    db = SessionLocal()
    try:
        record = DiagnosisRecord(
            disease=disease,
            confidence=confidence,
            image_path=image_path,
            treatment_plan=treatment_plan
        )
        db.add(record)
        db.commit()
        db.refresh(record)
        return record
    finally:
        db.close()

def get_recent_diagnoses(limit: int = 5):
    """Get recent diagnosis records"""
    db = SessionLocal()
    try:
        return db.query(DiagnosisRecord)\
                 .order_by(DiagnosisRecord.timestamp.desc())\
                 .limit(limit)\
                 .all()
    finally:
        db.close()
