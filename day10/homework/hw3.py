#3)მომხმარებელს შეაყვანინე ქულა. თუ ქულა 90 ან მეტია, დაბეჭდე Grade A, თუ 70 ან მეტია — Grade B, თუ 50 ან მეტია — Grade C, სხვა შემთხვევაში — Failed.
score = int(input("enter your score: "))
if score >= 90 :
    print("Grade A")
elif score >=70 :
    print("Grade B")
elif score >= 50 :
    print("Grade C")
else: 
    print("Failed")