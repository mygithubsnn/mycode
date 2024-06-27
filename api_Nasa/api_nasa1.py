#!/usr/bin/python3
"""
AUthor: Steve M

Nasa API qury
"""
import urllib.request
import pprint

def nasa_fn():
    nasaurl = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"
    apodurlobj = urllib.request.urlopen(nasaurl)
    dir(apodurlobj)
    apodurlobj.code
    apodurlobj.msg
    apodurlobj.length
    apod = apodurlobj.read().decode("utf-8")

    pprint.pprint(apod)

    print("")

def main():
    nasa_fn()


if __name__ == "__main__":
    main()





