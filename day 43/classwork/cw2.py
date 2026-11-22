#. შექმენით nested dictionary სახელად school, რომელშიც შეინახავთ სკოლის ინფორმაციას. მას უნდა ჰქონდეს student,
#  teacher და classroom ობიექტები. თითოეულ ობიექტში შეინახეთ მინიმუმ 3 ინფორმაცია. გამოიტანეთ ტერმინალში ყველა ობიექტის მონაცემები.

school = {
    "student": {
        "name": "გიორგი",
        "age": 15,
        "grade": 10
    },
    "teacher": {
        "name": "ნინო",
        "subject": "მათემატიკა",
        "age": 35
    },
    "classroom": {
        "number": 5,
        "students": 20,
        "floor": 2
    }
}

print(school["student"])
print(school["teacher"])
print(school["classroom"])
