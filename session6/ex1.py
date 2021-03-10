import P0.Seq0

#cada operacion en una funcion diferente!!!!!

class Seq:
    'A class for representing sequences.'
    def __init__(self, strbases):
        self.strbases = strbases
        if self.is_valid():
            print("New sequence created!")
        else:
            self.strbases = 'Error'
            print('INCORRECT Sequence detected')


    def is_valid(self): #method inside the class
        for c in self.strbases:
            if c != 'A' and c != 'C' and c != 'T' and c != 'G':
                return False
        return True

# if we use the @staticmethod we refer to the class, not the self as an argument: Seq.static_function('hello')
# Using the arg self, u call the function by naming the instance.thefunction(): sequence1.print_bases()
# So: staticmethod => class.function(v1) // self => s1.function()

# if we use an imported module we use the name of the module, if it is a method of the function we use self, if it's a static method we use the name of the class

    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)


#--- Main program
s1 = Seq("AGTACACTGGT") # by calling the class bfore the variable, python is calling the function innit;
                        # now this instance (s1) can acces all the functions in the class Sew
s2 = Seq("Am I valid???")
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")