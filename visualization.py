import matplotlib.pyplot as plt
import open3d as o3d
import numpy as np


# Plot the 2D clusters
def plot_clusters(clusters_2d):
    plt.figure(figsize=(10, 10))

    sorted_clusters = sorted(clusters_2d, key=len)

    # Smallest cluster - Red color for the smallest cluster.
    smallest_cluster = sorted_clusters[0]
    plt.scatter(smallest_cluster[:, 0], smallest_cluster[:, 1], c='red', label='Smallest Cluster',
                s=50)

    # Plot other clusters - black for the other clusters.
    for cluster in sorted_clusters[1:]:
        plt.scatter(cluster[:, 0], cluster[:, 1], c='black', s=10)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Clusters with Smallest Cluster Highlighted')
    plt.show()

# Plot the 2D clusters and highlight the exit point
def plot_clusters_with_exit(clusters_2d, exit_point):
    plt.figure(figsize=(10, 10))

    sorted_clusters = sorted(clusters_2d, key=len)

    # Smallest cluster - Red color for the smallest cluster
    smallest_cluster = sorted_clusters[0]
    plt.scatter(smallest_cluster[:, 0], smallest_cluster[:, 1], c='red', label='Smallest Cluster', s=50)

    # Plot other clusters - black color for all other points
    for cluster in sorted_clusters[1:]:
        plt.scatter(cluster[:, 0], cluster[:, 1], c='black', s=10)

    # Highlight the exit point - blue color for the exit point
    plt.scatter(exit_point[0], exit_point[1], c='blue', marker='x', label='Exit', s=100)

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Clusters with Exit Point Highlighted')
    plt.show()



# Plot 2D clusters with the bounding rectangle of the room
def plot_clusters_with_bounding(clusters_2d, rectangle=None):
    colors = plt.cm.jet(np.linspace(0, 1, len(clusters_2d)))

    # Plot clusters
    for i, cluster in enumerate(clusters_2d):
        plt.scatter(cluster[:, 0], cluster[:, 1], c=[colors[i]], marker='o', label=f'Cluster {i+1}')

    # Plot the bounding rectangle
    if rectangle:
        min_x, min_y, max_x, max_y = rectangle
        plt.plot([min_x, max_x, max_x, min_x, min_x], [min_y, min_y, max_y, max_y, min_y], 'r-')

    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Clusters with Bounding Rectangle')
    plt.show()


# Plot data points
def plot_data(points, title):
    plt.scatter(points[:, 0], points[:, 1], c='b', marker='.')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(title)
    plt.show()



def visualize_wall_and_non_wall(cloud_wall, cloud_non_wall):
    # Set the colors for the wall and non-wall points
    cloud_wall.paint_uniform_color([1, 0, 0])  # Red for wall
    cloud_non_wall.paint_uniform_color([0, 1, 0])  # Green for non-wall

    # Combine the point clouds for visualization
    combined = cloud_wall + cloud_non_wall

    # Visualize the point clouds
    o3d.visualization.draw_geometries([combined])