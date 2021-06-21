#for loop moves through a given range of numbers

#this loop will output all integers 0 through 9
for x in range(10):
    print(x)

print("-----------------------------")

#this loop will start at 20 and loop up to 30
for x in range(20, 30):
    print(x)

#create a list with a variable

word_list = ["Ham", "Cheese", "and", "sandwich"]

#iterate through word_list with a for loop
for word in word_list:
    print(word)

#While loops: follows a certain condition provided a start and stop point
#if no stop point is provided the loop will run infinitely

y = "yes"

print("---------------------")

while y == "yes":
    print("Cool!")
    y = input("Would you like to print 'Cool' again? ")