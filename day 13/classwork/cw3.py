#3)მომხმარებელს შემოატანინეთ რიცხვები. სანამ მომხმარებელი არ შეიყვანს 0-ს, დაამატეთ ყველა რიცხვი total ცვლადში. 0-ის შეყვანისას გამოიყენეთ break და ბოლოს გამოიტანეთ ჯამი
total = 0

while True:
    num = int(input("ente ra number: "))

    if num == 0:
        break

    
    total += num
print(total)