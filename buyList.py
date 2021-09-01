# -*- coding: utf-8 -*-

import sys
# Класс для считывания аргументов выполнения команды
class Input:
    file = sys.argv[1]
    operation = sys.argv[2]

# Класс Product описывает продукт из списка 
class Product:
    def __init__(self, a, b,):
        self.productName = a
        self.price = b 

# Класс ProductList для всего списка продуктов. Операций со списком реализованы методами сего класса
class ProductList:
    err = 0
    products = []

    def perform(self, operation):
        if operation == '':
            self.err = -1
            return

        if operation == "sum":
            sum = 0
            for i in self.products:
                sum += i.price
            return sum

        space = operation.find(' ')
        opName = operation[:space]

        separator = operation.find(' - ')
        
        productName = operation[space + 1:separator]
        price = operation[separator + 3:]

        if opName == 'add':
            self.products.append( Product(productName, price) )
            return 'done'
        
        if opName == 'upd':
            for i in self.products:
                if i.productName == productName:
                    i.price = price
            return 'done'
        
        if opName == 'del':
            for i in range( len(self.products) ):
                print(self.products[i].productName, productName)
                if ( productName in self.products[i].productName):              
                    self.products.remove(self.products[i])
                    return 'done'
        else:
            self.err = -2
            print(opName, productName, price)
            return 'smt gone wrong :('
    
def main():
    myInput = Input() 
    try:
        f = open(myInput.file, 'r')
    except IOError:
        input("Can't find such file. Please, press enter to exit")
        return
    
    a = ProductList() # создается экземпляр класса с пустым списком продуктов
    # В цикле файл парсится в объекты 'продукт - стоимость', дочерние для объекта Список продуктов
    for line in f:
        space = line.find(' - ')
        productName = line[:space]
        price = int( line[ space + 3:] ) 
        a.products.append(Product(productName, price))
        
    # выполнение операции с stdout ответом
    print( a.perform( myInput.operation ) )
    # перезапись файла с учётом выполненной операции
    f = open(myInput.file, 'w')
    for i in a.products:
        f.write(i.productName + ' - ' + str(i.price) + "\n")
    f.close()

if __name__ == '__main__':
    main()