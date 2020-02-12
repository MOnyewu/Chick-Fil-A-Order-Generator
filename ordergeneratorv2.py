#https://www.chick-fil-a.com/
import urllib
from urllib import request
import random

keyword = "<span aria-hidden"

def main():
    link = input("Please enter a url: ")
    data = get_url(link).read()
    html = data.decode("UTF-8")
    with open("chickfila.txt","w") as f:
        print(html, file=f)
    food_menu = get_food_menu("chickfila.txt")
    drink_menu = get_drink_menu("chickfila.txt")
    food_prices = food_price("chickfila.txt")
    drink_prices = drink_price("chickfila.txt")
    food_cost = literal_food_price("chickfila.txt")
    drink_cost = literal_drink_price("chickfila.txt") 
    order = eval(input("How many items do you want, excluding the drink? "))
    drink_order = eval(input("How many drinks do you want? "))
    totalcost = 0
    for i in range(order):
        rand = random.randint(0,len(food_menu)-1)
        print("Food item number ", i+1)
        print(food_menu[rand], food_prices[rand])
        totalcost += float(food_cost[rand])
    for i in range(drink_order):
        rand = random.randint(0,len(drink_menu)-1)
        print("Drink number ", i+1)
        print(drink_menu[rand], drink_prices[rand])
        totalcost += float(drink_cost[rand])
    print("Your total cost should be $%.2f"%(totalcost))
    

def get_food_menu(file):
    list = []
    with open(file) as myFile:
        for num, line in enumerate(myFile, 1):
            if keyword in line:
                if (line.find("<sup>") != -1):
                    start = line.find('>')
                    next = line.find('<sup>')
                    first = line[start+1:next]
                    start = line.find('</sup>') + 6
                    end = line.find('</span>')
                    second = line[start:end]
                    new = first + second
                    list.append(new)
                else:        
                    elem = line.find('>')
                    end_elem = line.find('</')
                    new_elem = line[elem+1:end_elem]
                    list.append(new_elem)
    return list[:-23]
def get_drink_menu(file):
    list = []
    with open(file) as myFile:
        for num, line in enumerate(myFile, 1):
            if keyword in line:
                if (line.find("<sup>") != -1):
                    start = line.find('>')
                    next = line.find('<sup>')
                    first = line[start+1:next]
                    start = line.find('</sup>') + 6
                    end = line.find('</span>')
                    second = line[start:end]
                    new = first + second
                    list.append(new)
                else:        
                    elem = line.find('>')
                    end_elem = line.find('</')
                    new_elem = line[elem+1:end_elem]
                    list.append(new_elem)
    return list[-23:]
def food_price(file):
    list = []
    with open(file) as myFile:
        for num, line in enumerate(myFile, 1):
            if '$' in line:
                end_elem = line.find(' ')
                item = line[0:end_elem + 1]
                list.append(item)
    return list[:-23]
def drink_price(file):
    list = []
    with open(file) as myFile:
        for num, line in enumerate(myFile, 1):
            if '$' in line:
                end_elem = line.find(' ')
                item = line[0:end_elem + 1]
                list.append(item)
    return list[-23:]
def get_url(url):
    resp = request.urlopen(url)
    return resp

def literal_food_price(file):
    list = []
    with open(file) as myFile:
        for num, line in enumerate(myFile, 1):
            if '$' in line:
                end_elem = line.find(' ')
                item = line[1:end_elem]
                list.append(item)
    return list[:-23]
def literal_drink_price(file):
    list = []
    with open(file) as myFile:
        for num, line in enumerate(myFile, 1):
            if '$' in line:
                end_elem = line.find(' ')
                item = line[1:end_elem]
                list.append(item)
    return list[-23:]
main()