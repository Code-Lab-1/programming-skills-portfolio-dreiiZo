("Exerise 5 - Cities")

def describe_city(City, Country= 'Iceland'):
    """Describe a City"""
    msg = f"{City} is on {Country}"
    print(msg)
    
    describe_city('Gardabaer')
    describe_city('Pangasinan')
    describe_city('Hvammstangi', 'Iceland')
    