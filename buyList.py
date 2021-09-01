# -*- coding: utf-8 -*-

import sys

class Input:
    file = sys.argv[1]
    operation = sys.argv[2]

class Product:
    def __init__(self, a, b,):
        self.productName = a
        self.price = b 
    
    
def main():
    myInput = Input()
    try:
        f = open(myInput.file, 'r')
    except IOError:
        input("Can't find such file. Please, press enter to exit")
        return
    
    products = []
    for line in f:
        space = line.find(' - ')
        productName = line[:space]
        price = float( line[ space + 3:-1] ) 
        products.append(Product(productName, price))

    # buy = PriceList()
    # if(myFile.operation == '1'):
    #     buy.add("Carrots - 75", f)

    # if( myFile.operation == '2'):
    #     buy.update("Onions - 50", "Onions - 30", f)


    # f = open(myFile.file, 'r')
    # for line in f:
    #     print(line)
    # f.close()

if __name__ == '__main__':
    main()