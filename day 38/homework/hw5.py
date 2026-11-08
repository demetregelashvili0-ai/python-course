#5) შექმენი Dictionary სახელად school, რომელშიც შეინახავ სკოლის სახელს, მოსწავლეების რაოდენობას და ქალაქს. შემდეგ:
#- დაამატე ახალი Key director, რომელშიც შეინახავ დირექტორის სახელს.
#- შეამოწმე in ოპერატორით, არსებობს თუ არა students Key.
#- წაშალე city Key.
#- შეცვალე სკოლის სახელი.
#- დაბეჭდე საბოლოო Dictionary.

school = {
    "name" : "221 mega skola",
    "students" : 2000,
    "city" : "tbilisi"
}
school["Director"] ="ინგa"

print("students" in school)

del school["city"]

school["name"] = "186 sajaro skola"
print(school)