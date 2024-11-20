class DemoClass:
    a=10

    def sum(self):    # jab aap class mai function bana rhe hai to aapko self name ka argument dena jaruri hai aur aap koi aur name bhi de sakte hai but self respectively accha rehta hai
        print(20+30)  # self ek object ka bhi kam karta hai...

demoobject = DemoClass() #demoobject is the object of class.. in this way object is declare 

print(demoobject.a) # call variable using object
demoobject.sum()  # call function using object