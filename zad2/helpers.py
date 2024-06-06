import tensorflow as tf
import pandas as pd
from sklearn.metrics import mean_squared_error
import math
import numpy as np

'''
Funkcja odpowiedzialna za wczytanie odpowiednich danych z plików xlsx w folderze z pomiarami
Interesują nas w tym przypadku 3 kolumny - zmierzone wartości x oraz y i ich wartości referencyjne
czyli kolumny: data__coordinates__x, data__coordinates__y, reference__x, reference__y
Mamy do wyboru dwa rodzaje plików - dynamiczne i statyczne
'''
# fileType - typ czytanego pliku(static/dynamic)
# columnNames - nazwy kolumn, które chcemy z danego pliku wczytać
# sourceFolder - domyślna lokalizacja pliku z pomiarami
import glob
import re
import pandas as pd

def readData(fileType: str, columnNames: list, sourceFolder="pomiary") -> tuple[pd.DataFrame, pd.DataFrame]:
    if fileType == 'dynamic':
        all_files = glob.glob(f"{sourceFolder}/F*/*.xlsx")
        files = [f for f in all_files if not (re.search("stat", f) or re.search("random", f))]
    else:
        files = glob.glob(f"{sourceFolder}/F*/*_stat_*.xlsx")

    data = [pd.read_excel(file, header=0, usecols=columnNames) for file in files]
    data = pd.concat(data, ignore_index=True)
    data = data.dropna()

    #zczytujemy ze wszystkich plików xslx niezbędne dane: czyli zmierzone x i y oraz ich referencyjne
    #wartości, w sumie dla każdego pliku są to 4 kolumny
    measuredCoordinates = pd.concat([data[columnNames[0]], data[columnNames[1]]], axis=1)
    referenceCoordinates = pd.concat([data[columnNames[2]], data[columnNames[3]]], axis=1)

    print(f"{fileType.capitalize()} data has been successfully loaded.")
    return measuredCoordinates, referenceCoordinates


def calculate_mean_squared_err(measurement: pd.DataFrame, reference: pd.DataFrame, choice=None):
    reference = reference.values.tolist()
    mse = []
    measurement = measurement.tolist() if choice == "result" else measurement.values.tolist()
    for i in range(len(measurement)):
        value = mean_squared_error([measurement[i][0], measurement[i][1]], [
            reference[i][0], reference[i][1]])
        mse.append(math.sqrt(value))
    return np.sort(mse) * 10000