class Interest:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    def simple_interest(self):
        si = (self.principal * self.rate * self.time) / 100
        return si

    def compound_interest(self):
        amount = self.principal * pow((1 + (self.rate / 100)), self.time)
        return amount-self.principal