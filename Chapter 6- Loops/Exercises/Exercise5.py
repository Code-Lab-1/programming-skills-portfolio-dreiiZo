("Exerise 5 - No Pastrami")

sandwich_orders = [
    'Bacon', 'Cheese', 'Egg', 'Mayonnaise'
    'Pepper', 'chicken', 'beef', "pastrami",'pastrami','pastrami']
finished_sanwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastarami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')
    
print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"i'm working on your {current_sandwich} sandwich")
    finished_sanwiches.apppend(current_sandwich)
    
    print("\n")
    for sandwhich in finished_sanwiches:
        print(f"I have made a {current_sandwich} sandwich")
    
    