class Shop:

    globallist = []

    def __init__(self, itemName, itemRate):
        self.itemName = itemName
        self.itemRate = itemRate

    def addItem(self):
        Shop.globallist.append([self.itemName, self.itemRate])
        print("Item added successfully.")

    def removeItem(self, wannaRemove):
        index = 0
        for name, cost in Shop.globallist:
            if wannaRemove == name:
                Shop.globallist.pop(index)
            index += 1

    def displayproducts(self):
        for name, rate in Shop.globallist:
            print(f"{name} -> {rate}")

shop1 = Shop("Test", 1)
shop1.removeItem(["Test, 1"])
choice = 1
while(choice != 4):
    choice = int(input("\n\n1. Add item\n2. Remove item\n3. Display items\n4. Quit\n\nEnter your choice: "))
    if choice == 1:
        n = int(input("\nEnter the number of products: "))
        for i in range(n):
            name = input("Enter item: ")
            rate = int(input("Enter the rate: "))
            shop1 = Shop(name, rate)
            shop1.addItem()
    
    elif choice == 2:
        name = input("\nEnter item name to be removed: ")
        shop1.removeItem(name)

    elif choice == 3:
        print("\nDisplaying products: ")
        shop1.displayproducts()

    elif choice == 4:
        print("\nQuitting...")
        break

    else:
        print("\nNot a valid choice.")
