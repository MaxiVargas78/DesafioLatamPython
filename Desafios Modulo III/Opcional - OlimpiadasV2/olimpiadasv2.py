import pandas as pd

df = pd.read_csv('athlete_events.csv')

subset = df.loc[:, ["Name","Team", "Year", "Medal"]]