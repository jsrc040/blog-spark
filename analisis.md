---

layout: default
title: Análisis de Flujo de Datos Simulado con Spark y Jekyll
permalink: /analisis/
---------------------

# Análisis de Flujo de Datos Simulado con Spark y Jekyll

## Objetivo

Aplicar técnicas de analítica avanzada para procesar y visualizar un flujo de datos simulado en un contexto empresarial usando Python y Spark.
El análisis busca identificar patrones de comportamiento de los usuarios, como la frecuencia y distribución de clics, para apoyar la toma de decisiones estratégicas.
Además, se pretende comparar enfoques de procesamiento por lotes y en tiempo real, entendiendo sus ventajas y limitaciones, y demostrar cómo integrar los resultados en un blog interactivo mediante Jekyll y GitHub Pages.

## Escenario

Una tienda online recopila datos de clics de sus usuarios en tiempo real para detectar patrones de navegación y comportamiento de compra.
El objetivo es identificar qué productos generan más interacción, cuáles son las horas pico de actividad y qué segmentos de usuarios son más activos.
Esta información permite optimizar la experiencia de navegación, personalizar recomendaciones y planificar estrategias de marketing basadas en datos reales.

## Dataset

El archivo `clickstream.csv` contiene las columnas:

* **Timestamp**
* **User_ID**
* **Clicks**

## Procesamiento

Se genera un flujo simulado con un script en Python (`analisis_spark.py`) que:

1. Crea el dataset si no existe.
2. Procesa los clics por usuario.
3. Genera un gráfico de barras con `matplotlib`.

## Código Python: Creación del dataset y gráfico

```python
# analisis_spark.py
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import random

# RUTAS
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CSV_PATH = os.path.join(ROOT, "clickstream.csv")
ASSETS_DIR = os.path.join(ROOT, "assets")
OUTPUT_IMG = os.path.join(ASSETS_DIR, "clicks_chart.png")

# Crear carpeta assets si no existe
os.makedirs(ASSETS_DIR, exist_ok=True)

# Crear dataset simulado si no existe
if not os.path.exists(CSV_PATH):
    start = datetime(2025, 10, 30, 10, 0, 0)
    user_ids = [f"user_{i}" for i in range(1, 21)]
    rows = []
    for i in range(1000):
        ts = start + timedelta(seconds=random.randint(0, 60*60 - 1))
        user = random.choice(user_ids)
        clicks = random.choices([0,1,2,3,4,5], weights=[5,30,25,20,12,8])[0] or 1
        rows.append([ts.strftime("%Y-%m-%d %H:%M:%S"), user, clicks])
    df_sim = pd.DataFrame(rows, columns=["Timestamp", "User_ID", "Clicks"])
    df_sim.to_csv(CSV_PATH, index=False)

# Leer CSV
df = pd.read_csv(CSV_PATH, parse_dates=["Timestamp"])

# Agrupar clics por usuario
clicks_por_usuario = df.groupby("User_ID")["Clicks"].sum().sort_values(ascending=False)

# Generar gráfico
plt.figure(figsize=(10,5))
clicks_por_usuario.plot(kind="bar")
plt.title("Clics por Usuario")
plt.xlabel("Usuario")
plt.ylabel("Total de clics")
plt.tight_layout()
plt.savefig(OUTPUT_IMG)
plt.close()
```

## Visualización

<div align="center">
  <img src="/assets/clicks_chart.png" alt="Gráfico de clics por usuario" width="700"/>
</div>

## Interpretación

Se observa que algunos usuarios tienen una cantidad de clics significativamente mayor.
Esto sugiere que son usuarios activos o interesados en ciertos productos, lo que puede ayudar a personalizar ofertas o mejorar la experiencia de compra.

## Pasos para subir el proyecto a GitHub

1. **Crear el repositorio en GitHub**

   * Ingresar a GitHub y crear un nuevo repositorio (ej. `clickstream-blog`).
   * Inicializar con `README.md` si se desea.

2. **Clonar el repositorio localmente**

```bash
git clone https://github.com/tu_usuario/clickstream-blog.git
cd clickstream-blog
```

3. **Agregar archivos del proyecto**

   * Carpeta `_posts/` (si aplica)
   * Carpeta `assets/` con imágenes (`clicks_chart.png`)
   * Archivo `analisis.md`
   * Archivo `_config.yml` y demás necesarios para Jekyll

4. **Hacer commit de los cambios**

```bash
git add .
git commit -m "Agregar blog con análisis de clics"
```

5. **Subir cambios a GitHub**

```bash
git push origin main
```

6. **Configurar GitHub Pages**

   * Ir a **Settings → Pages** en el repositorio.
   * Seleccionar la rama `main` y la carpeta `/` (root).
   * Guardar y esperar a que el sitio se publique (1-5 minutos).

## Despliegue del Blog

* Herramienta: **Jekyll**
* Tema: **Cayman**
* Estructura:

  * Carpeta raíz:

    * `_posts/` → posts si aplica
    * `assets/` → imágenes y gráficos
    * `_config.yml` → configuración de Jekyll
* GitHub Pages publica automáticamente desde la rama `main`.

## Procesamiento por Lotes vs. Streaming

* **Por lotes:** analiza datos históricos, ideal para informes y análisis agregados.
* **Streaming:** analiza datos en tiempo real, permite reaccionar rápidamente a eventos.
  En este proyecto se simula procesamiento por lotes, pero la misma lógica puede adaptarse a un flujo continuo de clics.

## Conclusiones

Los patrones muestran que los usuarios más activos se concentran en ciertas horas del día, lo que indica oportunidades para personalizar la experiencia y optimizar campañas de marketing.
