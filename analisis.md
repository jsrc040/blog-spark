---
layout: default
title: Análisis de Flujo de Datos Simulado con Spark y Jekyll
permalink: /analisis/
---

# Análisis de Flujo de Datos Simulado con Spark y Jekyll

## Objetivo
Aplicar analítica avanzada para procesar un flujo de datos simulado en un contexto empresarial usando Python y Spark.

## Escenario
Una tienda online analiza clics en tiempo real para detectar patrones de navegación.

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

## Interpretación
Se observa que algunos usuarios tienen una cantidad de clics significativamente mayor.  
Esto sugiere que son usuarios activos o interesados en ciertos productos, lo que puede ayudar a personalizar ofertas o mejorar la experiencia de compra.

## Despliegue del Blog
- Herramienta: **Jekyll**  
- Tema: **Cayman**  
- Estructura:
