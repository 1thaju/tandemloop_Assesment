class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation

    def calculate(self):
        if self.operation == "Addition":
            return self.a + self.b
        elif self.operation == "Subtraction":
            return self.a - self.b
        elif self.operation == "Multiplication":
            return self.a * self.b
        elif self.operation == "Division":
            if self.b == 0:
                return "Error: Division by zero!"
            return self.a / self.b
        else:
            return "Error: Invalid operation!"

if __name__ == "__main__":
    # Example Usage
    calc1 = Calculator(10.0, 5.0, "Addition")
    print(f"10.0 + 5.0 = {calc1.calculate()}")

    calc2 = Calculator(10.0, 5.0, "Subtraction")
    print(f"10.0 - 5.0 = {calc2.calculate()}")

    calc3 = Calculator(10.0, 5.0, "Multiplication")
    print(f"10.0 * 5.0 = {calc3.calculate()}")

    calc4 = Calculator(10.0, 5.0, "Division")
    print(f"10.0 / 5.0 = {calc4.calculate()}")

    calc5 = Calculator(10.0, 0.0, "Division")
    print(f"10.0 / 0.0 = {calc5.calculate()}")

    calc6 = Calculator(10.0, 5.0, "Exponentiation")
    print(f"Invalid operation example: {calc6.calculate()}") 