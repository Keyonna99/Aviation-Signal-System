from signal_monitor import SignalMonitor
from fallback_system import FallbackSystem
from anomaly_detection import AnomalyDetection
import time
import random

# Aviation Signal Monitoring System
# Simulates monitoring aircraft signals and activating a backup system if signal loss occurs.

def monitor_aircraft(aircraft_id):
    monitor = SignalMonitor()
    fallback = FallbackSystem()
    detector = AnomalyDetection()

    print(f"\nMonitoring Aircraft {aircraft_id}")

    # Randomly simulate signal loss
    if random.choice([True, False]):
        monitor.lose_signal()

    status = monitor.check_signal()
    print(f"Signal Status: {status}")

    if detector.detect(status):
        fallback.activate()

    print(f"Fallback Active: {fallback.status()}")


def main():

    aircraft_list = ["AA302", "DL145", "UA778"]

    print("Air Traffic Signal Monitoring System Started")

    for aircraft in aircraft_list:
        monitor_aircraft(aircraft)
        time.sleep(2)


if __name__ == "__main__":
    main()