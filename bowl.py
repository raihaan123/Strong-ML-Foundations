# %matplotlib
from mpl_toolkits.mplot3d import axes3d
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
fig = plt.figure(figsize=(20, 10))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')
X = np.linspace(-10, 10)
x1, x2 = np.meshgrid(X, X)
y = x1**2 + 10*x2**2
ax1.set_title('Before normalisation', fontsize=20)
ax1.plot_surface(x1, x2, y, cmap=cm.copper)
ax1.set_xlabel('Weight 1', fontsize=20)
ax1.set_ylabel('Weight 2', fontsize=20)
ax1.set_zlabel('Loss', fontsize=20)
y = x1**2 + x2**2
ax2.set_title('After normalisation', fontsize=20)
ax2.plot_surface(x1, x2, y, cmap=cm.copper)
ax2.set_xlabel('Weight 1', fontsize=20)
ax2.set_ylabel('Weight 2', fontsize=20)
ax2.set_zlabel('Loss', fontsize=20)
plt.show()
