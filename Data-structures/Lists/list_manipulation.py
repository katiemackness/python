# Katie Mackness
# 18/04/24 - Updated 18/02/2025
# Python 3.11.4

# ---------------------------------------------------------
# Guest List
# ---------------------------------------------------------

# Create a party guest list and send a message to each guest 
#   to invite them to the party.
guests = ['Arnold','Marnold','Parnold','Larnold']
message_1 = "\nDear"
message_2 = ",\nWould you like to come to dinner? Jan and Michael are going to be there!!\nLove,\nKatie"

for guest in guests:
    print(message_1, guest, message_2)


# Remove one guest and add a different one.
guests.remove('Marnold')
guests.append('Jenny')


# Add more guests to the list
#   and send a revised message to each guest

guests.insert(0,'Jonathan')
guests.insert(3,'Ponathan')
guests.append('Monathan')

message_2 = f"{message_2}\nP.S. We have found a bigger table! We're adding Jonathan, Ponathan and Monathan to the list :)"

for guest in guests:
    print(message_1,guest,message_2)

# Not enough room. Uninvite the last 5 guests.
popped = []

popped.append(guests.pop())
popped.append(guests.pop())
popped.append(guests.pop())
popped.append(guests.pop())
popped.append(guests.pop())

for guest in popped:
    print(f"Sorry, {guest}, you can't come to dinner anymore. :(")

# Tell the remaining guests they are still invited.
for guest in guests:
    print(f"Dear {guest}, everyone else is uninvited, but you are still invited! Woohoo!")


# Remove the remaining guests from the list.
del guests[0]
del guests[0]

print(guests)
