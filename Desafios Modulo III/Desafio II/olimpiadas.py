import pandas as pd

df = pd.read_csv('athlete_events.csv')

ejercicio_1 = df.shape
print("#EJERCICIO 1:")
print(ejercicio_1)
print("\n")

ejercicio_2 = df["Year"].value_counts().shape
print("#EJERCICIO 2:")
print(ejercicio_2)
print("\n")

ejercicio_3_1 = df["Season"].value_counts("%")
ejercicio_3_2 = df["Season"].value_counts()/len(df["Season"])
print("#EJERCICIO 3:")
print(ejercicio_3_1)
print(ejercicio_3_2)
print("\n")

subset = df.loc[:, ["Season", "City", "Year"]] #slice son para seleccionar posiciones desde/hasta de columnas
subset2 = subset[subset["Season"] == "Summer"]
subset3 = subset2[subset2["Year"] == subset2["Year"].min()]
ejercicio_4 = subset3.head(1)
print("#EJERCICIO 4:")
print(ejercicio_4)
print("\n")

subset = df.loc[:, ["Season", "City", "Year"]]
subset2 = subset[subset["Season"] == "Winter"]
subset3 = subset2[subset2["Year"] == subset2["Year"].min()]
ejercicio_5 = subset3.head(1)
print("#EJERCICIO 5:")
print(ejercicio_5)
print("\n")

subset = df.loc[:, ["Name" , "Team"]]
subset2 = subset["Team"].value_counts()
ejercicio_6 = subset2.head(10)
print("#EJERCICIO 6:")
print(ejercicio_6)
print("\n")

subset = df.loc[:, "Medal"]
ejercicio_7 = subset.value_counts("%")
print("#EJERCICIO 7:")
print(ejercicio_7)
print("\n")

subset = df.loc[:, ["Year", "Team"]]
subset2 = subset[subset["Year"] == subset["Year"].min()]
ejercicio_8 = subset2["Team"].unique()
print("#EJERCICIO_8:")
for x in ejercicio_8:
    print(x)
print("\n")
