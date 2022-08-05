import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.axes_grid1 import make_axes_locatable


def plot_state_values(V, iterations):
	x_range = np.arange(12, 22) # if < 11 we are not dumb and we pick another card
	y_range = np.arange(1, 11) # dealer's face up card
	X, Y = np.meshgrid(x_range, y_range)

	fig = plt.figure(figsize=(15,20))

	aces = [(True, "Usable ace"), (False, "No usable ace")]

	for i, (usableAce, title) in enumerate(aces, 1):
		ax = fig.add_subplot(int("21" + str(i)), projection='3d')
		Z = np.array([V[x, y, usableAce] if (x, y, usableAce) in V else 0 for y in Y[:,0] for x in X[0] ]).reshape(X.shape)

		surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, vmin=-1.0, vmax=1.0,
							   edgecolor='w', linewidth=0.5)
		ax.set_xlabel("Player's Current Sum")
		ax.set_ylabel("Dealer's Showing Card")
		ax.set_zlabel("Value")
		ax.view_init(ax.elev, -120)
		ax.set_title(title, fontsize=14)

	fig.suptitle("Value after %i iterations" % iterations, fontsize=20)
	plt.show()
