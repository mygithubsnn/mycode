#!/usr/bin/python3

def main():
    creds = {"admin":"scaleio", "root":"rootcre", "qatest1":"dell1234"}
    for x,y in creds.items():
        print(x)
        print(x[2])

        print("y value")
        print(y)






if __name__ == "__main__":
    main()

