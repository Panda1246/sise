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

    staticMeasuredCoordinates, staticReferenceCoordinates, dynamicMeasuredCoordinates, dynamicReferenceCoordinates = switch_all_nan_for_0(staticMeasuredCoordinates, staticReferenceCoordinates, dynamicMeasuredCoordinates, dynamicReferenceCoordinates)
    staticMeasuredCoordinates, staticReferenceCoordinates, dynamicMeasuredCoordinates, dynamicReferenceCoordinates = normalizing_data(staticMeasuredCoordinates, staticReferenceCoordinates, dynamicMeasuredCoordinates, dynamicReferenceCoordinates)
    network = creating_neuron_network()

    # KOMPILACJA SIECI PRZY POMOCY OPTYMALIZATORA "ADAM"
    network.compile(optimizer=tf.keras.optimizers.Adam(),
                    loss=tf.keras.losses.MeanSquaredError(),
                    metrics=['accuracy'])
    early_stop = early_stopping()

    network.fit(staticMeasuredCoordinates, staticReferenceCoordinates, epochs=100, verbose=1, callbacks=[early_stop])

    # WYPRINTOWANIE WAG NEURONÓW
    print("\nWAGI:\n")
    for x in range(0, 3):
        print("\nWarstwa nr ", x + 1, "\n")
        print(network.layers[x].get_weights()[0])

    error_mlp, error_mld = prediction_and_error(network, dynamicMeasuredCoordinates, dynamicReferenceCoordinates)

    save_to_xlsx(error_mlp)


    #NARYSUJ WYKRES
    draw_plot(error_mlp, error_mld)



    #zamiana wartości odczytanych z plików na wartości z zakresu <0, 1>
    #staticMeasuredCoordinates = (staticMeasuredCoordinates.astype("fl"))