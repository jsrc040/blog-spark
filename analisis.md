---
layout: default
title: Análisis de Flujo de Datos Simulado con Spark y Jekyll
permalink: /analisis/
---

# Análisis de Flujo de Datos Simulado con Spark y Jekyll

## Objetivo
Aplicar técnicas de analítica avanzada para procesar y visualizar un flujo de datos simulado en un contexto empresarial usando Python y Spark.  
El análisis busca identificar patrones de comportamiento de los usuarios, como la frecuencia y distribución de clics, para apoyar la toma de decisiones estratégicas.  
Además, se pretende comparar enfoques de procesamiento por lotes y en tiempo real, entendiendo sus ventajas y limitaciones, y demostrar cómo integrar los resultados en un blog interactivo mediante Jekyll y GitHub Pages.

##codigo python para creacion de la grafica e importacion de dataset
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

## Escenario
Una tienda online recopila datos de clics de sus usuarios en tiempo real para detectar patrones de navegación y comportamiento de compra.  
El objetivo es identificar qué productos generan más interacción, cuáles son las horas pico de actividad y qué segmentos de usuarios son más activos.  
Esta información permite optimizar la experiencia de navegación, personalizar recomendaciones y planificar estrategias de marketing basadas en datos reales.

#codigo implementado en python para la creacion de la grafica 
## Dataset
El archivo `clickstream.csv` contiene las columnas:
- **Timestamp**  
- **User_ID**  
- **Clicks**

## Procesamiento
Se genera un flujo simulado con un script en Python (`analisis_spark.py`) que:
1. Crea el dataset si no existe.  
2. Procesa los clics por usuario.  
3. Genera un gráfico de barras con `matplotlib`.

## Visualización

<div align="center">
  <img src="/assets/clicks_chart.png" alt="Gráfico de clics por usuario" width="700"/>
</div>
## Pasos para subir el proyecto a GitHub

1. **Crear el repositorio en GitHub**  
   - Ingresar a GitHub y crear un nuevo repositorio (ej. `clickstream-blog`).
   - Inicializarlo con un `README.md` si se desea.

2. **Clonar el repositorio localmente**  
```bash
git clone https://github.com/tu_usuario/clickstream-blog.git
cd clickstream-blog

## Interpretación
Se observa que algunos usuarios tienen una cantidad de clics significativamente mayor.  
Esto sugiere que son usuarios activos o interesados en ciertos productos, lo que puede ayudar a personalizar ofertas o mejorar la experiencia de compra.

## Despliegue del Blog
- Herramienta: **Jekyll**  
- Tema: **Cayman**  
- Estructura:
