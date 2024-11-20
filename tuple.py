# tuple is immutable data it can't change or update or delete
# tuple function are min(), max(), count(), index(), sum()

t = (20,30,40,50)

print(t)


# min()

min = min(t)

print("The Minimum Value Of tuple is :" + str(min))

# max()

max = max(t)


print("The Maximum Value Of tuple is :" + str(max))

# count() finds repeat value in tuple

c = t.count(20)

print("The Repeat Value In tuple " + str(c))

# index() return index number of particular variable

i = t.index(50)

print(i)

# sum() addition of integer value and does not work on string value....

s = sum(t)

print(s)
