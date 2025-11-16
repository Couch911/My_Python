import json
import numpy as np
import matplotlib.pyplot as plt
filename = "data.json"
try:
    with open("data.json", "r") as f:
        data = json.load(f)
    print(f"Файл {filename} відкрито")
except FileNotFoundError:
    print(f"Файл {filename} не існує")

countries = list(data.keys())
populations = [data[c]["population"] for c in countries]
colors = plt.cm.tab20(np.linspace(0, 1, len(countries)))

def func(pct):
    return f"{pct:.1f}%"

fig, ax = plt.subplots(figsize=(14, 8))

wedges, texts, autotexts = ax.pie(
    populations,
    autopct=lambda pct: func(pct),
    textprops=dict(color="white"),
    startangle=90,
    colors=colors,
    wedgeprops=dict(width=0.6)
)

ax.legend(
    wedges,
    countries,
    title="Countries",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1)
)

plt.setp(autotexts, size=7, weight="bold")
ax.set_title("Population by country", fontsize=20)
plt.tight_layout()
plt.show()
