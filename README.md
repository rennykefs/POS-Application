# 🏪 Inventory Management System (Python)

## Introduction  
It allows a store owner to manage stock, handle purchases, process returns, and track the cash register (**till balance**).  


---

## 💻 Features
- ➕ **Add new items** to inventory  
- 🔍 **Find items** by name  
- ✏️ **Update item quantities**  
- 🗑️ **Delete items** from inventory  
- 📦 **Check total stock available**  
- 🛒 **Purchase items** (updates stock + till balance)  
- 🔄 **Return items** (restores stock + refunds cash)  
- 📜 **Menu-driven system** for user interaction  

---

## 🧑‍💻 The Script
```python
# Inventory Management System

inventory = {}  # store items
till_balance = 0  # cash in hand

# Function for creating new items
def create_item(name, quantity, price):
    if name in inventory:
        print(f'Item {name} already exists')
    else:
        inventory[name] = {"quantity": quantity, "price": price}

# Function for adding items
def add_item():
    name = input("Enter item name: ")
    quantity = int(input("Enter item quantity: "))
    price = float(input("Enter item price: "))
    create_item(name, quantity, price)

# Function for finding items
def find_item(name):
    if name in inventory:
        print(f"Item found: Item: {name}, Quantity: {inventory[name]['quantity']}, Price: {inventory[name]['price']}")
    else:
        print(f'Item {name} not found')

# Updating item quantities
def update_item(name, quantity):
    if name in inventory:
        inventory[name]["quantity"] += quantity
        print(f"Item {name} updated successfully. New quantity: {inventory[name]['quantity']}")
    else:
        print(f"Item {name} not found.")

# Deleting items
def delete_item(name):
    if name in inventory:
        del inventory[name]
        print(f"Item {name} deleted successfully")
    else:
        print(f"Item {name} not found")

# Total stock available
def total_stock():
    stock_quantity = sum(item['quantity'] for item in inventory.values())
    print(f"Total stock quantity: {stock_quantity}")

# Purchasing items
def purchase_item(name, quantity):
    global till_balance
    if name in inventory and inventory[name]['quantity'] >= quantity:
        total_cost = inventory[name]['price'] * quantity
        inventory[name]['quantity'] -= quantity
        till_balance += total_cost
        print(f"Purchased {quantity} of {name}. Total cost: ${total_cost}. Till balance: ${till_balance}")
    else:
        print(f"Item {name} not found or insufficient quantity")

# Returning items
def return_item(name, quantity):
    global till_balance
    if name in inventory:
        refund_amount = inventory[name]['price'] * quantity
        inventory[name]['quantity'] += quantity
        till_balance -= refund_amount
        print(f"Returned {quantity} of {name}. Refunded amount: ${refund_amount}. Till balance: ${till_balance}")
    else:
        print(f"Item {name} not found")

# Menu interaction
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
```
## 📚 What I Learned
* Handling global variables for tracking balance
* Using dictionaries for structured data storage
* Performing CRUD operations (Create, Read, Update, Delete)
* Building a menu-driven console app
* Simulating a basic point-of-sale system

