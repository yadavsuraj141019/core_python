class DemoSuraj:
    a=10
    
    def __init__(self): # python mai constructor aese define hota hai.... aur automatic call hota hai jaise object create hota hai vaise....
        print("YADAV SURAJ")

    def showvalue(self):
        print(self.a)

    def showvalue1(self,a,b):
        print(a+b)

obj = DemoSuraj()
obj.showvalue()
obj.showvalue1(10,10)