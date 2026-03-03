✈️ Aviation Signal Redundancy System

Overview

The Aviation Signal Redundancy System is a modular Python-based simulation designed to model a backup aircraft tracking mechanism in the event of primary signal loss.

The goal of this project is to simulate a fail-safe aviation monitoring system that detects signal interruptions and activates a secondary fallback broadcasting system to maintain aircraft traceability.

This concept addresses real-world aviation challenges where aircraft lose communication signals and become difficult to locate.

⸻

Problem Statement

In aviation systems, when an aircraft loses primary communication or radar signal, locating the aircraft becomes significantly more difficult.

This project simulates:
	•	Signal monitoring
	•	Anomaly detection
	•	Automatic fallback system activation

The system acts as a redundancy layer — similar to how backup generators activate during power failure.

⸻

System Architecture

The project is structured using modular design principles.

Modules

1. signal_monitor.py
	•	Tracks aircraft signal status
	•	Simulates signal loss and restoration
	•	Provides signal state to other components

2. anomaly_detection.py
	•	Detects abnormal signal behavior
	•	Triggers response when signal loss is detected

3. fallback_system.py
	•	Simulates activation of backup GPS broadcasting
	•	Represents secondary location transmission system

4. main.py
	•	Integrates all modules
	•	Controls system execution flow
	•	Simulates signal interruption event

⸻

Technologies Used
	•	Python 3
	•	Object-Oriented Programming (OOP)
	•	Modular System Design
	•	Command Line Execution

⸻

How to Run the Project
	1.	Clone the repository:
     https://github.com/Keyonna99/aviation-signal-system.git

## 👩🏽‍💻 Author
Ke’Yonna Bass  
Computer Engineering Graduate  
