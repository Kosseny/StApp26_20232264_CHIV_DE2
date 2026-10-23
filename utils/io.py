import pandas as pd
import json
from pathlib import Path

def load_data():
    df = pd.read_excel("data/resultats-par-niveau-burvot-t1-france-entiere.xlsx")
    return df

def load_geojson():

    path = Path(__file__).resolve().parent.parent / "data" / "departements.geojson"

    with open(path, "r", encoding="utf-8") as file:
        geojson = json.load(file)

    return geojson