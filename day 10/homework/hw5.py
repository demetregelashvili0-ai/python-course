#5)მომხმარებელს შეაყვანინე თანხა. თუ თანხა 100 ან მეტია, დაბეჭდე Expensive, თუ 50 ან მეტია — Medium, სხვა შემთხვევაში — Cheap.
your_monye  = int(input("enter your price"))
if your_monye >= 100:
    print("Expensive")
elif your_monye >= 50 :
    print("Medium")
else:
    print("Cheap")