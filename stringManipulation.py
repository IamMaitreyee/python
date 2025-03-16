class StringManipulator:
    def __init__(self):
        self.text=" "
    def get_string(self):
        self.text=input("Enter the string: ")
    def print_string(self):
        print(self.text.upper())
    def reverse_lower(self):
        reversed_text = ' '.join(self.text.split()[::-1])
        print(reversed_text.lower())
obj=StringManipulator()
obj.get_string()
obj.print_string()
obj.reverse_lower()
