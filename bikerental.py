# mini project with help of oops concept

class BikeShop:
    def __init__(self,stock):  #self is a variable which contain memory address of current object object is 'obj' 
        self.stock=stock

    def displayBike(self):
        print("Total Bikes:",self.stock)

    def rentBike(self,q):

        if q<=0:
            print("Plz Enter Positive Or Greater Than 0 Value")
        elif q>self.stock:
            print("Enter The Value Less Than Stock:")

        else:
            self.stock=self.stock-q
            print("Total Price",q*100)
            print("Total Bike Shop",self.stock)

while True:
    obj = BikeShop(100)
    uc = int(input('''
    1 Display Stocks
    2 Rent A Bike
    3 Exit
    '''))

    if uc==1:
        obj.displayBike()
    elif uc==2:
        n = int(input("Enter How Many Bike You Want For Rent....."))
        obj.rentBike(n)
    else:
        break
