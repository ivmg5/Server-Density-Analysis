### README.md

---

## ANÁLISIS DE LA DENSIDAD DE SERVIDORES POR PAÍS A LO LARGO DEL TIEMPO

### ÍNDICE

1. **INTRODUCCIÓN**
2. **OBJETIVOS**
3. **METODOLOGÍA**
4. **RESULTADOS**
5. **CONCLUSIONES**

### INTRODUCCIÓN

La **densidad de servidores por cada 1,000,000 de habitantes** es una métrica empleada para entender la infraestructura de tecnología de la información en una región o país específico. Se calcula tomando el número total de servidores en un área geográfica y dividiéndolo por la población de esa zona, siendo expresada por cada millón de habitantes.

Una alta densidad de servidores indica el nivel de acceso a tecnologías de la información en una región, siendo fundamental para las políticas de inversión en infraestructura tecnológica y entendiendo su impacto en el desarrollo económico y social.

### OBJETIVO

El principal objetivo de este proyecto es **analizar la densidad de servidores a nivel mundial**, poniendo especial énfasis en **México** y la **Unión Europea**. El fin es identificar tendencias, hacer comparaciones y detectar patrones que puedan tener connotaciones estratégicas o políticas.

### METODOLOGÍA

- **Herramientas utilizadas:**
  - **Python:** Lenguaje de programación para el análisis de datos.
  - **Pandas:** Biblioteca de Python para manipulación y análisis de datos.
  - **Matplotlib:** Biblioteca de Python para generación de gráficos.
  - **Seaborn:** Biblioteca de visualización de datos en Python basada en Matplotlib.

- **Descripción del conjunto de datos:**
  - **Número de filas:** 3468
  - **Número de columnas:** 4
  - **Periodo de tiempo:** 2001 - 2016
  - **Variables:** 
    - Country Name: Nombre del país.
    - Country Code: Código del país.
    - Year: Año de recopilación de datos.
    - Value: Valor de la densidad de servidores.
  - **Resumen Estadístico:** 
    - Mínimo valor de densidad: 0.007193
    - Valor del primer cuartil (25%): 1.884437
    - Mediana (50%): 16.991548
    - Valor del tercer cuartil (75%): 143.011983
    - Máximo valor de densidad: 12034.126628.

### CÓMO EJECUTAR EL PROYECTO

1. Asegúrese de tener Python instalado en su máquina.
2. Instale las bibliotecas necesarias: 
```
pip install pandas matplotlib seaborn scipy
```
3. Clone el repositorio a su máquina local.
4. Navegue hasta la carpeta del proyecto.
5. Asegúrese de que el archivo "data.csv" esté presente en la misma carpeta que el script.
6. Ejecute el script principal usando `python main.py` (o el nombre que tenga el archivo principal).

### INTERPRETACIÓN DE RESULTADOS

Una vez ejecutado el script, se generará una serie de gráficos con diferentes enfoques:

1. **Cambio en la Densidad de Servidores en México vs. Promedio Mundial:** Este gráfico muestra la tendencia de la densidad de servidores en México en comparación con el promedio mundial a lo largo del tiempo.

2. **Top 10 Países por Densidad de Servidores:** Presenta los 10 países con mayor densidad de servidores en el último año registrado.

3. **Distribución de la Densidad de Servidores entre British Virgin Islands, Liechtenstein y Gibraltar:** Gráfico de pastel que muestra la comparación entre estas tres regiones en el último año registrado.

4. **Mapa de Calor de la Densidad de Servidores en la Unión Europea:** Un mapa de calor que visualiza la densidad de servidores en la Unión Europea a lo largo del tiempo.

5. **Comparación de la Densidad de Servidores entre América Latina & Caribe y Europa & Asia Central:** Un scatterplot que compara estas dos regiones. También se incluye una línea de regresión lineal para identificar tendencias y el coeficiente de determinación R^2 para cuantificar la relación lineal entre las dos regiones.

Cada gráfico proporcionará una visión clara sobre las tendencias, comparaciones y patrones en la densidad de servidores de diferentes regiones a lo largo del tiempo.
