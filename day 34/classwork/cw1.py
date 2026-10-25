#1) შექმენი ორი Set სახელად `fruits1` და `fruits2`. პირველში შეინახე 5 ხილი, ხოლო მეორეში 5 ხილი. გამოიყენე `union()` მეთოდი, რათა მიიღო ორივე Set-ის ყველა უნიკალური ხილი და დაბეჭდე მიღებული შედეგი.
fruits1 = {"apple", "banana", "orange", "kiwi", "mango"}
fruits2 = {"grape", "watermelon", "pineapple", "banana", "peach"}

all_fruits = fruits1.union(fruits2)

print(all_fruits)