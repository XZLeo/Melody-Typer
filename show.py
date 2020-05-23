import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)
x = np.array(range(10))
plt.plot(x, np.sin(x))


a = np.diag(range(15))
plt.matshow(a) 

plt.show()#所有图只要一个show就好了