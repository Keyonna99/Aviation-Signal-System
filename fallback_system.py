class FallbackSystem:
    def __init__(self):
        self.fallback_active = False

    def activate(self):
        self.fallback_active = True
        print("Fallback GPS broadcasting activated.")

    def deactivate(self):
        self.fallback_active = False
        print("Fallback deactivated.")

    def status(self):
        return self.fallback_active