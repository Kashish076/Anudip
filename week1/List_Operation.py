# appending a list at specified position
ab  = [1,2,3,4,5,6]
b = [11,22,33,44]
ab = ab[:3] + b +ab[3:]
print(ab,"\n")

# without using slicing
for i in range(len(b)):
    ab.insert(3+i,b[i])
print(ab)

# removing elements usnig remove function
ab.remove(3) 
# 3 is the position here
print(ab,"\n")

# popping of element from the list
ab.pop(2)
# 2 is the index here
ab.pop()
# pop without any index remove the last element of the list
print(ab,"\n")

# using delete deletes element within a range
del ab[4:8:2]

# Sorting of list in ascending order
ab.sort()
print(ab)
# Sorting of list in descending order
ab.sort(reverse=True)
print(ab)

# using clear 
ab.clear()
print(ab)