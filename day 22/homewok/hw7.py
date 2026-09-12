#7) შექმენი ცვლადი message = "  Hello World  ". lstrip() მეთოდით მოაშორე ჰარები მხოლოდ მარცხნიდან,
#  ხოლო [::-1] Slicing-ის გამოყენებით ამოატრიალე მთლიანი ტექსტი უკუღმა. დაბეჭდე შედეგი.
message = "  Hello World  "
print(message.lstrip()[::-1])