import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.random.rand(1000)
plt.hist(x,10)
plt.show()

D = pd.DataFrame([x,x+1])
D.plot(kind = 'box')
plt.show()