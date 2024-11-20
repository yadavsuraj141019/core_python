d = {
     'name':'suraj',
     'salary': 8000,
     'title':'yadav'
}

n = d.get('name') # get() mai jaise koi bhi 'key' pass karoge uska value de dega jaise is mai hai vaise 

print(n)


for a in d.keys(): # keys() is function se aap sare 'keys' to access kar sakte ho aur print kar sakte ho
    print(a)  


for b in d.values(): # values() is function se aap sare 'values' to access kar sakte ho aur print kar sakte ho
    print(b)

for c,d in d.items(): #  items() is function se aap sare 'keys' aur 'values' to access kar sakte ho aur print kar sakte ho
    print(c,d)


# Delete dictionary are as below

# del() and pop() with help of these two you deleted dictionary....

# note: 'key' ke help se hi delete hoga...


d = {
    1:'suraj',
    2:'yadav',
    3:'czcdcsd',
    4:'asdsad'
}

del d[3]

print(d)

d.pop(4)

print(d)


# update(): is used to update the value of dictionary

d.update({2:'kumar'})

print(d)

# clear() is used to clear all dictionary data....

d.clear()
print(d)

# insert new data in dictionary....

d['desc']="Name Is Brand"

print(d)
