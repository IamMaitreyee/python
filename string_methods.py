class StringManipulator:
    def __init__(self):
        self.text=" "
    def get_string(self):
        self.text=input("Enter the string: ")
    def print_string(self):
        print(self.text.upper())
obj=StringManipulator()
obj.get_string()
obj.print_string()
