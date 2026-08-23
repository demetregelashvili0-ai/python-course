#5.მომხმარებელს შეაყვანინე 10 რიცხვი და თუ რიცხვი არის 0, არ გამოიტანო.
for i in range(10):
    num = int(input("enter a number: "))
    if num == 0:
        continue
    print(num)