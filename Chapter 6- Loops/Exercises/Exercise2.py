("Exerise 2 - Movie Ticket")

prompt = "How old are you"
prompt += "\nPress 'Enter' when you are Done: "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    
    if age < 3:
        print(" You can get in, it's free!")
    elif age < 13:
        print(" Your ticket is $10")
    else:
        print(" Your ticket is $15")