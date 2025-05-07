def identificar_animal(palavra1, palavra2, palavra3):
    if palavra1 == "vertebrado":
        if palavra2 == "ave":
            if palavra3 == "carnivoro":
                return "aguia"
            elif palavra3 == "onivoro":
                return "pomba"
        elif palavra2 == "mamifero":
            if palvra3 == "onivoro":
                return "homem"
            elif palavra3 == "herbivoro":
                return "vaca"
    elif palavra1 == "invertebrado":
        if palavra2 == "inseto":
            if palavra3 == "hematofago":
                return "pulga"
            elif palara3 == "herbivoro":
                return "lagarta"
        elif palavra2 == "anelideo":
            if palavra3 =="hematofago":
                return "sanguessuga"
            elif palavra3 == "onivoro":
                return "Minoca"

entrada1 = input().strip()
entrada2= input().strip()
entrada3 =input().strip()

animal = identificar_animal(entrada1, entrada2, entrada3)
print(animal + "aaa")
