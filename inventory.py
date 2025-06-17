import json
import os

def validatenum(label):
    while True:
        try:
            num = int(input(f"Enter the {label} of the product: "))
            return num
        except ValueError:
            print("Please enter a number")

def newitem():
    name = input("Enter the Item's name: ").lower()
    barcode = validatenum("barcode number")
    quantity = validatenum("quantity")
    while True:
        try:
            price = float(input("Enter the price of the Product in local currency: "))
            break
        except ValueError:
            print("Please enter a valid price")
    item = {"name": name, "barcode": barcode, "quantity": quantity, "price": price}
    stock.append(item)
    if exist:
        with open("stock.json", "r") as file:
            temp = json.load(file)
        temp.extend(stock)
        with open("stock.json", "w") as file:
            json.dump(temp, file)
    else:
        with open("stock.json", "w") as file:
            json.dump(stock, file)

def view_inventory():
    if not exist:
        print("There are no records of any item. Please add items first.")
        return

    option = ""
    while option not in ["1", "2"]:
        option = input("Press 1 to search by name\nPress 2 to search by barcode number\nYour Option: ")
        if option not in ["1", "2"]:
            print("Please enter a valid option")

    with open("stock.json", "r") as file:
        data = json.load(file)

    if option == "1":
        name = input("Enter the name of an item: ").lower()
        found = False
        for item in data:
            if item["name"] == name:
                print(f"The inventory left for item {name} is {item['quantity']}")
                found = True
                break
        if not found:
            print("Item not found in the inventory.")

    elif option == "2":
        try:
            barcode = int(input("Enter the barcode number of an item: "))
        except ValueError:
            print("Invalid barcode number.")
            return
        found = False
        for item in data:
            if item["barcode"] == barcode:
                print(f"The inventory left for item with barcode {barcode} is {item['quantity']}")
                found = True
                break
        if not found:
            print("Item not found in the inventory.")

def add_or_remove(operator):
    if not exist:
        print("There are no records of any item. Please add items first.")
        return

    option = ""
    while option not in ["1", "2"]:
        option = input("Press 1 to search by name\nPress 2 to search by barcode number\nYour Option: ")
        if option not in ["1", "2"]:
            print("Please enter a valid option")

    with open("stock.json", "r") as file:
        data = json.load(file)

    if option == "1":
        name = input("Enter the name of the item: ").lower()
        for item in data:
            if item["name"] == name:
                amount = validatenum("amount")
                if operator == "+":
                    item["quantity"] += amount
                else:
                    item["quantity"] -= amount
                with open("stock.json", "w") as file:
                    json.dump(data, file)
                print("Stock updated.")
                return
        print("Item not found.")
    else:
        barcode = validatenum("barcode number")
        for item in data:
            if item["barcode"] == barcode:
                amount = validatenum("amount")
                if operator == "+":
                    item["quantity"] += amount
                else:
                    item["quantity"] -= amount
                with open("stock.json", "w") as file:
                    json.dump(data, file)
                print("Stock updated.")
                return
        print("Item not found.")

# Main Program
stock = []
exist = os.path.exists("stock.json")
string = None

while string != 0:
    try:
        string = int(input("\nPress 1 to enter a new item\nPress 2 to add stock\nPress 3 to subtract stock\nPress 4 to view stock report\nPress 0 to exit\nYour Option: "))
        if string == 1:
            newitem()
        elif string == 2:
            add_or_remove("+")
        elif string == 3:
            add_or_remove("-")
        elif string == 4:
            view_inventory()
        elif string == 0:
            print("Thanks for using the inventory system.")
        else:
            print("Invalid option. Please choose between 0 and 4.")
    except ValueError:
        print("Please enter a valid number.")