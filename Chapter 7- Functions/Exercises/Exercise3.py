("Exercise 3 - T-Shirt")

def Make_shirt(Size, Message):
    """Summarize the shirt that is going to be made"""
    print(f"\nI'm going to make a {Size} shirt.")
    print(f'It will have a design that says, "{Message}"')
    
Make_shirt('Large', 'Off the Wall')
Make_shirt(Message = "Task Force 141", Size = 'Large')