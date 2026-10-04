# 📡 URban-Tech-NeuroSphere-X | 

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Uvicorn-0.22+-499848?style=for-the-badge&logo=uvicorn&logoColor=white" alt="Uvicorn" />
  <img src="https://img.shields.io/badge/WebSockets-Live-010101?style=for-the-badge&logo=socketdotio&logoColor=white" alt="WebSockets" />
  <img src="https://img.shields.io/badge/OpenSky%20Network-Live%20Telemetry-00599C?style=for-the-badge" alt="OpenSky" />
  <img src="https://img.shields.io/badge/License-All%20Rights%20Reserved-red?style=for-the-badge" alt="License" />
</p>

---

## 🚁 Overview

**URban-Tech-NeuroSphere-X** is an intelligent, real-time tactical airspace monitoring system centered around **Kempegowda International Airport (VOBL Ground Radar, Bengaluru)**.

The system retrieves live ADS-B telemetry from the **OpenSky Network**, processes aircraft geographical coordinates into tactical polar vectors such as **range and bearing**, and streams real-time aircraft data through a **WebSockets pipeline** to an interactive HTML5 tactical radar interface.

The platform also integrates a **Deterministic & LLM Tactical Threat Engine** that evaluates aircraft conditions using emergency squawk codes, altitude changes, and velocity thresholds to categorize potential threats into:

- 🟢 `GREEN`
- 🟡 `YELLOW`
- 🔴 `RED`

The resulting tactical information is presented through a live radar interface containing aircraft blips, callsigns, altitude information, telemetry data, and alert indicators.

---

## 📁 Project Structure

```text
URban-Tech-NeuroSphere-X/
├── backend/
│   └── main.py
├── requirements.txt
├── README.md
│
├── Primary  Route.png
├── Safe Route.png
├── radar and Diagnostics.png
└── overview.png
