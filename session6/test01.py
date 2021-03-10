class Seq:
    'A class is the template we use for creating objects.' #Inside the class we define all the methods of the objects of that class, and we program their behaviour'
    def __init__(self, strbases): #The initialization method is called every time a new object is created.
        self.strbases = strbases #For representing a sequence we will use a string that is store in every object: strbases.
        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self): #As it is a method, the first parameter must be self.
        """Calculate the length of the sequence"""
        return len(self.strbases)


# Main program

# Create objects of the Class Seq:
s1 = Seq('AGTACACTGGT')
s2 = Seq('CGTAAC')

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"  Length: {s1.len()}") #"Execute the action for calculating the length on the s1 object"
print(f"Sequence 2: {s2}")
print(f"  Length: {s2.len()}")

print('________________________________________________________________________')

class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inherite
       the methods from the Seq class
    """
    def __init__(self, strbases, name=""): # we add functions, to print the gene name
        # -- Call first the Seq initilizer and then the gene init method
        super().__init__(strbases)
        self.name = name
        print("New gene created")

    def __str__(self): # we are overriding (changing) a function alrdy created
        """Print the Gene name along with the sequence"""
        return self.name + "-" + self.strbases

# --- Main program
s1 = Seq("AGTACACTGGT")
g = Gene("CGTAAC", "FRAT1")

# -- Printing the objects
print(f"Sequence 1: {s1}") #la f se pone para tranformar la funcin de dentro en str
print(f"Gene: {g}")