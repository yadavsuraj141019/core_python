import random

# random.randint(2,8): means iska matlab ye agar aapne random.randint(2,8) aapne argument mai 2 aur 8 pas kiya 
# to ye random.randint methods se aapko 2 se 8 ke bech mai se koi bhi random value de dega ya phir 2 aur 8 bhi de dega
# par 2 aur 8 ke bech mai ka hi dega...


n = random.randint(2,8)
print(n)


# random.randrange(3,9): means iska matlab ye huva ki aapko 3 se leke 8 tak ka koi bhi random value de dega
# par 9 nahi dega 
# note random.range() argument mai jo bhi second value diya jayega uska output nahi dega jaise is example mai hai....

n1 = random.randrange(3,9)
print(n1)

# random.choice() means neche vala list mai se koi bhi choice karke output dega par randomly 

l = [10,20,30,40]
n2 = random.choice(l)
print(n2)


# random() means ye function aapko 0 se 1 ke beech ka koi bhi float value return kar dega

r = random.random()

print(r)

# shuffle() means ye function mai aapne ek list banya us list mai 4 value like [1,2,3,4] to shuffle ke madad se
# list ke sequence order change ho jayega like 1 ki jagh 3 , 3 ki jagah 4 aesa...see below example.... 

l = [1,2,3,4]

random.shuffle(l)

print(l)

# uniform(): random.uniform(2,6) iska matlab aapne aesa value pass kiya parameter to 2 se leke 6 ke beech tak
# jitna bhi float value hai vo aayega randomly.....

u = random.uniform(2,6)

print(u)