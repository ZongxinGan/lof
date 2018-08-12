# -*- coding: utf8 -*-

import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor
import datetime

'''
f = open("receiveflow.txt",'a')

b = np.random.uniform(low=0,high=10,size=(100,1))
for i in range(len(b)):
    f.writelines('1' + '\n')
    
    f.writelines(str(b[i][-1]) + '\n')

f.close
'''

starttime = datetime.datetime.now()

raw = np.loadtxt("receiveflow.txt")
 
X = np.reshape(raw, (-1,2))

clf = LocalOutlierFactor(n_neighbors=10,n_jobs=-1)
y_pred = clf.fit_predict(X)

'''
y_deci = clf._decision_function(X)
clf.fit(X)
pred_D_X = clf._predict()
print(pred_D_X)
print(y_deci)
for i in range(len(pred_D_X)):
    if pred_D_X[i] == -1:
        m = m+1
print(m)
'''

Z = np.c_[X,y_pred]
Z = sorted(Z,key=lambda x: x[2],reverse=True)
for i in range(len(Z)):
    Z[i] = Z[i].tolist()

Z = np.array(Z)

n = 0
for i in range(len(Z)):
    if Z[i][2] == -1:
        n = n+1
        print(Z[i][1])
        
print(n)

endtime = datetime.datetime.now()

print(endtime - starttime)

#draw part
xx, yy = np.meshgrid(np.linspace(0, 1, 100), np.linspace(-1, 11, 100))
W = clf._decision_function(np.c_[xx.ravel(), yy.ravel()])

W = W.reshape(xx.shape)

plt.title("Local Outlier Factor (LOF)")
plt.contourf(xx, yy, W, cmap=plt.cm.Blues)

a = plt.scatter(Z[:1000, 0], Z[:1000, 1], c='white',
                edgecolor='k', s=20)
b = plt.scatter(Z[1000:, 0], Z[1000:, 1], c='red',
                edgecolor='k', s=20)
plt.axis('tight')
plt.xlim((0, 1))
plt.ylim((-1, 11))
plt.legend([a, b],
           ["normal observations",
            "abnormal observations"],
           loc="upper left")
plt.show()

