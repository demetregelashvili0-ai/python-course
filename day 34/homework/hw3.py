#3) შექმენი ორი Set სახელად `group_a` და `group_b`. პირველში შეინახე რიცხვები `{5, 10, 15, 20, 25}`, ხოლო მეორეში — `{15, 20, 25, 30, 35}`. თავდაპირველად გამოიყენე`union()`
#მეთოდი და დაბეჭდე ყველა უნიკალური რიცხვი. შემდეგ გამოიყენე `intersection()` მეთოდი და დაბეჭდე მხოლოდ საერთო რიცხვები. ბოლოს `len()` ფუნქციით გაიგე, რამდენი საერთო ელემენტია.
group_a = {5, 10, 15, 20, 25}
group_b = {15, 20, 25, 30, 35}
all_groups = group_a.union(group_b)
groups = group_a.intersection(group_b)
print(all_groups)
print(groups)
print(len(groups))