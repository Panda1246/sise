import pandas as pd
import tensorflow as tf
import numpy as np
import re
import math
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from glob import glob
from keras.src.callbacks import EarlyStopping

'''
Funkcja odpowiedzialna za wczytanie odpowiednich danych z plików xlsx w folderze z pomiarami
Interesują nas w tym przypadku 3 kolumny - zmierzone wartości x oraz y i ich wartości referencyjne
czyli kolumny: data__coordinates__x, data__coordinates__y, reference__x, reference__y
Mamy do wyboru dwa rodzaje plików - dynamiczne i statyczne
'''
# fileType - typ czytanego pliku(static/dynamic)
# columnNames - nazwy kolumn, które chcemy z danego pliku wczytać
# sourceFolder - domyślna lokalizacja pliku z pomiarami


def readData(fileType: str, columnNames: list, sourceFolder="pomiary") -> tuple[pd.DataFrame, pd.DataFrame]:
    # REVIEW(242336): można by tu zamiast stringa przekazywać flagę (bool) dynamic
    if fileType == 'dynamic':
        all_files = glob(f"{sourceFolder}/F*/*.xlsx")
        files = [f for f in all_files if not (re.search("stat", f) or re.search("random", f))]
    else:
        files = glob(f"{sourceFolder}/F*/*_stat_*.xlsx")

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
def switch_all_nan_for_0(measurement: pd.DataFrame, reference: pd.DataFrame, dynamic_measurement: pd.DataFrame, dynamic_reference: pd.DataFrame):
    measurement.fillna(0, inplace=True)
    reference.fillna(0, inplace=True)
    dynamic_measurement.fillna(0, inplace=True)
    dynamic_reference.fillna(0, inplace=True)
    return measurement, reference, dynamic_measurement, dynamic_reference

def normalizing_data(measurement: pd.DataFrame, reference: pd.DataFrame, dynamic_measurement: pd.DataFrame, dynamic_reference: pd.DataFrame):
    measurement = (measurement.astype('float32')) / 10000
    reference = (reference.astype('float32')) / 10000
    dynamic_measurement = (dynamic_measurement.astype('float32')) / 10000
    dynamic_reference = (dynamic_reference.astype('float32')) / 10000
    return measurement, reference, dynamic_measurement, dynamic_reference

def creating_neuron_network():
    network = tf.keras.models.Sequential()
    network.add(tf.keras.layers.Dense(10, activation='relu'))
    network.add(tf.keras.layers.Dense(5, activation='elu'))
    network.add(tf.keras.layers.Dense(2, activation='selu'))
    return network

def early_stopping():
    return EarlyStopping(monitor='loss', patience=3, min_delta=0.0000001, verbose=1)

def prediction_and_error(network, dynamic_measurement, dynamic_reference):
    prediction = network.predict(dynamic_measurement)
    error_mlp = calculate_mean_squared_err(prediction, dynamic_reference,
                                           choice="result")
    error_meas = calculate_mean_squared_err(dynamic_measurement, dynamic_reference)
    return error_mlp, error_meas

def save_to_xlsx(error_mlp):
    error_mlp = pd.DataFrame(error_mlp)
    error_mlp.to_excel("dis_error.xlsx", engine='xlsxwriter')
def draw_plot(error_mlp, error_meas):
    for errors, label in zip([error_mlp, error_meas], ["Dane filtrowane", "Dane niefiltrowane"]):
        x = 1. * np.arange(len(errors)) / (len(errors) - 1)
        plt.plot(errors, x, label=label)
    plt.legend()
    plt.xlim(0, 2000)
    plt.ylim(0, 1)
    plt.savefig("dis_error.jpg")
    plt.show()
