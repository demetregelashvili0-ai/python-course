#3) მომხმარებელს შემოატანინე 5 რიცხვი და for loop-ის გამოყენებით იპოვე მათი ჯამი.jami = 0

total = 0


for i in range(5):
    num = int(input("შეიყვანე რიცხვი: "))
    total += num

print("რიცხვების ჯამია:", total)