import pandas as pd

df = pd.read_csv('athlete_events.csv')

subset = df.loc[:, ["Name","Team", "Year", "Medal"]]
subset2 = subset[subset["Team"] == "Chile"]

#Año con la participación más alta
subset3 = subset2["Year"].value_counts().head(1)
print("El año con la participación más alta es: ")
print("Año  Cantidad")
print(subset3)
print("\n")

#Ganadores chilenos de alguna medalla
subset4 = subset2[subset2["Medal"] != "NaN" ].dropna().loc[:, ["Name", "Medal"]]
print("Nombres de todos los ganadores chilenos de alguna medalla:")
print(subset4)
print("\n")

#Año con más medallas ganadas por Chile
subset5 = subset2[subset2["Medal"] != "NaN" ].dropna().loc[:, ["Year", "Medal"]].value_counts().head(1)
print("Año con más medallas ganadas por Chile:")
print(subset5)