
class Calculator:
    @staticmethod
    def calculate(x, y):
        x = int(x)
        y = int(y)
        return {
            "hab": x + y,
            "cha": x - y,
            "gob": x * y,
            "mok": x / y
        }