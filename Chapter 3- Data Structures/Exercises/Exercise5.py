("Exercise 5 - Change Guest List")

guest = ["Amanda", "Michael", "Jimmy"]
Name = guest[0]
print(f"\nUnforunatly, {Name} won't be able to make it tonight")

del(guest[0])
guest.insert(0, 'Tracey')
name = guest[0]
print(f"\n{Name}, Please come to dinner at 7:00 Tonight")

name = guest[1]
print(f"{Name}, Please come to dinner at 7:00 Tonight")

name = guest[2]
print(f"{Name}, Please come to dinner at 7:00 Tonight")