import pandas as pd
df = pd.read_csv('ventas.csv', sep=';')

print(df.head())
print(df.info()) 

ventas_por_producto = df.groupby('producto')['cantidad'].sum()
print(ventas_por_producto)

ventas_por_producto.to_csv("resumen_ventas.csv", sep=';', index=True, header=True)
