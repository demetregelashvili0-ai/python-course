#4) მომხმარებელს შეაყვანინე ტემპერატურა. თუ ტემპერატურა 30 ან მეტია, დაბეჭდე Hot, თუ 15 ან მეტია — Warm, სხვა შემთხვევაში — Cold.

temperayure = int(input("enter temperayure"))


if temperayure >= 30:
    print("Hot")
elif temperayure >=15:
    print("Warm")
else:
    print("Cold")
