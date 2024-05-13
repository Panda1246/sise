#!/usr/bin/python3

import csv
import matplotlib.pyplot as plt
import os

def read_data(filename): # Function to read data from CSV file
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader: data.append(row)
    return data

def extract_data(data, column_index, alg=None): # Function to extract relevant data for plotting
    extracted_data = {}
    for row in data:
        difficulty = int(row[0]);
        algorithm = row[2]

        if difficulty not in extracted_data: extracted_data[difficulty] = {}

        if alg is None: # do not filter
            if algorithm not in extracted_data[difficulty]: extracted_data[difficulty][algorithm] = []
            extracted_data[difficulty][algorithm].append(float(row[column_index]))
        elif algorithm == alg: # filter
            detail = row[3]
            if detail not in extracted_data[difficulty]: extracted_data[difficulty][detail] = []
            extracted_data[difficulty][detail].append(float(row[column_index]))

    return extracted_data

# Function to create bar plots
def plotType1(data, title, ylabel, filename, isLog=True):
    details = list(data[1].keys())
    difficulty_levels = list(data.keys())
    bar_width = 0.1
    index = [level for level in range(len(difficulty_levels))]  # Adjusted to use index as x-axis position
    for i, detail in enumerate(details):
        values = [sum(data[level][detail])/len(data[level][detail]) for level in difficulty_levels]
        plt.bar(index, values, bar_width, label=detail)
        index = [x + bar_width for x in index] # needed for multiple bars
    plt.xlabel('Difficulty Level')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks([level -bar_width/2 + (bar_width*len(details)/2) for level in range(len(difficulty_levels))], difficulty_levels)
    plt.legend()
    # plt.grid(True)
    plt.tight_layout()
    # plt.figure(figsize=(10, 6))
    if isLog: plt.yscale('log')
    plt.savefig(os.path.join('pic', filename))
    plt.close()

def globalPlots(data):
    sl_data = extract_data(data, 5)
    vs_data = extract_data(data, 6)
    ps_data = extract_data(data, 7)
    t_data = extract_data(data, 8)
    
    startName = "glob"
    forName = ""
    # typ 1
    plotType1(t_data,
              "Średni czas znalezienia rozwiązania w zależności od głębokości" + forName,
              "Średni czas [ms]",
              startName + '_time_vs_diff.png')
    plotType1(sl_data,
              "Średnia długość rozwiązania w zależności od głębokości" + forName,
              "Średnia długość [ruchy]",
              startName + '_sol_len_vs_diff.png')
    plotType1(vs_data,
              "Średnia liczba odwiedzonych stanów w zależności od głębokości" + forName,
              "Średni numer odwiedzonych stanów",
              startName + '_vstd_c_vs_diff.png')
    plotType1(ps_data,
              "Średnia liczba przetworzonych stanów w zależności od głębokości" + forName,
              "Średni numer przetworzonych stanów",
              startName + '_proc_c_vs_diff.png')

def astarPlots(data):
    sl_data = extract_data(data, 5, alg="astr")
    vs_data = extract_data(data, 6, alg="astr")
    ps_data = extract_data(data, 7, alg="astr")
    t_data =  extract_data(data, 8, alg="astr")

    startName = "astr"
    # forName = "dla A*"
    forName = ""

    plotType1(t_data,
              "Średni czas znalezienia rozwiązania w zależności od głębokości" + forName,
              "Średni czas [ms]",
              startName + '_time_vs_diff.png',
              isLog=False)
    plotType1(sl_data,
              "Średnia długość rozwiązania w zależności od głębokości" + forName,
              "Średnia długość [ruchy]",
              startName + '_sol_len_vs_diff.png',
              isLog=False)
    plotType1(vs_data,
              "Średnia liczba odwiedzonych stanów w zależności od głębokości" + forName,
              "Średni numer odwiedzonych stanów",
              startName + '_vstd_c_vs_diff.png',
              isLog=False)
    plotType1(ps_data,
              "Średnia liczba przetworzonych stanów w zależności od głębokości" + forName,
              "Średni numer przetworzonych stanów",
              startName + '_proc_c_vs_diff.png',
              isLog=False)

def dbfsPlots(data):
    for dbfs in ["bfs", "dfs"]:
        sl_data = extract_data(data, 5, alg=dbfs)
        vs_data = extract_data(data, 6, alg=dbfs)
        ps_data = extract_data(data, 7, alg=dbfs)
        t_data =  extract_data(data, 8, alg=dbfs)
        
        startName = dbfs
        # forName = "dla A*"
        forName = ""
        
        plotType1(t_data,
                  "Średni czas znalezienia rozwiązania w zależności od głębokości" + forName,
                  "Średni czas [ms]",
                  startName + '_time_vs_diff.png',
                  isLog=False)
        plotType1(sl_data,
                  "Średnia długość rozwiązania w zależności od głębokości" + forName,
                  "Średnia długość [ruchy]",
                  startName + '_sol_len_vs_diff.png',
                  isLog=False)
        plotType1(vs_data,
                  "Średnia liczba odwiedzonych stanów w zależności od głębokości" + forName,
                  "Średni numer odwiedzonych stanów",
                  startName + '_vstd_c_vs_diff.png',
                  isLog= (dbfs == "bfs"))
        plotType1(ps_data,
                  "Średnia liczba przetworzonych stanów w zależności od głębokości" + forName,
                  "Średni numer przetworzonych stanów",
                  startName + '_proc_c_vs_diff.png',
                  isLog= (dbfs == "bfs"))

def main():
    data = read_data('data.csv')

    globalPlots(data)
    astarPlots(data)
    dbfsPlots(data)


if __name__ == "__main__": main()
