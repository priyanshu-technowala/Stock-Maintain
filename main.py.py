# Write a program to add, remove and search for items in a stock which is maintained by a dictionary

myStock = {
            "Tata Power" : 500,
            "Trident" : 65,
            "Wipro": 550,
            "Tesla" : 100000
        }

while 0 != 1:
    choice = int(input("Enter what would you like to do: \n\n 1. To check the stock \n 2. To add something to the stock \n 3. To remove something from the stock \n 4. To search for something in the stock \n 5. Exit \n\n"))
    if choice == 1:
        print(myStock)
    elif choice == 2:
        key = input("Enter the name of the Share you would like to add: ")
        quantity = int(input("Enter the quantity of the given Share: "))
        myStock[key] = quantity
    elif choice == 3:
        removeElement = input("Enter the name of the Share you would like to delete from the stock: ")
        del myStock[removeElement]
    elif choice == 4:
        searchElement = input("Enter the name of the element you would like to search: ")
        print(myStock[searchElement])
    elif choice == 5:
        exit()
    else:
        print("Invalid option selected")
        exit()
