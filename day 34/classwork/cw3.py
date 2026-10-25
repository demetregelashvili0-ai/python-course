#3) შექმენი ორი Set სახელად `students1` და `students2`. პირველში შეინახე 4 მოსწავლის სახელი, ხოლო მეორეში  4 მოსწავლის სახელი.
#  გამოიყენე `union()` მეთოდი, რათა მიიღო ყველა უნიკალური მოსწავლის სახელი.
#  შემდეგ გამოიყენე `len()` ფუნქცია და დაბეჭდე მიღებულ Set-ში არსებული მოსწავლეების რაოდენობა.
students1 = {"gio" , "nika" , "deme" , "sandro"}
students2 = {"lasha", "luka" , "saba" , "andria"}
all_students = students1.union(students2)
print(all_students)
print(len(all_students))