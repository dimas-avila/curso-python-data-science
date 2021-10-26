""" Python para ciencia de datos: Capítulo 1

En este script nos aseguraremos de tener todo
el setup montado, librerías, datasets, etc. y 
que lo podemos ejecutar correctamente. 
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


df = pd.read_csv("./data/avocado.csv")
# print(df.head(5))

chicago = df[ df["region"] == "Chicago" ]
# print(chicago.head(15))

chicago = chicago.set_index("Date")
chicago = chicago.sort_values(by="Date")

# print(chicago.head(15))

# Gráfico

MAX_SAMPLES = 100

precio = chicago["AveragePrice"][: MAX_SAMPLES]
cantidad = chicago["Total Volume"][: MAX_SAMPLES]

plt.plot(precio, label="Precio Medio")
plt.plot(cantidad, label="Volumen total")

plt.title("Precio de los aguacates vs tiempo")
plt.xlabel("Fecha")
plt.xticks(rotation=90)
plt.ylabel("Precio en $")
plt.legend()
plt.show()











