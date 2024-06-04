# Stationery Store Manager

import os

class Sta:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

def addSta():
    name = input("Enter Stationery Name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    sta = Sta(name, quantity, price)
    with open("stadb.txt", "a") as file:
        file.write(f"{sta.name},{sta.quantity},{sta.price}\n")

def displaySta():
    with open("stadb.txt", "r") as file:
        for line in file:
            name, quantity, price = line.strip().split(",")
            print(f"Name: {name}, Quantity: {quantity}, Price: {price}")

def update_quantity():
    name = input("Enter Stationery Name: ")
    quantity = int(input("Enter new quantity: "))
    with open("stadb.txt", "r") as file:
        lines = file.readlines()
    with open("stadb.txt", "w") as file:
        for line in lines:
            stationery_name, stationery_quantity, stationery_price = line.strip().split(",")
            if stationery_name == name:
                file.write(f"{stationery_name},{quantity},{stationery_price}\n")
            else:
                file.write(line)

def main():
    while True:
        print("1. Add Stationery\n2. Display Stationery\n3. Update Quantity\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            addSta()
        elif choice == "2":
            displaySta()
        elif choice == "3":
            update_quantity()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

