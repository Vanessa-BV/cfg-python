#Session 1
"Cat" + "videos"
"Cat" + " videos"
"cat" * 3
"Cat".upper()
"Cat".lower()
"the lord of the rings".title()

#Session 1 - variables
food = "spaghetti"
print(food)

oranges = 12
cost_per_orange = 0.5
total_cost = oranges * cost_per_orange
print(total_cost)

print(str(oranges) + " oranges")
print("costs " + str(total_cost))

#Session 2 - user input
user_name = "sara_1987"
age = 23
output = "{} is {} years old".format(user_name, age)
print(output)

days = 31
hours =24
total_hours = days * hours
msg = "There are {} in {} days".format(total_hours, days)
print(msg)

fruit = input("What fruit do you like? ")
veg = input("What veg do you like? ")
print("You like {} and and you like {}".format(fruit, veg))

apples_string = "12"
total_apples = int(apples_string) + 5
print(total_apples)

purchased_apples = input("How many apples did you buy? ")
print(type(purchased_apples))
total_apples = int(purchased_apples) + 5
print(total_apples)

friends = input("How many friends? ")
pizzas = int(friends) * 0.5
print("You need {} pizzas for {} friends".format(pizzas, friends))


#Session 2 - modules (math, datetime, timeit, re, copy)
import datetime
now = datetime.datetime.now()
print(now)

#Session 2 - formatting date objects
import datetime
my_date = datetime.date(2020, 12, 31)
print(my_date.strftime("%d-%b-%Y"))

#Session 2 - for loops (allow you to repeat a blockof code multiple times)
for number in range(5):
    print(number)

for character in "Banana":
    print(character)

for name in ["Mary", "Rebecca", "Sandy"]:
    print(name)

#Session 2 - while loop (used to iterate over a block of code or statements as long as the test experession is true)
store_capacity = 5 #

while store_capacity > 0:
    print("Please come in. Spaces available: " + str(store_capacity))
    store_capacity = store_capacity - 1

print("\n Please wait for someone to exit the store.")

