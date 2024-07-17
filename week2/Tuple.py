tuple = 23,44,56,78,53,46
# Traverse in forward directiomn using negative indexing
print("Traversal of tuple in forward order using negative indexing:")
for i in range(-len(tuple),0):
    print(tuple[i], end = ",")
print("\n---------------------------------------------------------------")
# backword using forward indexing
print("Traversal of tuple in backward direction using forward indexing: ")   
for i in range(len(tuple)-1,-1,-1):
    print(tuple[i], end = ",")
print("\n---------------------------------------------------------------")
# sum of all the elements
print("The elements are: ")
print(tuple)
print("The sum of all the elements in the tuple{} is {}".format(tuple,sum(tuple)))

# Tuple as immutable datatype with mutable elements
print("---------------------------------------------------------------")
immutable_tuple = ([1, 2, 3], {'a': 1, 'b': 2})

print("Original tuple:", immutable_tuple)
immutable_tuple[0].append(4)
immutable_tuple[1]['c'] = 3

print("Modified tuple:", immutable_tuple)