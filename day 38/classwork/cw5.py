#5) შექმენი Dictionary სახელად game, რომელშიც შეინახავ თამაშის სახელს, ჟანრს და რეიტინგს. შემდეგ:
#დაამატე ახალი Key developer, რომელშიც შეინახავ თამაშის შემქმნელის სახელს.
#შეამოწმე in ოპერატორით, არსებობს თუ არა rating Key.
#წაშალე genre Key.
#შეცვალე თამაშის სახელი.
#დაბეჭდე საბოლოო ობიექტი.
game = {
    "name": "Doom",
    "genre": "FPS",
    "rating": 9.0
}

game["developer"] = "id Software"

if "rating" in game:
    print("Rating Key არსებობს!")
else:
    print("Rating Key არ არსებობს!")

del game["genre"]

game["name"] = "Doom Eternal"

print(game)