#list(): list() is a mutable data.. mutable means aap list ko change,delete,add kar sakte ho isliye
#list ek mutable data hai...

l = [1,2,3,4,5,"Suraj"]

print(l[2])

print(l[0:6])#slice start to end with slicing

print(l[0::2])#slice start end and increment three arguments...

print(l[-5])#reverse se data layega aur reverse ka index number start with -1

print(l[-1::-1])


#nested list()

#index no:  0,1,2,   3    -> pura nested list ko ek hi index number hoga jaisa is example mai hai...
       l = [1,2,3,[4,5,6]]

print(l)

print(l[3]) #agar aapko sirf nested list ka data chayie to aese print hoga aur uska index value 3 hoga kiyuki vo pura nested list ko ek hi index number mai cover kar leta hai...

print(l[3][0]) #agar aapko nested list mai se koi data chayie to aese print hoga... aur nested list ka index number '0' se start hoga...



