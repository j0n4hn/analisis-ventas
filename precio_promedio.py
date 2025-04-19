import pandas as pd
df = pd.read_csv('ventas.csv', sep=',')  # Cambia el separador según tu archivo

# Filtrar los productos cuyo precio unitario sea mayor a 99
productos_filtrados = df[df['PrecioUnitario'] > 99]

# Calcular el precio promedio de los productos filtrados
precio_promedio_filtrado = productos_filtrados['PrecioUnitario'].mean()

# Mostrar el precio promedio de los productos con precio unitario mayor a 99
print(f"\nEl precio promedio de los productos con costo unitario mayor a 99 es: {precio_promedio_filtrado}")
