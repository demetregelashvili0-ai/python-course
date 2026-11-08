#2) შექმენი Dictionary სახელად car, რომელშიც შეინახავ მანქანის ბრენდს, მოდელს,
#  გამოშვების წელს და ფერს. შემდეგ წაშალე Dictionary-დამ color Key და დაბეჭდე განახლებული Dictionary.
car = {
    "car_name" : "bmw",
    "car_brend" : "m5 competition",
    "car_year" : 2018,
    "car_color" : "black"
}

del car["car_color"]
print(car)