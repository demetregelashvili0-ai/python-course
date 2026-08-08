#6) მომხმარებელს შეაყვანინე საათი (0-23). თუ საათი 12-ზე ნაკლებია, დაბეჭდე Morning, თუ 18-ზე ნაკლებია — Afternoon, სხვა შემთხვევაში — Evening.
time = int(input("enter what time is it: "))
if time < 12 :
    print("Morning")
elif time <= 18 :
    print("Afternoon")
else:
    print("Evening")