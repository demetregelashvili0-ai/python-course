#4) შექმენი list, რომელშიც შეინახავ 12 რიცხვს. გამოიყენე while ციკლი და დაბეჭდე მხოლოდ უარყოფითი რიცხვები.
#  ყველა დადებითი რიცხვი კი დაამატე ცალკე tuple-ში (შეგიძლია ჯერ ცალკე List გამოიყენო და შემდეგ Tuple-ად გადააქციო). 

nums = [4, -2, 7, -5, 9, -1, 3, -8, 6, -4, 2, -7]

i = 0
my_list = []

while i < 12:
    if nums[i] < 0:
        print(nums[i])
    elif nums[i] > 0:
        my_list.append(nums[i])

    i += 1

my_tuple = tuple(my_list)

print(my_tuple)