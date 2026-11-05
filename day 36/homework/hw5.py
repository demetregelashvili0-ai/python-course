#5) შექმენი ორი set, სახელად subjects1 და subjects2. თითოეულში შეინახე 5 სხვადასხვა სასკოლო საგანი. გამოიყენე for ციკლი, რათა პირველი Set-ის ყველა ელემენტი დაბეჭდო. 
# შემდეგ გამოიყენე union() და intersection() მეთოდები და დაბეჭდე ორივე Set-ის გაერთიანება და საერთო ელემენტები.
subjects1 = {"მათემატიკა", "ქართული", "ინგლისური", "ისტორია", "ბიოლოგია"}

subjects2 = {"ფიზიკა", "ქიმია", "გეოგრაფია", "მუსიკა", "სპორტი"}

for i  in subjects1:
    print(i)

all_subjects = subjects1.union(subjects2)
subjects = subjects1.intersection(subjects2)
print(all_subjects)
print(subjects)