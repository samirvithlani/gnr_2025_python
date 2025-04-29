season = input("enter season name")
match season:
    case "spring":
        print("Spring is the season of new beginnings.")
    case "summer":
        print("Summer is the season of sunshine and warmth.")
    case "autumn":
        print("Autumn is the season of harvest and change.")
    case "winter":
        print("Winter is the season of cold and snow.")
    case _:
        print("Invalid season name.")