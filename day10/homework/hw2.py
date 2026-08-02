#2) მომხმარებელს შეაყვანინე რიცხვი. თუ რიცხვი დადებითია, დაბეჭდე Positive, თუ ნულის ტოლია — Zero, სხვა შემთხვევაში — Negative.
num1 = int(input("enter a number"))
if num1 > 0 :
    print("Positive")
elif num1 == 0 :
    print("Zero")
else: 
    print("Negative")