#მომხმარებელს შეაზვანინე 3 რიცხვი და იპოვე ყველაზე დიდი.
num1 = int(input("enter a number"))
num2 = int(input("enter a number"))
num3 = int(input("enter a number"))


if num1 > num2 and num1 > num3:
    print("num1  არის ყველაზე დიდი")
elif num2 > num1 and num2 > num3:
    print("num2  არის ყველაზე დიდი")
else:
    print("num  არის ყველაზე დიდი")