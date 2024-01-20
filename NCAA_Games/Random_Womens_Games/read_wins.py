import pandas as pd
import numpy as np
import sys
import os
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

num_sets = 0

def read_pandas_file(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        return None
    
def importance_precent(s1, s2, table_data):
    if s1 >= 24 and s2 >= 24: return abs(table_data[s1, s2 - 1] - table_data[s1 - 1, s2])
    if s1 >= 25: return 1
    if s2 >= 25: return 0
    return abs(table_data[s1, s2 + 1] - table_data[s1 + 1, s2])
    
def calculate(data_frame, total_table, win_table):
    for index, row in data_frame.iterrows():
        i = int(row['my_score'])
        j = int(row['opponent_score'])
        if(i < 26 and j < 26):
            total_table[i,j] += 1
            total_table[j,i] += 1
            if row['win'] == True:
                win_table[i,j] += 1
            else:
                win_table[j,i] += 1 
    
if __name__ == "__main__":
    directory_path = '.'
    total_table = np.zeros((26, 26))
    win_table = np.zeros((26, 26))
    table_data1 = np.zeros((26, 26))
    table_data2 = np.zeros((26, 26))
    x_max = 0 
    csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]
    for file in csv_files:
        file_path = os.path.join(directory_path, file)
        data_frame = read_pandas_file(file_path)
        if data_frame is None:
            sys.exit(1)
        # print(data_frame.iloc[-1, 0])
        if data_frame.iloc[-1, 0] > 24 or data_frame.iloc[-1, 1] > 24:
            num_sets += 1
            calculate(data_frame, total_table, win_table)
    
    print('number of sets evaluated - ' + str(num_sets)) 
    for i in range(0, 26):
        for j in range(0, 26):
            if total_table[i, j] == 0:
                if(i > j):
                    table_data1[i, j] = 100
                else:
                    table_data1[i, j] = 0
            else:
                table_data1[i, j] = (win_table[i, j] / total_table[i, j]) * 100
            
    for i in range(0, 26):
        for j in range(0, 26):
            x = importance_precent(i, j, table_data1)
            if x == 100 or x == 0:
                x = 0.0001
            if x > x_max:
                x_max = x
            table_data2[i, j] = x
            
    fig, ax = plt.subplots(figsize=(11, 7))
    cmap = plt.get_cmap("RdYlBu")
    im = ax.imshow(table_data1, cmap=cmap, vmin=-20, vmax=120, aspect='auto')
    ax.set_xlabel('Opponent Score')
    ax.set_ylabel('My Score')
    ax.set_xticks(np.arange(26))
    ax.set_yticks(np.arange(26))
    ax.set_xticklabels(np.arange(26))
    ax.set_yticklabels(np.arange(26))
    ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
    ax.xaxis.set_label_position('top')
    x = np.arange(26)
    default_x_ticks = range(len(x))
    plt.xticks(default_x_ticks, x)
    for i in range(26):
        for j in range(26):
            text = ax.text(j, i, f'{table_data1[i, j]:.0f}%', ha='center', va='center', color='black', fontsize=8)
    plt.tight_layout()
    plt.show()
    # plt.savefig("simple_model_" + str(wp) + ".png")
    fig, ax = plt.subplots(figsize=(11, 7))
    cmap = plt.get_cmap("summer_r")
    im = ax.imshow(table_data2, cmap=cmap, norm=LogNorm(vmin=1, vmax=x_max), aspect='auto')
    ax.set_xlabel('Opponent Score')
    ax.set_ylabel('My Score')
    ax.set_xticks(np.arange(26))
    ax.set_yticks(np.arange(26))
    ax.set_xticklabels(np.arange(26))
    ax.set_yticklabels(np.arange(26))
    ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
    ax.xaxis.set_label_position('top')
    x = np.arange(26)
    default_x_ticks = range(len(x))
    plt.xticks(default_x_ticks, x)
    for i in range(26):
        for j in range(26):
            text = ax.text(j, i, f'{table_data2[i, j]:.0f}%', ha='center', va='center', color='black', fontsize=8)
    plt.tight_layout()
    plt.show()
    # plt.savefig("i_simple_model_" + str(wp) + ".png")
    
    # python3 read_wins.py