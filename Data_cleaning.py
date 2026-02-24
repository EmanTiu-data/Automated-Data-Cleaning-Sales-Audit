import pandas as pd
import numpy as np

data = {
    'Fecha': ['2026-01-01', '02/01/2026', '2026.01.03', '2026-01-01', np.nan],
    'Producto': [' Laptop ', 'smartphone', 'LAPTOP', ' Tablet', 'SmartPhone'],
    'Precio': ['$1200', '800 USD', '1200', '  450 ', '900'],
    'Cantidad': [1, 2, 1, 3, np.nan],
    'Email_Cliente': ['ema@mail.com', 'JUAN@MAIL.COM', 'ema@mail.com', 'luis@mail.com', '  ']
}

df_sucio = pd.DataFrame(data)
df_sucio.to_csv('ventas_sucias.csv', index=False)


df = pd.read_csv('ventas_sucias.csv')
df['Fecha'] = pd.to_datetime(df['Fecha'], errors='coerce')
df['Producto'] = df['Producto'].str.strip().str.capitalize()
df['Precio'] = df['Precio'].replace({r'\$': '', 'USD': '', ' ': ''}, regex=True).astype(float)
df = df.drop_duplicates()
df['Cantidad'] = df['Cantidad'].fillna(1)
df = df.dropna(subset=['Fecha'])
total_ventas = df['Precio'].sum()
cantidad_items = df['Cantidad'].sum()
ticket_promedio = df['Precio'].mean()
filas_originales = 5 
filas_finales = len(df)
print(f'Filas eliminadas:{filas_originales - filas_finales}')
print(f'Ingresos totales: {total_ventas}')
print(f'Unidades vendidas: {cantidad_items}')
print(f'Valor promdio por venta: ${ticket_promedio:,.2f}')