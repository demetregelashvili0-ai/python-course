#შექმენით nested dictionary სახელად game, რომელშიც შეინახავთ თამაშის ინფორმაციას. 
# მას უნდა ჰქონდეს player და weapon ობიექტები. player-ში შეინახეთ მოთამაშის სახელი, level და health, ხოლო weapon-ში იარაღის სახელი, 
# damage და rarity. შეცვალეთ მოთამაშის level, health და იარაღის damage. საბოლოოდ გამოიტანეთ განახლებული ინფორმაცია.


game = {
    "player": {
        "name": "Giorgi",
        "level": 10,
        "health": 100
    },

    "weapon": {
        "name": "Sword",
        "damage": 50,
        "rarity": "Legendary"
    }
}

game["player"]["level"] = 20
game["player"]["health"] = 150
game["weapon"]["damage"] = 100

print("Player:", game["player"])
print("Weapon:", game["weapon"])
