import json
countries = {
    "Ukraine": {"area": 714000, "population": 33000000, "capital": "Kyiv", "continent": "Europe"},
    "USA": {"area": 2114000, "population": 233000000, "capital": "Washington", "continent": "North America"},
    "Slovakia": {"area": 344000, "population": 13000000, "capital": "Bratislava", "continent": "Europe"},
    "Germany": {"area": 540000, "population": 78000000, "capital": "Berlin", "continent": "Europe"},
    "France": {"area": 657800, "population": 92000000, "capital": "Paris", "continent": "Europe"},
    "Denmark": {"area": 213240, "population": 8500000, "capital": "Copenhagen", "continent": "Europe"},
    "Sweden": {"area": 4570000, "population": 23580000, "capital": "Stockholm", "continent": "Europe"},
    "Bulgaria": {"area": 234000, "population": 7849000, "capital": "Sofia", "continent": "Europe"},
    "Estonia": {"area": 145000, "population": 4500000, "capital": "Tallinn", "continent": "Europe"},
    "Spain": {"area": 475000, "population": 62500000, "capital": "Madrid", "continent": "Europe"},
}
with open("data.json", "w") as file:
    json.dump(countries, file, ensure_ascii=False, indent=4)


def print_countries():
    with open("data.json", "r") as file:
        countries = json.load(file)

    for cname, j in countries.items():
        print(f"Країна: {cname}")
        print(f"Площа: {j['area']} км²")
        print(f"Населення: {j['population']} осіб")
        print(f"Столиця: {j['capital']}")
        print(f"Континент: {j['continent']}")
        print()


def add_country(countries):
    with open("data.json", "r") as file:
        countries = json.load(file)
        cname = input("Введіть назву країни: ")
        if cname in countries:
            print("Така країна вже існує!\n")
            add_country(countries)
        elif cname.isdigit():
            print("Назва країни не може бути числом!\n")
            add_country(countries)

        area = int(input("Введіть площу (у км²): "))
        population = int(input("Введіть населення: "))
        capital = input("Введіть столицю: ")
        if capital.isdigit():
            print("Введіть вірно ")
            add_country(countries)
        continent = input("Введіть континент: ")
        if continent.isdigit():
            print("Введіть вірно ")
            add_country(countries)

        countries[cname] = {
            "area": area,
            "population": population,
            "capital": capital,
            "continent": continent
        }
    with open("data.json", "w") as file:
        json.dump(countries, file, ensure_ascii=False, indent=4)
    print(f"Країну '{cname}'  додано\n")


def delete_country(countries):
    with open("data.json", "r") as file:
        countries = json.load(file)
        cname = input("Введіть назву країни: ")
        if cname.isdigit():
            delete_country(countries)
        if cname in countries:
            del countries[cname]
            print(f"Країну '{cname}' видалено\n")
        else:
            print(f"Країну '{cname}' не знайдено!\n")
    with open("data.json", "w") as file:
        json.dump(countries, file, ensure_ascii=False, indent=4)
        file.close()


def choose_country(countries):
    with open("data.json", "r") as file:
        countries = json.load(file)
        cname = input("Введіть назву країни: ")
        if cname.isdigit():
            choose_country(countries)
        if cname in countries:
            print(f"Країна: {cname}\n")
            print(f"Площа: {countries[cname]['area']} км²")
            print(f"Населення: {countries[cname]['population']} осіб")
            print(f"Столиця: {countries[cname]['capital']}")
            print(f"Континент: {countries[cname]['continent']}")
            print()
        else:
            print("Такої країни не існує!\n")

def continent_country(countries):
    with open("data.json", "r") as file:
        countries = json.load(file)
        f = False
        for cname, j in countries.items():
            if j["continent"] in ("Asia" , "Africa"):
                print(f"Країна: {cname}")
                f = True
        if not f:
            print(" Не знайдено країн Азії або Африки")

while True:
    print("\nSelect an option:")
    print("1 - View Countries")
    print("2 - Add new country")
    print("3 - Delete Country")
    print("4 - Choose Country")
    print("5 - Choose countries in Africa and Asia")
    print("0 - Exit")

    try:
        x = int(input("Your choice: "))
    except ValueError:
        print("Введіть число!")
        continue

    if x == 1:
        print_countries()

    elif x == 0:
        break
    elif x == 2:
        add_country(countries)
    elif x == 3:
        delete_country(countries)
    elif x == 4:
        choose_country(countries)
    elif x == 5:
        continent_country(countries)
    else:
        print("Функція ще не реалізована.")