#Create a loop that prints all of the items from a store to a terminal
#with their index number stored in brackets beside them

item_store = ["[0] Bread", "[1] Milk", "[2] Eggs", "[3] Hot Wheels", "[4] Mangoes", "[5] Paper Towels", "[6] Dish Soap", "[7] Lilies"]

item_prices = ["[0] Bread-$2.50", "[1] Milk-$1.25", "[2] Eggs-$2.00", "[3] Hot Wheels-$1", "[4] Mangoes-$0.75", "[5] Paper Towels-$3.10", "[6] Dish Soap-$1.67", "[7] Lilies- $2.99"]

print("Here is a list of items found at a market: ")

#print the item_store list to the user in the terminal
for items in item_store:
    print(items)

print("--------------------------------------------")

#print the list with the cost of each item
print("Here are the prices of each item: ")

for prices in item_prices:
    print(prices)

#create an empty list to store items
item_box = []

#the maximum amount of items the user will be allowed to select
maximum_amount = 4

#create a list that just holds 'double type' variables which correspond
#to the 'item_prices' list

cost_list = [2.50, 1.25, 2.00, 1.00, 0.75, 3.10, 1.67, 2.99]

#create an empty list to store the item prices
price_list = []

#write another loop to start the item selector process
#this loop will run 4 times since the maximum amount is set to 4
for m in range(maximum_amount):
        item_one = input("Please select the item you would like by entering the corresponding item number: ")

        # call the item_box and append the selected item 
        # in the item_store list input by the user
        # to the item_box list
        
        item_box.append(item_store[int(item_one)])

        # call the empty price_list list and append the price amounts
        # from the cost_list

        price_list.append(cost_list[int(item_one)])

#output the items the user selected to the terminal
#output the total cost the user owes with respect to the items selected

print("The items you took home are: ")

for things in item_box:
    print(things)

print("Here is your receipt: ")
for prices in price_list:
    print(prices)

#import math
#print total using fsum taken from math library which stands for float sum
print("You owe: ")
import math
print(math.fsum(price_list))