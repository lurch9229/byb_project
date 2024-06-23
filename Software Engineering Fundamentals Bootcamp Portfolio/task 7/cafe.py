"""
create a program to determine value of stock
in a cafe. Can determine value based on per item and all items
"""

"""
create list and dicts for menu, stock and price
determine total items in stock by adding stock for each item
print the total amount of items in stock
"""
#   Create list and dicts
menu = ["coffee", "tea", "cake", "cookie"]
print(menu)

stock = {"coffee": 10, "tea": 10, "cake": 5, "cookie": 5}
print(stock)

price = {"coffee": 120, "tea": 100, "cake": 200, "cookie": 150}
print(price)

#   Determine total number of items in stock
total_stock = stock["coffee"] + stock["tea"] + stock["cake"] + stock["cookie"]
print(f"\nCafe has {total_stock} items in stock")

#   loop through indexes in var_menu
for i in menu:
    if i == "coffee":
        item_value = stock["coffee"] * price["coffee"]  # stock * price for coffee
        print(f"\nTotal stock of coffee is worth: {item_value}")
    elif i == "tea":
        item_value = stock["tea"] * price["tea"]    # stock * price for tea
        print(f"Total stock of tea is worth {item_value}")
    elif i == "cake":
        item_value = stock["cake"] * price["cake"]  # stock * price for cake
        print(f"Total stock of cake is worth: {item_value}")
    else:
        item_value = stock["cookie"] * price["cookie"]  # stock * price for cookie
        print(f"Total stock of cookies are worth: {item_value}")


#   Determine the total value of products in cafe
"""
create int variable for each item
loop through indexes in menu
    if index = specific menu item
        stock * item price
take value of item stock for each item and add them together
"""

#   create variables
coffee = int
tea = int
cake = int
cookie = int

#   loop through indexes in var_menu
for i in menu:
    if i == "coffee":
        coffee = int(stock["coffee"] * price["coffee"])
    elif i == "tea":
        tea = int(stock["tea"] * price["tea"])
    elif i == "cake":
        cake = int(stock["cake"] * price["cake"])
    elif i == "cookie":
        cookie = int(stock["cookie"] * price["cookie"])


#   create variable of items added together
value = coffee + tea + cake + cookie
print(f"\nTotal value of items in cafe: {value}")

