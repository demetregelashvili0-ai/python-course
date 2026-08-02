#7) მომხმარებელს შეაყვანინე ორი რიცხვი. თუ პირველი რიცხვი მეორეზე მეტია, დაბეჭდე First number is bigger
# , თუ ნაკლებია — Second number is bigger, სხვა შემთხვევაში — Numbers are equal.
num1 = int(input("enter a number"))
num2 = int(input("enter a second number"))
if num1 > num2:
    print("first number is bigger")
elif num1 < num2 :
    print("Second number is bigger")
else:
    print("Numbers are equal")
