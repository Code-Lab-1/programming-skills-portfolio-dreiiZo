("Exerise 1 - Pizza Toppings")

prompt = "\nWhat topping would you like on the pizza?"
prompt += "\nPress 'Enter' when you are done: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f" I'll add {topping} on your pizza.")
    else:
        break