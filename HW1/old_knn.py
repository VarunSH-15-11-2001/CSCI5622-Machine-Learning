import pandas as pd
import math
from collections import Counter
# import time as t
from tqdm import tqdm 

data = pd.read_csv('Breast_Cancer.csv')



def compute_distances(point1, point2):
    """
        Age, survival months, regional node positive, regional node examined and Tumor size
        are the continuous variables. Euclidean distance is used for measuring similarity 
        between these variables.

        Race, Marital Status, T Stage, N Stage, 6th Stage, Defferentiated, Grade, A Stage, 
        Estrogen Status, Progesterone Status are the categorical values. Hamming distance 
        is used for measuring the similarity across these variables.
    """
    euclidean_distance = math.sqrt(
        (point1['Age'] - point2['Age'] ) **2+
        (point1['Tumor Size'] - point2['Tumor Size'] ) **2+
        (point1['Regional Node Examined'] - point2['Regional Node Examined']) **2+
        (point1['Regional Node Positive'] - point2['Regional Node Positive'] ) **2+
        (point1['Survival Months'] - point2['Survival Months'])**2
    )

    # print("ed: ", euclidean_distance)

    

    hamming_distance = (
        (0 if point1['Race']==point2['Race'] else 1) + 
        (0 if point1['Marital Status']==point2['Marital Status'] else 1) +
        (0 if point1['T Stage']==point2['T Stage'] else 1) +
        (0 if point1['N Stage']==point2['N Stage'] else 1) +
        (0 if point1['6th Stage']==point2['6th Stage'] else 1) +
        (0 if point1['differentiate']==point2['differentiate'] else 1) +
        (0 if point1['Grade']==point2['Grade'] else 1) +
        (0 if point1['A Stage']==point2['A Stage'] else 1) +
        (0 if point1['Estrogen Status']==point2['Estrogen Status'] else 1) +
        (0 if point1['Progesterone Status']==point2['Progesterone Status'] else 1) 
    )
    
    
    # print("hd: ", hamming_distance)
    return euclidean_distance + hamming_distance
    
    

def split_dataset(data):
    totalRows = data.shape[0] - 1

    """
        split data into train, validation and testing sets : 75-15-15% each
        find the total size of the dataset and *0.75, .15, .15
    """

    train_boundary = math.floor(0.70*totalRows)
    val_boundary = train_boundary + math.ceil(0.15*totalRows)
    test_boundary = val_boundary + math.ceil(0.15*totalRows)

    train_data = data.iloc[:train_boundary]
    val_data = data.iloc[train_boundary:val_boundary]
    test_data = data.iloc[val_boundary:test_boundary]

    train_Y = train_data['Status']
    train_X = train_data.drop(['Status'], axis=1)

    val_Y = val_data['Status']
    val_X = val_data.drop(['Status'], axis=1)


    test_Y = test_data['Status']
    test_X = test_data.drop(['Status'], axis=1)

    # print(train_X.shape[0])
    # print(val_X.shape[0])

    return train_X, train_Y, val_X, val_Y, test_X, test_Y



def parameter_tuning_knn(data, k):
    
    train_X, train_Y, val_X, val_Y, test_X, test_Y = split_dataset(data=data)

    print(val_X)
    print(val_Y)

    val_pred = {}
    point_distance_map = {}

    point_point_map = {}

    for val_index in tqdm(range(list(val_X.shape)[0])):

        """
            for every point in the validation dataset, find the k nearest neighbours by computing distances,
            map and store distances to its training point, sort the map, and look at the first k points.
        """


        # print("Iterating at val_point: ", val_index)

        for train_index in range(list(train_X.shape)[0]):
            # print("Iterating at train_point: ", train_index)
            distance_list=[]
            point_list=[]
            # print(val_index, train_index)
            distance = compute_distances(val_X.iloc[val_index], train_X.iloc[train_index])
            point_distance_map[train_index] = distance
        



    
        sorted_distances_point_map = dict(sorted(point_distance_map.items(), key=lambda item: item[1]))
        
        """
            while looking at the first k points, find the most occuring 'Status' value among them, using
            train_Y and report it as the output for that val_point
        """


        counter = 0
        output = []
        for pair in sorted_distances_point_map.items():
            if(counter>=k): break                           # already found K neighbours
            # print(pair)
            point_number, distance = pair
            output.append(train_Y.iloc[point_number])
            # print(train_Y.iloc[point_number])
            counter+=1
        
        pred_status, trash = Counter(output).most_common()[0]
        # print(pred_status)
        val_pred[val_index]=pred_status

    correct_predictions = 0
    for pair in val_pred.items():
        point, status = pair
        
        



        
        
parameter_tuning_knn(data, 3)

    
    


"""
    code to test working of distance computation

    distance = compute_distances(data.iloc[1], data.iloc[0])
    print(data.iloc[1])
    print(data.iloc[0])
    print(distance)
"""