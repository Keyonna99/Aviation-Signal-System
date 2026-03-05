class SignalMonitor:
    def __init__(self):
        self.signal_status = "ACTIVE"

    def lose_signal(self):
        self.signal_status = "LOST"

    def restore_signal(self):
        self.signal_status = "ACTIVE"

    def check_signal(self):
        return self.signal_status