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

def extract_data(data, column_index): # Function to extract relevant data for plotting
    extracted_data = {}
    for row in data:
        difficulty = int(row[0])
        algorithm = row[2]
        if difficulty not in extracted_data: extracted_data[difficulty] = {}
        if algorithm not in extracted_data[difficulty]: extracted_data[difficulty][algorithm] = []

        extracted_data[difficulty][algorithm].append(float(row[column_index]))
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

def globalPlots():
    data = read_data('data.csv')

    # Extract relevant data for plotting
    solution_length_data = extract_data(data, 5)
    visited_states_data = extract_data(data, 6)
    processed_states_data = extract_data(data, 7)
    time_data = extract_data(data, 8)

    # typ 1
    plotType1(time_data,
                    "Średni czas znalezienia rozwiązania w zależności od głębokości",
                    "Średni czas [ms]",
                    'glob_time_vs_diff.png')
    plotType1(solution_length_data,
                    "Średnia długość rozwiązania w zależności od głębokości",
                    "Średnia długość [ruchy]",
                    'glob_sol_len_vs_diff.png')
    plotType1(visited_states_data,
                    "Średnia liczba odwiedzonych stanów w zależności od głębokości",
                    "Średni numer odwiedzonych stanów",
                    'glob_vstd_c_vs_diff.png')
    plotType1(processed_states_data,
                    "Średnia liczba przetworzonych stanów w zależności od głębokości",
                    "Średni numer przetworzonych stanów",
                    'glob_proc_c_vs_diff.png')

def main():
    globalPlots()
    
if __name__ == "__main__": main()
