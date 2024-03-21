import numpy as np

import matplotlib.pyplot as plt

results_list=[]
with open ("results.txt", 'r')as file:
    for line in file:
        results_list += [line]
        
data_array = np.array([np.fromstring (item, sep=',') for item in results_list])

data_array = data_array.transpose()        

plt.plot(data_array[2][20:30], data_array[3][20:30], 'k*')
plt.xlabel('y position [m e-6] central to wear track')
plt.ylabel('stiffness [arbitrary units]')
plt.show()
        
x=1