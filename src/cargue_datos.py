# cargue_datos.py
# Carga los archivos de Kaggle, une atletas con regiones por NOC y crea las
# variables nuevas del taller: IMC, medalla, grupo_etario, tiene_medidas,
# n_pruebas y grupo_participacion.

import numpy as np
import pandas as pd

RUTA_DATOS = "../data"


def cargar_datos(ruta=RUTA_DATOS):
    atletas = pd.read_csv(f"{ruta}/athlete_events.csv")
    regiones = pd.read_csv(f"{ruta}/noc_regions.csv")
    return atletas, regiones


def preparar_datos(atletas, regiones):
    df = atletas.merge(regiones, on="NOC", how="left")
    df.loc[df["NOC"] == "SGP", "region"] = "Singapore"

    df["IMC"] = df["Weight"] / (df["Height"] / 100) ** 2
    df["Medal"] = df["Medal"].fillna("Sin medalla")
    df["medalla"] = (df["Medal"] != "Sin medalla").astype(int)

    df["grupo_etario"] = pd.cut(df["Age"], bins=[0, 17, 34, np.inf],
                                labels=["Menores", "Jóvenes adultos", "Mayores"])
    df["grupo_etario"] = df["grupo_etario"].cat.add_categories("Sin edad").fillna("Sin edad")
    df["tiene_medidas"] = np.where(df["Height"].notna() & df["Weight"].notna(),
                                   "Con estatura y peso", "Sin estatura o peso")

    df["n_pruebas"] = df.groupby(["ID", "Games"])["Event"].transform("count")
    df["grupo_participacion"] = pd.cut(df["n_pruebas"], bins=[0, 1, 3, np.inf],
                                       labels=["Grupo 1 (1 prueba)", "Grupo 2 (2-3)", "Grupo 3 (4+)"])
    return df


if __name__ == "__main__":
    atletas, regiones = cargar_datos()
    df = preparar_datos(atletas, regiones)
    print(df.shape)
    print(df.head())
