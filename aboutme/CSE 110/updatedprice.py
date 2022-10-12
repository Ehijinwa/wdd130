import math

child_meal = float(input("what is the price of a child's meal"))
children = float(input("how many children are there"))
adult_meal = float(input("what is the price of an adult's meal"))
adult = float(input("how many adults are there"))
tax_rate = float(input("what is the sales tax rate"))
dog_meal = float(input("what is the price of the dogs meal"))
dog = float(input("how many dogs are there"))

subtotal = child_meal * children + adult_meal * adult + dog_meal * dog
sales_tax = subtotal * tax_rate / 100
total = subtotal + sales_tax

print(f"the subtotal is ${subtotal}")
print(f"the sales tax is ${sales_tax}")
print(f"the total is ${total}")
payment_amount = float(input("what is the payment amount"))
change = payment_amount - total

print(f"the change is ${change:.2f}")
