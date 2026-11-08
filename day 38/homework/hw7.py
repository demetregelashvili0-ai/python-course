#7) შექმენი Dictionary სახელად movie, რომელშიც შეინახავ ფილმის სახელს, რეჟისორს, გამოშვების წელს და ჟანრს. მომხმარებელს შემოატანინე Key და შეამოწმე in ოპერატორით,
#  არსებობს თუ არა ის Dictionary-ში. შემდეგ წაშალე year Key და დაბეჭდე საბოლოო Dictionary.
movie = {
    "name": "Avatar",
    "director": "James Cameron",
    "year": 2009,
    "genre": "Sci-Fi"
}

key = input("Enter Key: ")

if key in movie:
    print("Key exists")
else:
    print("Key does not exist")

del movie["year"]

print(movie)