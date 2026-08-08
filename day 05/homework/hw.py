#1) კომენტარების სახით ახსენით რა არის input() ფუნქცია და რისთვის გამოიყენება
#1)input შეკიტხვას ეკიტხება
#2) მომხმარებელს შემოატანინეთ თავისი სახელი და დაბეჭდეთ, რა სახელი შემოიტანა.
name = input ("whats your name")
print (name)
#3)3) მომხმარებელს შემოატანინეთ თავისი საყვარელი ფერი და დაბეჭდეთ.
fav_color  = input ("whats your favorit color")
print (fav_color)
#4)კომენტარებით ახსენით, რა არის f-string და რატომ არის მისი გამოყენება მოსახერხებელი.
age = 14
print (f"your age is{age}")
#5) მომხმარებელს შემოატანინეთ თავისი ასაკი და f-string-ის გამოყენებით დაბეჭდეთ:I am {ასაკი} years old
age1 = 14
print (f"I am {age1} years old")
#6) მომხმარებელს შემოატანინეთ თავისი გვარი და f-string-ის გამოყენებით დაბეჭდეთ:Your surname is {გვარი}
lastname = "gelashvili"
print (f"your lastname is {lastname}")
#7) მომხმარებელს შემოატანინეთ თავისი საყვარელი ცხოველი და დაბეჭდეთ:My favorite animal is {ცხოველი}
fav_animal = "dog"
print (f"My favorite animal is {fav_animal} ")

#8) მომხმარებელს შემოატანინეთ თავისი საყვარელი სპორტი და დაბეჭდეთ:I like {სპორტი}
fav_sport = "basketball"
print(f"i like {fav_sport}")
#9) მომხმარებელს შემოატანინეთ ქალაქის სახელი და ქვეყანა. შემდეგ f-string-ის გამოყენებით დაბეჭდეთ:I live in {ქალაქი}, {ქვეყანა}
city = input("whitch cyty do you live")
country = input("whitch country do you live")
print (f"i live in {country , city}")
#10) მომხმარებელს შემოატანინეთ თავისი სახელი, ასაკი და საყვარელი ფერი. შემდეგ f-string-ის გამოყენებით დაბეჭდეთ:My name is {სახელი}, I am {ასაკი} years old and my favorite color is {ფერი}.
name = input ("whats your name")
fav_color  = input ("whats your favorit color")
age = input ("whats your age")
print(f"My name is {name}, I am {age} years old and my favorite color is {fav_color}")