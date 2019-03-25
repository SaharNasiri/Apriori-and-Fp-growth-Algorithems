# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 18:55:55 2019

@author: sahar
"""

import pandas as pd
from itertools import combinations 
import operator
import time


start = time.time()

data = pd.read_csv('data_discretization.csv')
data = data.drop(['Unnamed: 0'], axis=1)
min_support=int(input("Enter the minimum support: "))

D = {}
for i in range(data.shape[0]):
    D[i] = []
trues = []    
for items in data:
    trues = data[items].notnull()
    for i in range(len(trues)):
        if trues[i] == True:
            D[i].append(items)
            
values = []
for i in D.values():
    for j in i:
        values.append(j)
values = set(values)
C1 = set(combinations(values, 1))

sup_dic = []
for i in C1:
    counter = 0
    for j in D:
        if i[0] in D[j]:
            counter += 1
    sup_dic.append([i, counter])

C1 = sup_dic

L1 = [[i[0][0], i[1]] for i in C1 if i[1] > min_support]
L1.sort(key=operator.itemgetter(1), reverse=True)

ordered_items = {}

for j in D:
    ordered_items[j] = []
    for i in L1:
        if i[0] in D[j]:
            ordered_items[j].append(i[0])
            
ordered_transactions = ordered_items
ordered_items = [i[0] for i in L1]

nodes = L1
edge_list = []

for i in ordered_transactions:
    for j in range(len(ordered_transactions[i])):
        try:
            edge_list.append([ordered_transactions[i][j], ordered_transactions[i][j + 1]])
        except:
            continue

edge = set(tuple(i) for i in edge_list)

for i in edge:
    for j in i:
        for k in nodes:
            if j in k:
                k[1] = k[1] - 1
                
ordered = set(tuple(i) for i in ordered_transactions.values())
end = time.time()

print("The run-time for FP-growth Algorithm is: ", end - start, "\n\n")
print("-----------------------------------------")                
print("The Frequent items are: ", "\n")
print("The weighted nodes are: ", "\n\n", nodes)               
print("-----------------------------------------")                
print("The FP-Tree is: ", "\n") 
print("The edges are: ", "\n\n", edge)


