class calulator:
    
    def Add(self, x, y):
        return x + y
    
    def Subtract(self, x, y):
        return x - y

    def Multiply(self, x, y):
        return x * y    
    
    def Divide(self, x, y):
        if y == 0:
            return "Error: Division by zero"
        return x / y
    
    

calculator = calulator()

sum = calculator.Add(10, 5)

difference = calculator.Subtract(10, 5)

product = calculator.Multiply(10, 5)

dividend = calculator.Divide(10, 5)

print(sum)
print(difference)
print(product)
print(dividend)