import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_bloch_sphere():
   
    phi = np.linspace(0, 2 * np.pi, 100)
    theta = np.linspace(0, np.pi, 100)
    x = np.outer(np.cos(phi), np.sin(theta))
    y = np.outer(np.sin(phi), np.sin(theta))
    z = np.outer(np.ones(np.size(phi)), np.cos(theta))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(x, y, z, color='c', alpha=0.1, rstride=5, cstride=5)

    theta_state = np.pi / 4  
    phi_state = np.pi * 3 / 4 

    x_state = np.sin(theta_state) * np.cos(phi_state)
    y_state = np.sin(theta_state) * np.sin(phi_state)
    z_state = np.cos(theta_state)

    ax.quiver(0, 0, 0, x_state, y_state, z_state, color='r', linewidth=2, label='State Vector')

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    ax.set_title('Bloch Sphere Representation')
    ax.legend()

    ax.set_box_aspect([1,1,1])  

    plt.show()

plot_bloch_sphere()
