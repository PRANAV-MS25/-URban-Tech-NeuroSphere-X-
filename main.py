from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random

app = FastAPI()

# ==============================
# CORS
# ==============================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==============================
# DATABASE
# ==============================

events_db = [

    {
        "id": 1,
        "type": "Traffic Congestion",
        "severity": "High",
    },

    {
        "id": 2,
        "type": "Crowd Density High",
        "severity": "Medium",
    },

    {
        "id": 3,
        "type": "AI Risk Alert",
        "severity": "Critical",
    },

]

# ==============================
# MODEL
# ==============================

class Event(BaseModel):
    type: str
    severity: str

# ==============================
# ROOT
# ==============================

@app.get("/")
def home():

    return {
        "message": "NeuroSphere AI Backend Running"
    }

# ==============================
# GET EVENTS
# ==============================

@app.get("/events")
def get_events():

    enhanced_events = []

    for event in events_db:

        threat_score = random.randint(40, 100)

        if threat_score > 80:
            response_unit = "Ambulance + Police"

        elif threat_score > 60:
            response_unit = "Police Unit"

        else:
            response_unit = "Drone Surveillance"

        enhanced_event = {

            **event,

            "threat_score": threat_score,

            "response_unit": response_unit,

            "telemetry": {

                "cpu_usage": random.randint(40, 95),

                "network_strength": random.randint(50, 100),

                "ai_confidence": random.randint(70, 99),

            }

        }

        enhanced_events.append(enhanced_event)

    return enhanced_events

# ==============================
# CREATE EVENT
# ==============================

@app.post("/events")
def create_event(event: Event):

    new_event = {

        "id": len(events_db) + 1,

        "type": event.type,

        "severity": event.severity,

    }

    events_db.append(new_event)

    return {

        "message": "Event created successfully",

        "event": new_event,

    }