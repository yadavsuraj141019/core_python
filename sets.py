# sets : sets are unorder data type or unindex... set works on delete data but can't changed.. you can 
# insert data but can't changed or update data

# note: sets stores unique value and doest not work on repeted value like 2 bar 10 aur 20 etc..

# agar aapne 10 ko 2 bar likha hai sets mai to sets 1 bar hi print hoga koi bhi value agar aapne 
# repeat kiya to ek bar hi print hoga like neche vale example dekh lo

s = {10,20,30,10,10}

print(s)


# sets function are set(), add(), pop(), remove(), clear() and discard() and update()

# set() means agar aapka pas koi list hai ya tuple to usko set mai convert karna hai to aap set() ka use kar sakte ho....

l = [10,20,30]

s1 = set(l)

print(s1)

# add() used to add element in sets

s2 = {10,20,30,40}

s2.add(50)

print(s2)

# pop() used to delete element in sets but randomly from the element koi bhi kar dega delete

s2.pop()

print(s2)

# remove() and discard() used to delete element in sets but it is used on value jo value likoge vo delete ho jayega 

s2.remove(50)  

print(s2)

# clear() used to clear all sets element 

s2.clear()

print(s2)


# update() 
