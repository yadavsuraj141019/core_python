class A:
    def displayA(self):
        print("Suraj A")

class B(A):
    def displayB(self):
        print("Suraj B")


objb = B()
objb.displayA()
objb.displayB()

# in heritance menas aapne 2 class banaya jaise is example mai hai A And B class agar aap A Class ke sare
# function or behaviour class B Mai lena chhate hai to aapko inherit karna padega
# Note: inherit ke bad Aap B class ka object banake A class Ka Function And behaviour acess kar sakte hai...