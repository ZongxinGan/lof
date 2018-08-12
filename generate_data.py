# -*- coding: utf8 -*-

import numpy as np
f = open("receiveflow.txt",'w')


#generate normal train data
b = np.random.uniform(low=0,high=5,size=(1000,1))
for i in range(len(b)):
    tmp = np.random.uniform(0.25,0.75)
    f.writelines(str(tmp) + '\n')
    
    f.writelines(str(b[i][-1]) + '\n')



#generate abnormal data
b = np.random.uniform(low=8,high=10,size=(10,1))
for i in range(len(b)):
    tmp = np.random.uniform(0.25,0.75)
    f.writelines(str(tmp) + '\n')
    
    f.writelines(str(b[i][-1]) + '\n')



f.close
