import pandas as pd
import numpy as np
import sys
import os
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

total_sets = 0
winning_sets = 0
before_point = 0
arr = []

def read_pandas_file(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        return None
    
def calculate(data_frame):
    global winning_sets
    for index, row in data_frame.iterrows():
        i = int(row['my_score'])
        j = int(row['opponent_score'])
        if ((i == before_point and j < before_point) and row['win'] == True):
            winning_sets += 1
            return
        elif ((j == before_point and i < before_point) and row['win'] == False):
            winning_sets += 1
            return
    
if __name__ == "__main__":
    directory_path = '.'
    folders = [folder for folder in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, folder))] 
    x = []
    for i in range(1,26):
        x.append(i)
        before_point = i
        total_sets = 0
        winning_sets = 0
        for folder in folders:
            folder_path = os.path.join(directory_path, folder)
            csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
            for file in csv_files:
                file_path = os.path.join(folder_path, file)
                data_frame = read_pandas_file(file_path)
                if data_frame is None:
                    sys.exit(1)
                if data_frame.iloc[-1, 0] > 24 or data_frame.iloc[-1, 1] > 24:
                    total_sets += 1
                    calculate(data_frame)
        arr.append(winning_sets / total_sets)
    print("Point cutoff - " + str(before_point))
    print("Total sets - " + str(total_sets))
    print("Winning sets - " + str(winning_sets))
    print("Winning percent - " + str(winning_sets / total_sets))
    print(arr)
    
    plt.plot(x, arr)
    plt.xlabel('First to point')
    plt.ylabel('Probability to win')
    plt.grid()
    plt.show()

            
            