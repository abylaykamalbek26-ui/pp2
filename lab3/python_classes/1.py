class manipulationstring:
    def __init__(self):
        self.string = ""
    def get_string(self):
        self.string=input("Enter a string:")
    def print_string(self):
        print(self.string.upper())

a = manipulationstring()
a.get_string()  
a.print_string() 