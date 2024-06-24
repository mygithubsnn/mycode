#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
print(proto)
print(proto[1])

proto.extend("dns") # this line will add d, n, and s
print(proto)



# simiple list
#mylist = ["apple", "orange", "pear"]

#otherlist = ["cookie", "candy"]


# append opens up a SINGLE slot at the end
#mylist.append(otherlist) # creates a LIST in a LIST
#mylist.extend(otherlist) # creates as many SLOTS as ITEMS within otherlist

#print(mylist)

