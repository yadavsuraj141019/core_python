# chr() and ord() two functions of string...

# chr(): chr() means ye aapse integer value lega apna parameter mai aur return karega aapko character or string..
# neeche vala example dekho samjh aa jayega...


a = 66

print(chr(a))



# ord(): ord() means aaapko pass karna hai character aur return karega aapko integer value neeche vala example dekho samjh aa jayega..

a = ord('A')

print(a)


# format(): format() means aap koi bhi string mai koi bhi string ya integer value insert kar sakte hai {} curlybrackets ke sath..
# with the help of format()


txt1 = "Welcome {name} {lname}".format(name="Suraj",lname="Yadav")

print(txt1)

txt2 = "Welcome {0} {1} {2}".format("Suraj","Yadav",14) # 0 and 1 ka matlab index value like array jaisa...

print(txt2)

txt3 = "Welcome {} {}".format("Suraj","Yadav") # agar aap curly bracket blank rakh doge to bhi vo as a index value data de dega like array..
print(txt3)

txt4 = "Welcome {a:>10} {b}".format(a=20,b=30)
print(txt4)

#a:10: iska matlab ye huva left se right space dega phir aayega 'a' ka value...
#output: welcome        20 30 aesa output aayega a:10 ka...


#a:^10: iska matlab ye aapko 'a' ka value se pehle thoda space phir 'a' ka value ke bad thoda space dega
#output:welcome    20    30 aesa output dega a:^10 ka...


#a:<10: iska matlab 'a' ka value ke bad space dega...
#output:welcome 20        30 aesa output dega a:<10 ka...

#a:>10: iska matlab 'a' ka value se pehle space dega...
#output:welcome          20 30 aesa output dega a:>10

#format() help se aap ek string ko acche se formating kar sakte hai.....