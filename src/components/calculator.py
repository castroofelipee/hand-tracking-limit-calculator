class Calculator:
    def __init__(self):
        self.value = 0

    def update_value(self, gesture):
        if gesture == "CLOSE":
            self.value -= 1
        elif gesture == "OPEN":
            self.value += 1

    def calculate_limit(self):
        return f"The limit as x approaches infinity is: {self.value}"
