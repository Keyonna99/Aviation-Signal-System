class AnomalyDetection:
    def detect(self, signal_status):
        if signal_status == "LOST":
            print("Anomaly detected: Signal interruption.")
            return True
        return False