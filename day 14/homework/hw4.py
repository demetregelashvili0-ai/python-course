#4) მომხმარებელს შემოატანინე 5 რიცხვი და იპოვე მათ შორის ყველაზე დიდი რიცხვი.



max_num = int(input("შეიყვანე რიცხვი: "))

for i in range(5):
    num = int(input("შეიყვანე რიცხვი: "))
    if num > max_num:
        max_num = num

print("ყველაზე დიდი რიცხვია:", max_num)