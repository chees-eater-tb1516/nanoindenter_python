import numpy as np

import matplotlib.pyplot as plt

results_list=[]
with open ("hfrrwaterresults.txt", 'r')as file:
    for line in file:
        results_list += [line]
        
data_array = np.array([np.fromstring (item, sep=',') for item in results_list])

data_array = data_array.transpose()        

step = 9
#print (np.mean(data_array[3][30:]))
#print (np.std(data_array[3][30:]))
start = (step-1)*30 
end = step*30 + 1

plt.plot(data_array[1][start:end], data_array[3][start:end], 'k*')
plt.xlabel('x position [µm] crosses wear track')
plt.ylabel('stiffness [arbitrary units]')
plt.show()
        
x=1