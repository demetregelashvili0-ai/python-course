# შექმენით nested dictionary სახელად library, რომელშიც შეინახავთ 3 წიგნის ინფორმაციას. თითოეულ წიგნს უნდა ჰქონდეს title, author, pages და available მონაცემები.
#  დაამატეთ მეოთხე წიგნი, შემდეგ for ციკლების გამოყენებით გადაუარეთ ყველა წიგნს და გამოიტანეთ თითოეული წიგნის ყველა ინფორმაცია.
# ასევე შექმენით nested list სახელად grades, რომელშიც შეინახავთ 3 მოსწავლის ქულებს და for ციკლების გამოყენებით გამოიტანეთ ყველა მოსწავლის ყველა ქულ

library = {
    "book1": {
        "title": "Harry Potter",
        "author": "J.K. Rowling",
        "pages": 300,
        "available": 30
    },
    "book2": {
        "title": "The Hobbit",
        "author": "Tolkien",
        "pages": 250,
        "available": 20
    },
    "book3": {
        "title": "1984",
        "author": "George Orwell",
        "pages": 328,
        "available": 13
    }
}

library["book4"] = {
    "title": "Minecraft",
    "author": "Markus Persson",
    "pages": 200,
    "available": 74
}
for book in library:
    print(book)
    for info in library[book]:
        print(info, ":", library[book][info])

grades = [
    ["Giorgi", [90, 85, 100]],
    ["Demetre", [80, 95, 90]],
    ["Nika", [70, 85, 95]]
]

for student in grades:
    print(student[0])
    for grade in student[1]:
        print(grade)
