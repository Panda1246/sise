from helpers import *


if __name__ == "__main__":
    print("Program started...")

    #wczytanie danych pomiarowych statycznych
    (staticMeasuredCoordinates, staticReferenceCoordinates) = readData(columnNames=['data__coordinates__x', 'data__coordinates__y',
                                                   'reference__x', 'reference__y'], fileType="stat")
    #wczytanie danych pomiarowych dynamicznych

    (dynamicMeasuredCoordinates, dynamicReferenceCoordinates) = readData(columnNames=['data__coordinates__x', 'data__coordinates__y',
                                                                        'reference__x', 'reference__y'],
                                                           fileType="dynamic")

    print("Data read successfully")
    print(staticMeasuredCoordinates.values)
    print(staticReferenceCoordinates.values)
    print(staticMeasuredCoordinates.all)

    #zamiana wartości odczytanych z plików na wartości z zakresu <0, 1>
    staticMeasuredCoordinates = (staticMeasuredCoordinates.astype("fl"))