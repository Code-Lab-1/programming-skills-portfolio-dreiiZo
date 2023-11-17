("Exerise 4 - Deli")

sandwich_orders = ['Turkey', 'Chicken', 'Tuna', 'Beef']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm making your {current_sandwich} sandwich")
    finished_sandwiches.append(current_sandwich)
    
    print("\n")
    for sandwich in finished_sandwiches:
        print(f"I have made a {sandwich} sandwich")