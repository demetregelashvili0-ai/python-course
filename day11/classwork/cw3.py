#3) შექმენი ცვლადი username და password.
#თუ username სწორია, შიგნით შეამოწმე password.
#- თუ password სწორია, დაბეჭდე "შესვლა წარმატებულია"
#- თუ არა, დაბეჭდე "არასწორი პაროლი"
#თუ username არასწორია, დაბეჭდე "მომხმარებელი ვერ მოიძებნა"
username = input("enter username")
password = int(input("enter ypur password"))
if username == "gela" :
    if password == 11222:
     print("შესვლა წარმატებულია")
elif username != "gela" :
   print("მომხმარებელი ვერ მოიძებნა")
   if password != 11222:
      print("არასწორი პაროლი")