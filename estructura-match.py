frutas = "Mangos"

match frutas:
    case "Mangos":
        print(f"{frutas}")
    case "Manzanas":
        print(f"{frutas}")
    case _ :
        print(f"{frutas} no existe")

hora = 10
match hora:
    case _ if 5 <= hora < 12:
        print("mañana")
    case _ if 12 <= hora < 18:
        print("tarde")
    case _ if 18 <= hora < 22:
        print("noche")
    case _:
        print("Es muy tarde")