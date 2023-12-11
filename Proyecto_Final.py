import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
# Símbolo de BNB en Yahoo Finance
simbolo_bnb = 'BNB-USD'

# Especificar el rango de fechas
inicio = '2022-01-01'
fin = '2022-12-31'

# Obtener datos históricos cada semana
datos_bnb = yf.download(simbolo_bnb, start=inicio, end=fin, interval='1wk')

# Extraer columnas de tiempo y precio de cierre
datos_seleccionados = datos_bnb[['Close']].reset_index()

# Guardar los datos en un archivo CSV
datos_seleccionados.to_csv('datos_bnb.csv', index=False)

# Mostrar los primeros registros
print(datos_seleccionados.head())