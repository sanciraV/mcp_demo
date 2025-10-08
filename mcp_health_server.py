from fastapi import FastAPI
from datetime import date

app = FastAPI(
    title="MCP Health Data Server",
    description="Example MCP-like API exposing dummy health data",
    version="1.0.0"
)

# Dummy Health Data
health_data = {
    "height_cm": 178,
    "weight_kg": 75,
    "blood_type": "O+",
    "allergies": ["pollen", "penicillin"],
    "diet_type": "Mediterranean",
    "alcohol_intake": "moderate",
    "caffeine_intake": "2 cups/day",
    "smoker": False,
    "is_active": True,
    "hrs_sleep": 7,
    "fitness_goals": "maintain weight, improve endurance",
    "medical_notes": "Patient shows good cardiovascular fitness.",
    "recorded_date": str(date.today())
}

# Dummy Diagnosis Data
diagnosis_data = [
    {
        "diagnosis_name": "Hypertension",
        "diagnosis_code": "I10",
        "severity": "Moderate",
        "status": "Active",
        "diagnosed_by": "Dr. Maria Stein",
        "diagnosis_date": "2024-05-10",
        "start_date": "2024-05-10",
        "end_date": None,
        "notes": "Monitoring blood pressure every 2 weeks."
    },
    {
        "diagnosis_name": "Allergic Rhinitis",
        "diagnosis_code": "J30.9",
        "severity": "Mild",
        "status": "Resolved",
        "diagnosed_by": "Dr. Hans Müller",
        "diagnosis_date": "2023-08-14",
        "start_date": "2023-08-14",
        "end_date": "2023-09-10",
        "notes": "Responded well to antihistamines."
    }
]

# Dummy Treatments Data
treatments_data = [
    {
        "treatment_type": "Medication",
        "treatment_name": "Antihypertensive therapy",
        "treatment_description": "Lowers blood pressure",
        "medication_name": "Lisinopril",
        "dosage": "10mg",
        "route": "oral",
        "start_date": "2024-05-10",
        "end_date": None,
        "frequency": "Once daily",
        "provider_name": "Dr. Maria Stein",
        "provider_specialty": "Cardiology",
        "facility_name": "Vienna Health Center",
        "status": "Ongoing",
        "outcome": "Stable blood pressure",
        "side_effects": ["mild cough"],
        "effectiveness": "Good",
        "priority": "High",
        "cost": 40.0,
        "insurance_covered": True,
        "notes": "Re-evaluate dosage in 6 months."
    },
    {
        "treatment_type": "Lifestyle",
        "treatment_name": "Exercise Program",
        "treatment_description": "Cardio and flexibility routine",
        "medication_name": None,
        "dosage": None,
        "route": None,
        "start_date": "2024-06-01",
        "end_date": None,
        "frequency": "3x/week",
        "provider_name": "Coach Lukas Reiter",
        "provider_specialty": "Fitness Trainer",
        "facility_name": "ActiveLife Gym",
        "status": "Ongoing",
        "outcome": "Improved stamina",
        "side_effects": [],
        "effectiveness": "Excellent",
        "priority": "Medium",
        "cost": 60.0,
        "insurance_covered": False,
        "notes": "Encourage more stretching."
    }
]

# Routes
@app.get("/health")
def get_health():
    return {"status": "ok", "message": "MCP Health Data Server is running"}

@app.get("/api/health")
def get_health_data():
    return health_data

@app.get("/api/diagnosis")
def get_diagnosis_data():
    return {"diagnoses": diagnosis_data}

@app.get("/api/treatments")
def get_treatments_data():
    return {"treatments": treatments_data}

@app.get("/.well-known/ai-plugin.json")
def get_manifest():
    return {
        "schema_version": "v1",
        "name_for_human": "MCP Health Server",
        "name_for_model": "mcp_health_data",
        "description_for_model": "Provides health, diagnosis, and treatment data for a user.",
        "api": {
            "type": "openapi",
            "url": "https://mcp-demo-yei4.onrender.com/openapi.json"
        },
        "auth": {
            "type": "none"
        },
        "logo_url": "https://mcp-demo-yei4.onrender.com/static/logo.png",
        "contact_email": "support@example.com",
        "legal_info_url": "https://mcp-demo-yei4.onrender.com/legal"
    }

