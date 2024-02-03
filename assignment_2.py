input_age = int(input("Enter your age: "))

if input_age < 4:
    price = 0
elif input_age < 18:
    price = 25
elif input_age < 100:
    price = 40
else:
    price = 10
print(f"Your admission cost is ${price}.")
