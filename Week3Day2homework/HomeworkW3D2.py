cartItems = []
cartTotal = 0

def addItem(itemName, itemPrice):
    cartItems.append(itemName)
    return(itemPrice)
    
cartTotal += addItem("Apple", 0.5)
cartTotal += addItem("Orrange", 0.65)
cartTotal += addItem("Bread", 4.5)
cartTotal += addItem("Bread", 4.5)
cartTotal += addItem("Orange", 4.5)
cartTotal += addItem("Bread", 4.5)
cartTotal += addItem("Watermelon", 5)
cartTotal += addItem("Blueberries", 5)
cartTotal += addItem("Blueberries", 5)
cartTotal += addItem("Blueberries", 5)
cartTotal += addItem("Blueberries", 5)
cartTotal += addItem("Blueberries", 5)
cartTotal += addItem("Blueberries", 5)

cartSummary = dict((item,cartItems.count(item))for item in cartItems)

print(cartSummary)
print(cartTotal)
