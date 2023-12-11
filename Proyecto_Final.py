import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Símbolo de BNB en Yahoo Finance
simbolo_bnb = 'BNB-USD'

# Especificar el rango de fechas para el año 2022
inicio_2022 = '2022-01-01'
fin_2022 = '2022-12-31'

# Obtener datos históricos cada semana
datos_bnb_2022 = yf.download(simbolo_bnb, start=inicio_2022, end=fin_2022, interval='1wk')

# Extraer columnas de tiempo y precio de cierre
datos_seleccionados = datos_bnb_2022[['Close']].reset_index()

# Crear la matriz de diseño
X = np.column_stack((np.ones_like(datos_seleccionados.index), datos_seleccionados.index))

# Obtener la variable dependiente
y = datos_seleccionados['Close'].values

# Calcular los coeficientes utilizando la regresión lineal matricial
theta = np.linalg.inv(X.T @ X) @ X.T @ y

# Realizar predicciones en el conjunto de datos de entrenamiento
y_pred = X @ theta

# Calcular el error cuadrático medio en el conjunto de datos de entrenamiento
mse = mean_squared_error(y, y_pred)
print(f"Error Cuadrático Medio en el Conjunto de Entrenamiento: {mse}")
# Convertir la serie a un array de numpy antes de realizar la indexación
dates_array = np.array(datos_seleccionados['Date'])

# Visualizar los resultados
plt.scatter(dates_array, y, label='Datos reales')
plt.plot(dates_array, y_pred, label='Predicciones', color='red')
plt.xlabel('Fecha')
plt.ylabel('Precio de Cierre de BNB')
plt.title('Modelo de Regresión Lineal Matricial - BNB 2022')
plt.legend()
plt.show()