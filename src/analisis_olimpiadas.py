# analisis_olimpiadas.py
# Usa cargue_datos.py para preparar los datos y genera las tablas principales
# de tasas de medalla en outputs/tablas/.

import os
from cargue_datos import cargar_datos, preparar_datos

RUTA_TABLAS = "../outputs/tablas"


def tasa_medalla(data, columna):
    tabla = data.groupby(columna, observed=True)["medalla"].agg(registros="count", medallas="sum")
    tabla["tasa_%"] = (100 * tabla["medallas"] / tabla["registros"]).round(2)
    return tabla


def main():
    os.makedirs(RUTA_TABLAS, exist_ok=True)
    atletas, regiones = cargar_datos()
    df = preparar_datos(atletas, regiones)

    for columna in ["Sex", "Season", "grupo_etario", "tiene_medidas", "grupo_participacion"]:
        tabla = tasa_medalla(df, columna)
        tabla.to_csv(f"{RUTA_TABLAS}/tasa_medalla_por_{columna}.csv")
        print(tabla, end="\n\n")


if __name__ == "__main__":
    main()
