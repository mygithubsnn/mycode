#!/usr/bin/python3
"""
Author: Steve
Let's try REST APIT
"""

import requests

def main():
    r = requests.get("https://pokeapi.co/api/v2/pokemon/")
    type(r)
    r_json = r.json()
    for count in range(3):
        print(f"print out: {r_json[count]}" )


if __name__ == "__main__":
    main()
