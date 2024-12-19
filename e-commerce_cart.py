cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}

def totalPrice():
    total=sum(cart_items.values())
    if len(cart_items)==0:
        print("The cart is empty!!")
    elif len(cart_items)>5:
        total*=0.9
        print("Total Price: ",total)
    else:
        print("Total Price: ",total)

totalPrice()