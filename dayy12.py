class CustomException(Exception):
    """Custom Exception for specific error handling."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class Calculator:
    def __init__(self):
        pass

    def divide(self, numerator, denominator):
        try:
            if denominator == 0:
                raise CustomException("Denominator cannot be zero.")
            return numerator / denominator
        except CustomException as ce:
            print(f"Custom Exception Caught: {ce}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Usage
calc = Calculator()
result = calc.divide(10, 0)  # This will raise a CustomException
print(result)  # Output: None


