#2)შექმენი Tuple სახელად cars, რომელშიც იქნება 6 მანქანის ბრენდი გამოიყენე len() ფუნქცია ელემენტების რაოდენობის 
# გასაგებად და in ოპერატორით შეამოწმე, არის თუ არა "mercedes-benz" Tuple-ში.
car = ("bmw" , "Toyota" , "Hyundai" , "BYD" , "Ford" , "mercedes-benz")
print(len(car))
"mercedes-benz" in car
if "mercedes-benz" in car:
    print("mercedes-benz არის tuple")