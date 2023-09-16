import numpy as np

#https://stackoverflow.com/questions/44509347/reading-file-with-variable-columns
# Read XYZ file
def read_xyz(filename):
    points = []
    with open(filename, 'r') as file:
        for line in file:
            data = line.split()
            x, y, z = float(data[0]), float(data[1]), float(data[2])  # added z-coordinate
            points.append((x, y, z))

    return np.array(points)

# The purpose of this function is to identify the non walls points and then removes statistical outliers from the non-wall points.
def remove_noise(cloud):
    # Identify walls in the room
    # Uses the RANSAC algorithm to identify the largest plane in the point cloud, which is assumed to be the wall.
    plane_model, inliers = cloud.segment_plane(distance_threshold=0.08, ransac_n=3, num_iterations=1000)
    cloud_wall = cloud.select_by_index(inliers)
    cloud_non_wall = cloud.select_by_index(inliers, invert=True)

    # Noise removal on non-wall points
    centroid = np.mean(np.asarray(cloud_non_wall.points), axis=0)
    distances = np.linalg.norm(np.asarray(cloud_non_wall.points) - centroid, axis=1)

    # Weights are used in a way the if the point is closest to the center its affected more .
    max_distance = np.max(distances)
    weights = 1 - (distances / max_distance)

    adjusted_nb_neighbors = 20 + (weights * 20).astype(int)
    avg_nb_neighbors = int(np.mean(adjusted_nb_neighbors))

    cloud_non_wall, ind = cloud_non_wall.remove_statistical_outlier(nb_neighbors=avg_nb_neighbors, std_ratio=1.0)

    # Merge wall and non-wall points
    cloud_combined = cloud_wall + cloud_non_wall
    #visualize_wall_and_non_wall(cloud_wall, cloud_non_wall)
    return cloud_combined

# Down sampling.
def downsample(cloud):
    cloud = cloud.voxel_down_sample(voxel_size=0.03)
    return cloud