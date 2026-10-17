#5) შექმენი Set სახელად `programming_languages`, რომელშიც იქნება 5 პროგრამირების ენა. გამოიყენე `len()` ფუნქცია ელემენტების რაოდენობის გასაგებად,
#  `discard()` მეთოდით სცადე ისეთი ენის წაშლა, რომელიც Set-ში არ არსებობს, ხოლო `in` ოპერატორით შეამოწმე, არის თუ არა `"JavaScript"` Set-ში. ბოლოს დაბეჭდე Set.
programming_languages = {"Python", "Java", "C++", "JavaScript", "C#"}
print(len(programming_languages))
programming_languages.discard("C#")
print(programming_languages)
print("JavaScript" in programming_languages)