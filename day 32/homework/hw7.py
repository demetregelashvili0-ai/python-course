#7) შექმენი Set სახელად `animals`, რომელშიც იქნება 6 ცხოველი. `remove()` მეთოდით წაშალე ერთ-ერთი ცხოველი, `add()` მეთოდით დაამატე ახალი ცხოველი და 
# `discard()` მეთოდით სცადე ისეთი ცხოველის წაშლა, რომელიც Set-ში არ არსებობს. ბოლოს დაბეჭდე Set.
animals = {"wolf", "dog", "cat", "horse", "parrot"}
animals.remove("wolf")
animals.add("hamster")
animals.discard("fox")
print(animals)