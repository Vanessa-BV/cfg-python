for number in range(9):
    print("~" * number)


today = input ("What days is it? ")
is_monday = today == "Monday"
print("Today is Monday: {}".format(is_monday))

#Comparison operators
# 1. Input the price of a burger using input()
# 2. Check whether the price is less than or equal (<=) 10.00
# 3. Print the result in the format below
price = input("How much is a burger? ")
within_budget = float(price) <= 10.00
print("Burger is within budget {}".format(within_budget))

#Logical operators
mars_choice = input("Would you like to visit Mars? y/n ")
is_willing = mars_choice == "y"
affordable = input("Can you afford to visit Mars? y/n ")
can_afford = affordable == "y"
should_you_visit_mars = is_willing and can_afford
print("You should visit Mars: {}".format(should_you_visit_mars))

price = input("How much is a burger? ")
vegetarian = input("Is there a vegetarian option? y/n ")
within_budget= float(price) <= 10.00
has_vegetarian = vegetarian == "y"
is_good_choice = within_budget and has_vegetarian
print("Restaurant meets criteria: {}".format(is_good_choice))

#IF statements
password = input("password: ")
if password == "jumanji":
    print("Success!")