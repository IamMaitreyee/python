class Calculator:
    def add(self, a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def multi(self,a,b):
        return a*b
    def div(self,a,b):
        if b==0:
            return "Error! Division by zero."
        return a/b
if __name__ == "__main__":
   calc=Calculator()
   print("Addition: 5 + 3 = ",calc.add(5,3))
   print("Subtraction: 5 - 3 = ", calc.sub(5, 3))
   print("Multiplication: 5 * 3 = ", calc.multi(5, 3))
   print("Division: 5 / 3 = ", calc.div(5, 3))