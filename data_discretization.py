# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 15:34:38 2019

@author: sahar
"""

#In this notebook the data is being discretized and it is going to be saved in 
#a csv file named data_discretization.csv 
#(To run this code it will take a long time that is why I saved the data in csv file) 
#I used bluehive with one Gpu to run it.

import pandas as pd
import numpy as np
from collections import defaultdict
import itertools
import time

data = pd.read_table('data.txt', header=None, sep=',')
data.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num',
                'marital-status', 'occupation', 'relationship', 'race', 'sex',
                'capital-gain', 'capital-loss', 'hours-per-week',
                'native-country', 'income']


for i in range(len(data['age'].values)):   
    if data['age'].values[i] < 26: 
        data['age'].iloc[i] = 'Young'
    elif data['age'].values[i] > 26 and data['age'].values[i] < 55:
        data['age'].iloc[i] = 'Middle-Aged'         
    else:
        data['age'].iloc[i] = 'Old'
        
for i in range(len(data['hours-per-week'].values)):
    if data['hours-per-week'].values[i] > 0 and data['hours-per-week'].values[i] <= 20:       
        data['hours-per-week'].iloc[i] = '0-20hrs'
    elif data['hours-per-week'].values[i] > 20 and data['hours-per-week'].values[i] <= 40:    
        data['hours-per-week'].iloc[i] = '20-40hrs'
    elif data['hours-per-week'].values[i] > 40 and data['hours-per-week'].values[i] <= 60:    
        data['hours-per-week'].iloc[i] = '40-60hrs'
    elif data['hours-per-week'].values[i] > 60 and data['hours-per-week'].values[i] <= 80:
        data['hours-per-week'].iloc[i] = '60-80hrs'
    else:
        data['hours-per-week'].iloc[i] = '80-100'
        
for i in range(len(data['education-num'].values)):                       
    if data['education-num'].values[i] > 0 and data['education-num'].values[i] <= 4:
        data['education-num'].iloc[i] = '0-4'            
    elif data['education-num'].values[i] > 4 and data['education-num'].values[i] <= 8:      
        data['education-num'].iloc[i] = '4-8'
    elif data['education-num'].values[i] > 8 and data['education-num'].values[i] <= 12:     
        data['education-num'].iloc[i] = '8-12'
    else:
        data['education-num'].iloc[i] = '12-16'           

for i in range(len(data['capital-gain'].values)):       
    if data['capital-gain'].values[i] == 0:               
        data['capital-gain'].iloc[i] = 'No Gain'
    elif data['capital-gain'].values[i] > 0 and data['capital-gain'].values[i] <= 10000:     
        data['capital-gain'].iloc[i] = 'Medium Gain'                    
    else:
        data['capital-gain'].iloc[i] = 'High Gain'  

for i in range(len(data['capital-loss'].values)):
    if data['capital-loss'].values[i] == 0:
        data['capital-loss'].iloc[i] = 'No Loss'                          
    elif data['capital-loss'].values[i] > 0 and data['capital-loss'].values[i] <= 2250:
        data['capital-loss'].iloc[i] = 'Modest Loss'                      
    else:
        data['capital-loss'].iloc[i] = 'Appreciable Loss'                 
    
for i in range(len(data['fnlwgt'].values)):
    if data['fnlwgt'].values[i] > 0 and data['fnlwgt'].values[i] <= 375000:
        data['fnlwgt'].iloc[i] = '<=375,000'
    elif data['fnlwgt'].values[i] > 375000 and data['fnlwgt'].values[i] <= 750000:  
        data['fnlwgt'].iloc[i] = '>375,000 and <=750,000'
    elif data['fnlwgt'].values[i] > 750000 and data['fnlwgt'].values[i] <= 1125000:   
        data['fnlwgt'].iloc[i] = '>750,000 and <=1,125,000'
    else:
        data['fnlwgt'].iloc[i] = '>1,125,000 and <=1,500,000'
        
data = data.applymap(lambda d: np.nan if d == ' ?' else d) 
data.to_csv('data_discretization.csv')