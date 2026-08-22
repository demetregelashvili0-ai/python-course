#8.მომხმარებელს შეაყვანინე 5 რიცხვი. თუ რიცხვი 10-ზე მეტია, გამოტოვე და არ გამოიტანო.


for  i in range(5):
    num = int(input("enter an number: "))
    if num >10:
        continue
    print(num)