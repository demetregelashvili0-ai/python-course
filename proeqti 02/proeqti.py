#შექმენით პროგრამა, რომელიც უზრუნველყოფს მომხმარებლის ავტორიზაციას, ითვლის პროდუქტების შეძენის ღირებულებას (ფასდაკლებებითა და ბონუსებით),
#  აღრიცხავს ყოველდღიურ ხარჯებს და აგენერირებს დეტალურ ფინანსურ რეზიუმეს.
# ავტორიზაცია და პროფილის შექმნა
# მოითხოვეთ პაროლი while ციკლის გამოყენებით. სანამ მომხმარებელი არ შეიყვანს "python123"-ს, მოითხოვეთ ხელახლა.
# წარმატებული შესვლის შემდეგ შემოატანინეთ: სახელი, გვარი, ასაკი (int), ქალაქი, ქვეყანა და საწყისი ბალანსი (float).
# შექმენით Boolean ცვლადი is_adult, რომელიც შეამოწმებს, არის თუ არა ასაკი 18-ის ან მეტი.
# type() ფუნქციით შეამოწმეთ და დაბეჭდეთ მონაცემთა ტიპები.


coreqt_password = "python123"
password = input("enter your password")
while  coreqt_password != password:
    print("პაროლი არასწორია სცადეთ ხელახლა: ")

    password = input("enter your password")
print("პაროლი სწორია")


name =input("enter your name: ")
lastname =input("enter your lsdtnsme: ")
age = int(input("enter your age: "))
country = input("enter your country: ")
city = input("enter your city: ")
balans = float(input("Enter your balans: "))


is_adult = age <= 18

print (f"თქვენი სახელია არის: {name} {type(name)} და გვარი : {lastname} {type(lastname)} ასაკი: {age} {type(age)} თქვენ ცხოვრობთ ამ ქვეყანჯასში: {country} (type{country}) და ამ ქალაქში: {city} {type(city)} თქვენი ბალანსი არის: {balans} {type(balans)}")


# პროდუქტის ყიდვა და ფასდაკლების სისტემა
# მომხმარებელს შემოატანინეთ სასურველი პროდუქტის სახელი, ერთეულის ფასი (float) და რაოდენობა (int).
# იპოვეთ ჯამური ღირებულება (ფასი * რაოდენობა).
# Nested IF და ლოგიკური ოპერატორებით (and, or):ჯერ შეამოწმეთ, არის თუ არა ბალანსი საკმარისი.თუ ბალანსი საკმარისია:
# თუ რაოდენობა 10-ზე მეტია AND ჯამი 100-ზე მეტია გამოიყენეთ 20%-იანი ფასდაკლება.
# თუ ჯამი 50-ზე მეტია გამოიყენეთ 10%-იანი ფასდაკლება.
# სხვა შემთხვევაში 0% ფასდაკლება.ჩამოაჭერით საბოლოო თანხა ბალანსს.
# თუ ბალანსი არ არის საკმარისი, დაბეჭდეთ შესაბამისი შეტყობინება.


prodaqt = input("enter your brodaqt name: ")
prodaqt_amount = int(input("enter the amount of produqt you have: "))
prodaqt_price = float(input("enter what price your looking for seliing it: "))

total_price = prodaqt_price * prodaqt_amount
print(total_price)
if balans >= total_price:
    if prodaqt_amount  > 10 and total_price > 100 :
        discounted = 20 
        print("თქვენ მიღეთ ფასდაკლება 20% ით")

    elif total_price > 50:
        discounted = 10
        print("თქვენ მიიღეთ 10% ფასდაკლება")

    else:
        discounted = 0
        print("თქვენ მიიღეთ 0% ფასდაკლება")
    discounted_amount = (total_price * discounted) / 100
    finall_price = total_price - discounted_amount
    balans -= finall_price
    print(finall_price , balans)
    bonutpoints = int(finall_price // 10)
    print(bonutpoints)
else:
    print("თქვენ ბალანსზე საკმარისი თანხა არი გაქვთ")
# გამოითვალეთ ბონუს ქულები: ყოველ სრულ 10 ლარზე 1 ბონუს ქულა (გამოიყენეთ // მთელზე გაყოფა). ასევე იპოვეთ %-ით გაყოფის ნაშთი.
# ხარჯების აღრიცხვის ციკლი (while, break, total)
# შექმენით ცვლადი total_expenses = 0.
# while ციკლით მომხმარებელს სთხოვეთ დამატებითი ხარჯების შეყვანა:
# თუ შემოიყვანს 0-ს, ციკლი გაჩერდეს (break).
# თუ შემოიყვანს უარყოფით რიცხვს, ციკლი გაჩერდეს (break).
# დადებითი ხარჯები დაამატეთ total_expenses-ში.
# მათემატიკური ანალიზი და საბოლოო რეზიუმე
# გამოითვალეთ დარჩენილი ბალანსის კვადრატი ( 2) და კუბი ( 3).
# % 2 == 0-ით შეამოწმეთ, ლუწია თუ კენტი დარჩენილი ბალანსის მთელი ნაწილი.
# f-string-ით გამოიტანეთ სრული ფინანსური ანგარიში.

total_expenses = 0
while True:
    expense = float(input("Enter your spent money: "))
    if expense <= 0:
        print("Entering spent money is completed!")
        break
    total_expenses -= expense




print(f"დახარჟული თანხის სრული რაოდენობა არის {total_expenses}")
balans -= total_expenses
print(balans)
sqcverofbalans = balans**2
cubedbalans = balans**3
intbalans = int(balans)
if intbalans % 2 == 0:
    print(f"ბალანზე დარჩენილია ლუწი რიცხვი სრაოდენობა {intbalans}")
else:
    print(f"ბალანზე დარჩენილია კენტი რიცხვი სრაოდენობა {intbalans}")
print("საბოლოო ფინანსური ხარჯი")
print(f"მომხმარებელი: {name}, {lastname} ასაკი: {age} {is_adult}")
print(f"თქვენი ბალანსია {balans}")