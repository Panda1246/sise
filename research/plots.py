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
def plotType1(data, title, ylabel, filename):
    algorithms = list(data[1].keys())
    difficulty_levels = list(data.keys())
    bar_width = 0.35
    index = [level for level in range(len(difficulty_levels))]  # Adjusted to use index as x-axis position
    plt.figure(figsize=(10, 6))
    for i, algorithm in enumerate(algorithms):
        values = [sum(data[level][algorithm])/len(data[level][algorithm]) for level in difficulty_levels]
        plt.bar(index, values, bar_width, label=algorithm)
        index = [x + bar_width for x in index]
    plt.xlabel('Difficulty Level')
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks([level + bar_width for level in range(len(difficulty_levels))], difficulty_levels)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.yscale('log') # dla BFSa
    plt.savefig(os.path.join('pic', filename))
    plt.close()

# Main function

def globalPlots(data):
    # Extract relevant data for plotting
    sl_data = extract_data(data, 5)
    vs_data = extract_data(data, 6)
    ps_data = extract_data(data, 7)
    t_data = extract_data(data, 8)

    # typ 1
    plotType1(t_data,
                    "Średni czas znalezienia rozwiązania w zależności od głębokości",
                    "Średni czas [ms]",
                    'glob_time_vs_diff.png')
    plotType1(sl_data,
                    "Średnia długość rozwiązania w zależności od głębokości",
                    "Średnia długość [ruchy]",
                    'glob_sol_len_vs_diff.png')
    plotType1(vs_data,
                    "Średnia liczba odwiedzonych stanów w zależności od głębokości",
                    "Średni numer odwiedzonych stanów",
                    'glob_vstd_c_vs_diff.png')
    plotType1(ps_data,
                    "Średnia liczba przetworzonych stanów w zależności od głębokości",
                    "Średni numer przetworzonych stanów",
                    'glob_proc_c_vs_diff.png')
def astarPlots(data):
    sl_data = extract_data(data, 5, alg="astr")
    vs_data = extract_data(data, 6, alg="astr")
    ps_data = extract_data(data, 7, alg="astr")
    t_data =  extract_data(data, 8, alg="astr")

    pass # TODO: implement this

def dbfsPlots(data):
    pass # TODO: implement this
    
def main():
    data = read_data('data.csv')

    globalPlots(data)
    astarPlots(data)
    dbfsPlots(data)


if __name__ == "__main__": main()
