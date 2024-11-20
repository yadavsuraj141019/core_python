# encapsulation are two function getter() and setter() method
# Note: agar aapko kisi private variable mai value set karna hai to setter() method used hoga
# aur jo value set kiya usko get karna hai to getter() method used hoga

class Student:
    def __init__(self):
        self.__name=""

    def getname(self):
        return self.__name

    def setname(self,name):
        self.__name = name


obj = Student()
obj.setname("Yadav Suraj")
name = obj.getname()
print(name)