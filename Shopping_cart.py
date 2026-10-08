cart=["apple","banana","orange","milk","bread"]
#Remove duplicates
cart=list(set(cart))

#add cheese
cart.append("cheese")

#remove milk
cart.remove("milk")

#sort alphabetically
cart.sort()
print(" final Shopping cart items:",cart)
print("Total items in the cart:",len(cart))