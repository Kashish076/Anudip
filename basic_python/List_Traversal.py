frstlst = [1,2,3,56,"xys","yuo"]

# Forward traversal of list
for i in range(0,len(frstlst)):
    print(frstlst[i])
print("<------------------------------------------------------------------>")
# forward traversal using negative indexing
for i in range(-len(frstlst),-1):
    print(frstlst[i])
print("<------------------------------------------------------------------>")

# Reverse of a list using forward indexing
for i in range(len(frstlst)-1,-1,-1):
    print(frstlst[i])
print("<------------------------------------------------------------------>")
for i in range(len(frstlst)):
    print(frstlst[len(frstlst)-i-1])
