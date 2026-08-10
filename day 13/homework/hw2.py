#while loop-ის გამოყენებით გამოთვალეთ 1-დან 100-მდე ყველა კენტი რიცხვის ჯამი.
total = 0
i  = 1

while i <= 100:
    if i % 2 != 0:
        total += i
    i += 1

print(total)