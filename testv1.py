import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Define the vertices of the cuboid thickness is mm
def genArmor(thickness, resolution):
    # define dimensions of the cuboid
    width = thickness * 4
    length = thickness * 4
    # list of list of list of vertices
    # 0,0,0 in center
    
    arr = np.zeros((resolution, resolution, resolution, 3))
    for i in range(resolution):
        for j in range(resolution):
            for k in range(resolution):
                # i is the x axis
                # j is the y axis
                # k is the z axis
                plot = [(width/2 - (resolution - i) * thickness/resolution), 
                        (width/2 - (resolution - j) * thickness/resolution), 
                        (thickness/2 - (resolution - k) * thickness/resolution)]
                arr[i][j][k] = plot
    return arr

thickness = 10
armor = genArmor(thickness, 10)

# Flatten the array to get the vertices
armor_vertices = armor.reshape(-1, 3)

# Plot the vertices of the generated armor
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter3D(armor_vertices[:, 0], armor_vertices[:, 1], armor_vertices[:, 2])

# Plot the trajectory line through the center
center = [15, 15, 10]
trajectory = [10, 5, 10]

# Normalize the trajectory vector
trajectory_norm = np.linalg.norm(trajectory)
trajectory_unit = [t / trajectory_norm for t in trajectory]

# Define the length of the line
line_length = 60  # total length of the line

# Calculate the endpoints
end1 = [center[i] + trajectory_unit[i] * line_length / 2 for i in range(3)]
end2 = [center[i] - trajectory_unit[i] * line_length / 2 for i in range(3)]

ax.plot([end1[0], end2[0]], [end1[1], end2[1]], [end1[2], end2[2]], color='r')

# Set labels
padding = 2  # in cm
ax.set_xlim([-30, 30])
ax.set_ylim([-30, 30])
ax.set_zlim([-thickness / 2, thickness / 2])

# Set the aspect ratio to be 30 cm, 30 cm, thickness in mm
ax.set_box_aspect([30, 30, thickness / 10])  # Convert thickness to cm

# Show the plot
plt.show()