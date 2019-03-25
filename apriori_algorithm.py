# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 15:23:38 2019

@author: sahar
"""

import pandas as pd
from itertools import combinations 
import time

def creating_C(data, k):
    values = []
    for i in data.values():
        for j in i:
            values.append(j)
    values = set(values)
    return set(combinations(values, k))

def calculating_support(D, C):
    sup_dic = {}
    for i in C:
        counter = 0
        i = frozenset(i)
        for j in D:
            if i.issubset(D[j]):
                counter += 1
        sup_dic[i] = counter

    return sup_dic

def creating_L(C, min_support):
    L = [i for i in C if C[i] > min_support]
    L_fi = {}
    for i in range(len(L)):
        L_fi[i] = list(L[i]) 
    return L_fi

def apriori(data, min_support):
    D = {}
    for i in range(data.shape[0]):
        D[i] = []
    trues = []    
    for items in data:
        trues = data[items].notnull()
        for i in range(len(trues)):
            if trues[i] == True:
                D[i].append(items)
    k = 1
    while True:
        
        if k == 1:
            C = creating_C(D, k)
        else:
            C = creating_C(L, k)        
        L = creating_L(calculating_support(D, C), min_support)
        if len(L) <= 1:
            break
        k = k + 1
        
    return L

start = time.time()
data = pd.read_csv('data_discretization.csv')
data = data.drop(['Unnamed: 0'], axis=1)
print("The Frequent Item Set is: ", apriori(data, min_support=int(input("Enter the minimum support: "))))
end = time.time()
print("The run-time for Apriori Algorithm is: ", end - start)

#Result: Enter the minimum support: 22000
#The Frequent Item Set is:  
#{0: ['education', 'capital-loss', 'hours-per-week', 'fnlwgt', 
 #    'native-country', 'marital-status', 'race', 'income', 
  #   'education-num', 'capital-gain', 'age', 'relationship', 'sex']}
  
#Enter the minimum support: 3
#The Frequent Item Set is:  {0: ['education', 'capital-loss', 'hours-per-week', 
 #                               'fnlwgt', 'workclass', 'native-country', 'marital-status',
  #                              'occupation', 'income', 'education-num', 'relationship', 
   #                             'capital-gain', 'age', 'race', 'sex']}