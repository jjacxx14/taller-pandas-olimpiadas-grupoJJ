# Taller Pandas: 120 años de historia olímpica

Proyecto colaborativo del curso **Programación II (Ciencia de Datos)**. Analizamos los registros de atletas de los Juegos Olímpicos entre 1896 y 2016 con Pandas para entender quiénes participan, cómo cambió la participación en el tiempo, qué información falta y qué características se asocian con ganar una medalla.

## Integrantes y roles

| Integrante | Rol |
|---|---|
| Jacobo Beltrán | Líder de Datos, Líder de Repositorio y Líder de Reporte |

El grupo tiene un solo integrante, así que asumí los tres roles: limpieza y análisis de los datos, manejo de ramas, pull requests y conflictos, y redacción del informe, el README y la carpeta docs/.

## Objetivos

- Cargar los dos datasets de Kaggle, entender qué representa cada variable y compararlos usando la variable NOC.
- Crear nuevas variables (IMC, medalla, grupo etario, número de pruebas) y unir los datos por país.
- Revisar los datos faltantes y qué tan representativos son los datos de toda la historia olímpica.
- Responder preguntas con agrupaciones y tasas, y presentar los hallazgos con gráficos.
- Practicar el trabajo en equipo con GitHub Desktop: ramas, commits, pull requests, revisiones y conflictos.

## Cómo ejecutar el proyecto

1. Clonar el repositorio con GitHub Desktop.
2. Descargar los datos siguiendo las instrucciones de [`data/README.md`](data/README.md) y guardarlos en la carpeta `data/`.
3. Instalar las librerías: `pip install -r requirements.txt`
4. Abrir `notebooks/proyecto_olimpiadas.ipynb` en Jupyter y ejecutar todas las celdas en orden.
5. Opcional: desde la carpeta `src/`, ejecutar `python analisis_olimpiadas.py` para regenerar las tablas principales.

## Estructura del proyecto

```
taller-pandas-olimpiadas-grupoX/
├── README.md            # Presentación del proyecto
├── .gitignore           # Archivos y carpetas a ignorar (incluye los CSV de data/)
├── requirements.txt     # Librerías necesarias
├── data/
│   └── README.md        # Instrucciones de descarga (los CSV no se suben)
├── notebooks/
│   └── proyecto_olimpiadas.ipynb   # Análisis completo de los 14 puntos
├── src/
│   ├── cargue_datos.py           # Carga, fusión y creación de variables
│   └── analisis_olimpiadas.py    # Genera las tablas principales
├── outputs/
│   ├── tablas/          # Resultados en CSV
│   └── graficos/        # Gráficos en PNG
└── docs/
    └── informe_final.pdf   # Informe con hallazgos, conclusiones y proceso colaborativo
```

## Fuente de los datos

[120 years of Olympic history: athletes and results](https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results) (Kaggle).
