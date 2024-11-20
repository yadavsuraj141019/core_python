# polymorphism means same function name (but different signatures)...
# agar jaise python mai len() hai iska kam hai length find karna chahe list ka ya string ka dono ka find karega..
# vaise hi function name same hai like len() but kam alag alag hai .... neeche vala example dekho pata chal jayega

l = [10,20,30,40]

print(len(l))

s = "Suraj"

print(len(s))


# polymorphism has two functions overloading() and overidding()
# below examples....
# overloading() means function name are same but output is different according to parameter...like below examples 

class Ws:
    def displayinfo(self,name=''):
        print("Welcome Suraj" +name)


obj = Ws() 
obj.displayinfo('Digiteon')

# overriding() examples below......

class Suraj:
    def display(self):
        print("Suraj Yadav")


class Yadav(Suraj):
    def display(self):
        super().display()  # super() se app parent ke function ko access kar sakte hai...
        print("Suraj Yadav Kumar")

yad = Yadav()
yad.display() 


# overriding() function ka matlab function ko override kar dega jaise upar vala example mai 2 class banaye like suraj and yadav
# class banaye aur yadav vale class mai apne ne suraj vale class ko inherit kar diya to inherit ka matlab ye huva 
# ki yadav class ke object se apne suraj class ke sare function and behaviour access kar sakte hai but 
# is upar vale example mai dono class mai same name ka function hai to vo parent class matlab suraj vale class
# ke function access nahi karega aur override karke sirf yadav class ka function display karega

# note: agar apne ko parent ya suraj vala class ke function ko acess karna hai to 'super()' ke madad se
# agar same function name hai child aur parent mai to parent ke function acess kar sakte hai super() ki madad se