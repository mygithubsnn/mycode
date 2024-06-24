#!/usr/bin/env python3

proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)

# pop out an item in a list
def popfn():
    proto.pop(1)
    print("pop a http")
    print(proto)

def insertfn():
    proto.insert(5, 'dns')
    print("insert a dns")
    print(proto)

def appendfn():
    proto.append("domain")
    print("append a domain")
    print(proto)

def main():
    print(proto)


if __name__ == "__main__":
    popfn()
    insertfn()
    appendfn()
    main()

