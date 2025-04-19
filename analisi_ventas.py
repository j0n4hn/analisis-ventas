import pandas as pd
import os

# Verifica el directorio actual y los archivos
print("📁 Directorio actual:", os.getcwd())
print("📄 Archivos en el directorio:", os.listdir())

# Cargar el CSV
try:
    df = pd.read_csv('ventas.csv')  # Si los valores están separados por comas
    print("✅ Archivo 'ventas.csv' cargado correctamente.")
except Exception as e:
    print("❌ Error al leer ventas.csv:", e)
    exit()

# Eliminar espacios al inicio y fin de los nombres de las columnas
df.columns = df.columns.str.strip()

# Mostrar las primeras filas del DataFrame y su información
print("\n🔍 Primeras filas del DataFrame:")
print(df.head())

print("\n🧠 Información general del DataFrame:")
print(df.info())

# Mostrar tipo de datos del objeto ventas_por_producto
try:
    ventas_por_producto = df.groupby('Producto', as_index=False)['Cantidad'].sum()
    print("\n📐 Tipo de datos del resumen:", type(ventas_por_producto))
    print("\n🧾 Contenido del resumen:")
    print(ventas_por_producto.head())
    print("📌 Columnas:", ventas_por_producto.columns)

    # Guardar el DataFrame a un archivo CSV
    ventas_por_producto.to_csv("resumen_ventas.csv", sep=';', index=False, header=True)
    print("\n✅ Archivo 'resumen_ventas.csv' creado exitosamente.")
except Exception as e:
    print("❌ Error al procesar o guardar el resumen:", e)
