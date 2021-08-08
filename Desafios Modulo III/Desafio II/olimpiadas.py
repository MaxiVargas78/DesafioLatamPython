import pandas as pd

df = pd.read_csv('athlete_events.csv')

ejercicio_1 = df.shape
print(ejercicio_1)

ejercicio_2 = df["Year"].value_counts().shape
print(ejercicio_2)

ejercicio_3_1 = df["Season"].value_counts("%")
ejercicio_3_2 = df["Season"].value_counts()/len(df["Season"])
print(ejercicio_3_1)
print(ejercicio_3_2)

res = df.groupby("Year")["Team"].agg( _="min")
ejercicio_4 = res.head(1)
print("El país y año donde fue la primera olimpiada es: "+str(ejercicio_4))

res1 = df.groupby("Season") == "Winter"]["Year"].agg(_="min")
ejercicio_5 = res1.head(5)
print(ejercicio_5)




