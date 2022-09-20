import matplotlib.pyplot as plt
import pandas as pd
df =  pd.read_csv("athlete_events.csv").dropna()

totales = df.value_counts("Medal")
etiquetas = df["Medal"].value_counts().keys()

totales.plot.pie(figsize=(10,10) ,labels=etiquetas,autopct="%0.5f" )
plt.pie(totales)
plt.show()



