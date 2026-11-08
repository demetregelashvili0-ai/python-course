#6) შექმენი Dictionary სახელად footballer, რომელშიც შეინახავ ფეხბურთელის სახელს, ასაკს, გუნდს და გატანილი გოლების რაოდენობას. შემდეგ დაამატე ახალი Key position
# , რომელშიც შეინახავ ფეხბურთელის პოზიციას. შეცვალე მისი ასაკი და გოლების რაოდენობა. დაბეჭდე განახლებული Dictionary.
footballer = {
    "name": "Lionel Messi",
    "age": 37,
    "team": "Inter Miami",
    "goals": 850
}

footballer["position"] = "Forward"

footballer["age"] = 39
footballer["goals"] = 937

print(footballer)