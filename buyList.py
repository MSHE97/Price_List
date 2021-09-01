# -*- coding: utf-8 -*-

import sys

class IOFile:
    file = sys.argv[1]
    operation = sys.argv[2]

class PriceList:
    def PriceList():
        products = []
    def PriceList(self, list):
        products = list
       


def main():
    myFile = IOFile()
    try:
        f = open(myFile.file)
    except IOError:
        input("Can't find such file. Please, press enter to exit")
        return
    for line in f:
        print(line)
    f.close()

if __name__ == '__main__':
    main()