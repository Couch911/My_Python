import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Data2.csv')
df.columns = df.columns.str.strip()
for col in df.columns:
    if "[YR" in col:
        df[col] = pd.to_numeric(df[col], errors='coerce')

years = [int(c.split()[0]) for c in df.columns if "[YR" in c]
france = df[df["Country Name"] == "France"].iloc[0]
ukraine = df[df["Country Name"] == "Ukraine"].iloc[0]

fr_values = [france[f"{y} [YR{y}]"] / 1_000_000 for y in years]
ua_values = [ukraine[f"{y} [YR{y}]"] / 1_000_000 for y in years]

plt.figure(figsize=(16, 10))
plt.plot(years, fr_values, '-o', linewidth=4, color='blue', label='France')
plt.plot(years, ua_values, '-o', linewidth=4, color='red', label='Ukraine')

plt.title("Population ", fontsize=36)
plt.xlabel("Year", fontsize=20)
plt.ylabel("Population millions", fontsize=30)
plt.grid(True)
plt.legend(fontsize=14)
plt.tight_layout()
plt.show()

print("раїни:")
countries = df["Country Name"].dropna().unique()
for c in countries:
    print(" - ", c)

print("\nВведіть дві країни для порівняння:")
c1 = input("Перша країна: ").strip()
c2 = input("Друга країна: ").strip()

if c1 not in countries or c2 not in countries:
    print("такої країни немає ")
    exit()

country1 = df[df["Country Name"] == c1].iloc[0]
country2 = df[df["Country Name"] == c2].iloc[0]

c1_values = [country1[f"{y} [YR{y}]"] / 1_000_000 for y in years]
c2_values = [country2[f"{y} [YR{y}]"] / 1_000_000 for y in years]

x = np.arange(len(years))
width = 0.35
plt.figure(figsize=(16, 10))

plt.bar(x - width/2, c1_values, width, label=c1, color='blue')
plt.bar(x + width/2, c2_values, width, label=c2, color='red')

plt.title(f"Population: {c1} vs {c2}", fontsize=30)
plt.xlabel("Year", fontsize=24)
plt.ylabel("Population millions", fontsize=25)
plt.xticks(x, years, rotation=45)

plt.legend(fontsize=14)
plt.grid(axis='y')

plt.tight_layout()
plt.show()
