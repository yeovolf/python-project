inventory = {"tomato":30, "thyme":4.5, "garlic":7.5, "rice":10, "onions":4, "fish":9.99}

shopping_list = []

list_length = 5

for idx in range(list_length):
    item = input('Enter item to buy: ')
    shopping_list.append(item)

print(shopping_list)

cart = shopping_list

def grocery_cart_total(price):
    try:
        total = 0
        for item in cart:
            total+= inventory[item]

    except Exception as error:
        return("Item not in inventory")

    return total    

total_cart = grocery_cart_total(shopping_list) 
    
print(f"the grocery cart total is:{total_cart}")
    
    

    
    