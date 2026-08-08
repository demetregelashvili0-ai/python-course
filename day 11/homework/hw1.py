#1) შექმენი ცვლადი balance = 1000.
#მომხმარებელს შეაყვანინე თანხა.
#თუ თანხა დადებითია, შიგნით შეამოწმე ბალანსზე მეტია თუ არა.
#- თუ არა, დაბეჭდე "თანხა წარმატებით გაიტანეთ"
#- თუ მეტია, დაბეჭდე "არასაკმარისი ბალანსი"
#თუ თანხა 0 ან უარყოფითია, დაბეჭდე "არასწორი თანხა"
balance = 1000
costumar_balance = int(input("enter your balance: "))
if  costumar_balance > 0 :
 if  costumar_balance >= balance:
    print("თანხა წარმატებით გაიტანეთ")
if costumar_balance < balance :
    print("არასაკმარისი ბალანსი")
elif costumar_balance <= 0 :
    print("არასწორი თანხა")