print("Proverka")
a = float(input("Enter a number for a (a>=0): ")) # вводимо та перевіряємо а
if a < 0:
    print("a Negative")
    exit()
b = float(input("Enter a number for b (b>=0): ")) #  вводимо та перевіряємо b
if b < 0:
    print("b Negative")
    exit()
print("a =", a, "b =", b)
if a < b:
    print("X =", a/b+5)
elif a == b:
    print("X =", -5)
else :
    print("X =", (a*a-b)/b)
# перевіряємо умови та виконуємо розрахунки
                # Завдання 2
n = 8
a, b = 0, 1
suma_fibonacci = 0
for i in range(n):
    print("№",i+1,"=",a, end=" ")
    suma_fibonacci += a
    a, b = b, a + b
print("\n Sum of fibonacci (8 numbers) =", suma_fibonacci)
# Виводимо кожне число окремо та виводимо їх суму
                # Завдання 3
n = int(input("Enter a number for n (1<N<9): ")) # вводимо та перевіряємо n
if n > 8:
    print("n too big")
    exit()
elif n < 2:
    print("n too small")
    exit()
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
    # виводимо з кожним новим рядком на 1 число більше, залишаючі старі числа