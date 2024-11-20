# encapsulation means aapne koi private function ya variable banaya aur usko aap bahr object ke madad se acess nahi kar sakte
# aur aapko acess karna hai to aap class mai hi acees kar sakte ho

class Student:
    __name = "Suraj"  # __name is private variable aur __(underscore)used karke private variable banta hai

    def __init__(self):
        print(self.__name)  # aap self ki madad se acces ya print class ke andar kar sakte ho par bahr acess nahi kar sakte ...
        self.__display()
    def __display(self):
        print("Welcome")

obj = Student()

