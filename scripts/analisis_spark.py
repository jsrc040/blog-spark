# analisis_spark.py
# Crea un CSV simulado (si falta), calcula clics por usuario y guarda un gráfico en ../assets/clicks_chart.png

import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import random

# RUTAS (relativas a la carpeta scripts/)
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CSV_PATH = os.path.join(ROOT, "clickstream.csv")     # clickstream.csv en la raíz del proyecto
ASSETS_DIR = os.path.join(ROOT, "assets")
OUTPUT_IMG = os.path.join(ASSETS_DIR, "clicks_chart.png")

# 0) Asegurarse que exista assets/
os.makedirs(ASSETS_DIR, exist_ok=True)

# 1) Generar dataset simulado si no existe
if not os.path.exists(CSV_PATH):
    print("No se encontró clickstream.csv — creando dataset simulado...")
    start = datetime(2025, 10, 30, 10, 0, 0)
    user_ids = [f"user_{i}" for i in range(1, 21)]  # 20 usuarios
    rows = []
    for i in range(1000):  # 1.000 filas
        ts = start + timedelta(seconds=random.randint(0, 60*60 - 1))  # dentro de 1 hora
        user = random.choice(user_ids)
        clicks = random.choices([0,1,2,3,4,5], weights=[5,30,25,20,12,8])[0]
        if clicks == 0:
            clicks = 1
        rows.append([ts.strftime("%Y-%m-%d %H:%M:%S"), user, clicks])
    df_sim = pd.DataFrame(rows, columns=["Timestamp", "User_ID", "Clicks"])
    df_sim.to_csv(CSV_PATH, index=False)
    print(f"Dataset creado en: {CSV_PATH}")

# 2) Leer CSV con pandas
print("Leyendo dataset...")
df = pd.read_csv(CSV_PATH, parse_dates=["Timestamp"])

# Mostrar una vista rápida (opcional)
print("\nPrimeras 5 filas del CSV:")
print(df.head().to_string(index=False))

# 3) Agrupar: total de clics por usuario
clicks_por_usuario = df.groupby("User_ID")["Clicks"].sum().sort_values(ascending=False)

print("\nTop 5 usuarios por clics:")
print(clicks_por_usuario.head(5).to_string())

# 4) Graficar y guardar
print("\nGenerando gráfico...")
plt.figure(figsize=(10,5))
clicks_por_usuario.plot(kind="bar")
plt.title("Clics por Usuario")
plt.xlabel("Usuario")
plt.ylabel("Total de clics")
plt.tight_layout()
plt.savefig(OUTPUT_IMG)
plt.close()
print(f"Gráfico guardado en: {OUTPUT_IMG}")

print("\nHecho. Ahora arranca Jekyll y revisa la página (http://127.0.0.1:4000/analisis).")
