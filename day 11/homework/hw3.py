#3) მომხმარებელს შეაყვანინე ტემპერატურა.
#თუ ტემპერატურა 0-ზე მეტია, შიგნით შეამოწმე 30-ზე მეტია თუ არა.
#- თუ არის, დაბეჭდე "ცხელა"
#- თუ არა, დაბეჭდე "თბილა"
#თუ ტემპერატურა 0 ან ნაკლებია, დაბეჭდე "ცივა"
temperayure = int(input("enter temperayure"))

if temperayure > 0 :
 if temperayure > 30:
    print("ცხელა")
if temperayure < 30 :
    print("თბილა")
elif temperayure <= 0:
    print("ცივა")