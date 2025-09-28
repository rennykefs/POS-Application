#create dictionary for storage

inventory={} #inventory dictionary
till_balance=0 #store cash in hand

#function for create items
def create_item(name, quantity, price):
    if name in inventory:
        print(f'item {name} already exists')
    else:
        inventory[name]={"quantity":quantity,"price":price}

#Function for contact addition
def add_item():
    name= input("Enter item name: ")
    quantity= input(int("Enter item quantity: "))
    price= input(float("Enter item price: "))
    create_item(name,quantity,price)# recalling the creating function

#Function for finding item
def find_item (name):
    if name in inventory:
        print(f"Item found: Item: {name}, Quantity: {inventory[name]["quantity"]}, Price: {inventory[name]["price"]}")
    else:
        print(f'Item: {name} is not found')

#Updating item in inventory
def update_item(name,quantity):
    if name in inventory:
        inventory[name]["quantity"]+=quantity
        print(f"Item {name} updated successfully. New quantity: {inventory[name]["quantity"]}")

    else:
        print(f"Item {name} not found.")

#deleting item in inventory
def delete_item(name):
    if name in inventory:
        del inventory[name]
        print(f"Item {name} deleted successfully")
    else:
        print(f"Item {name} not found")

#Return total stock
def total_stock():
     stock_quantity = sum(item['quantity'] for item in inventory.values())
     print(f"Total stock quantity : {stock_quantity}")

#Purchase an item and update inventory and till balance
def purchase_item(name,quantity):
    global till_balance #tracks the money balance at the register
    if name in inventory and inventory[name]['quantity'] >= quantity:
        total_cost = inventory[name]['price'] * quantity #total cost
        inventory[name]['quantity'] -= quantity #update inventory after deduction
        till_balance += total_cost #The total cost of the purchase is added to the cash register (till balance), reflecting the income from the sale.
        print(f"Purchased quantity of the item {name}. Total cost: ${total_cost}. Till balance: ${till_balance}")
    else:
        print(f"Item {name} not found or insufficient quantity")

#Return an item and update inventory and till balance
def return_item(name,quantity):
    global till_balance
    if name in inventory:
        refund_amount = inventory[name]["price"] * quantity
        inventory[name]['quantity'] += quantity
        till_balance -= refund_amount
        print(f'Returned {quantity} of item {name}. Refunded amount: {refund_amount}. Till balance{till_balance}')
    else:
        print(f"Item '{name}' not found")

#Menu Interaction
def menu():
    while True:
        print("\n Welcome to Renny Inventory Management")
        print("\n Inventory Menu:")
        print("1. Add Item")
        print("2. Find Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Total Stock")
        print("6. Purchase Item")
        print("7. Return Item")
        print("8. Exit")

        choice = input("Choose an option (1-8): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            name = input("Enter the item name to find: ")
            find_item(name)
        elif choice == '3':
            name = input("Enter the item name to update: ")
            quantity = int(input("Enter the quantity to add/subtract: "))
            update_item(name, quantity)
        elif choice == '4':
            name = input("Enter the item name to delete: ")
            delete_item(name)
        elif choice == '5':
            total_stock()
        elif choice == '6':
            name = input("Enter the item name to purchase: ")
            quantity = int(input("Enter the quantity to purchase: "))
            purchase_item(name, quantity)
        elif choice == '7':
            name = input("Enter the item name to return: ")
            quantity = int(input("Enter the quantity to return: "))
            return_item(name, quantity)
        elif choice == '8':
            print("Exiting the inventory system.")
            break
        else:
            print("Invalid choice. Please try again.")
menu()
