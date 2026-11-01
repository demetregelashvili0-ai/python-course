#შექმენი list, რომელშიც მომხმარებლის მიერ შეყვანილი 5 საყვარელი ხილი იქნება შენახული. გამოიყენე for ციკლი და თითოეული ხილი დაამატე set-ში. 
#ბოლოს დაბეჭდე Set, რათა ნახო, რომელი უნიკალური ხილები შეიყვანა მომხმარებელმა.
fruits = []

for i in range(5):
    fruit = input("შეიყვანე საყვარელი ხილი: ")
    fruits.append(fruit)

new_set = set()

for fruit in fruits:
    new_set.add(fruit)

print(new_set)