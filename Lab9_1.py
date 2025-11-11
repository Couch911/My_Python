import csv
import os

flag = False

try:
    with open("data.csv", "r",) as csvopen:
        reader = csv.DictReader(csvopen, delimiter=",")
        print("Country Name: GPD")
        for row in reader:
            print(row["Country Name"], ":", row["2016 [YR2016]"])

except FileNotFoundError:
    print("Файл data.csv не знайдено!")

try:
    with open("data.csv", "r") as csvopen:
        reader = csv.DictReader(csvopen, delimiter=",")
        ind = input("\nВведіть значення GDP щоб знайти країни з більшим показником: ")

        while not ind.replace(".", "", 1).isdigit():
            ind = input("Введіть значення ще раз : ")

        ind = float(ind)
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Країни з більшим GDP за", ind, ":")

        with open("new_lab9.csv", "w", newline="") as csvopen2:
            writer = csv.writer(csvopen2, delimiter=",")
            writer.writerow(["Country Name", "2016 [YR2016]"])  # заголовок

            for row in reader:
                try:
                    if row["2016 [YR2016]"] and float(row["2016 [YR2016]"]) > ind:
                        flag = True
                        print(row["Country Name"], ":", row["2016 [YR2016]"])
                        writer.writerow([row["Country Name"], row["2016 [YR2016]"]])
                except ValueError:
                    continue

        if not flag:
            print(" Показників, більших за", ind, "не знайдено.")

except FileNotFoundError:
    print("Файл data.csv не знайдено!")
