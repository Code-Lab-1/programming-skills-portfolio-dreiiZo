("Exerise 4 - Large Shirts")

def Make_shirt(Size = 'XL', Message = 'Bravo 0-6'):
    """Summarize the shirt that is going to be made"""
    print(f"\nI'm going to make a {Size} shirt.")
    print(f'It will have a design that says, "{Message}"')
    
Make_shirt()
Make_shirt(Size = 'Medium')
Make_shirt('Small', 'Weapons Hot Vaqueros')