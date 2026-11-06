inventory = {
    "Laptop": 10,
    "Mouse": 20,
    "Keyboard": 15
}

# Add new stock
def add_stock(product, quantity):

    inventory[product] = inventory.get(product, 0) + quantity

    print(quantity, product, "added successfully")


# Sell product
def sell_product(product, quantity):

    if product not in inventory:

        print(product, "does not exist!")

    elif inventory[product] >= quantity:

        inventory[product] -= quantity

        print(quantity, product, "sold successfully")

    else:

        print("Insufficient stock!")


# Testing
add_stock("Mouse", 10)

add_stock("Monitor", 5)

sell_product("Laptop", 2)

sell_product("Mobile", 1)

sell_product("Keyboard", 20)

print("\nFinal Inventory:")
print(inventory)