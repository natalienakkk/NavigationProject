import numpy as np
from sklearn.cluster import DBSCAN

# extract clusters using DBSCAN clustering algorithm 2 important parameters : 1.The maximum distance between two
# samples for one to be considered as in the neighborhood of the other.
# 2. The number of samples (or total weight) in a neighborhood for a point to be considered as a core point.
def extract_clusters(points_2d, eps, min_points):
    db = DBSCAN(eps=eps, min_samples=min_points).fit(points_2d)
    labels = db.labels_
    unique_labels = np.unique(labels)
    clusters_2d = [points_2d[labels == label] for label in unique_labels if label != -1]
    return clusters_2d

#Find bounding box that fits all the clusters except the smallest cluster,using this bounding box we define the room and seprate it from the exit
def bounding_box(points, smallest_cluster):
    #basic bounding box that includes all clusters.
    min_x, min_y = np.min(points, axis=0)
    max_x, max_y = np.max(points, axis=0)

    # Function to check if a point is inside the bounding box
    def is_inside_bbox(point, bounding_box):
        return (bounding_box[0] <= point[0] <= bounding_box[2]) and (bounding_box[1] <= point[1] <= bounding_box[3])

    # Check if the entire cluster is inside the bounding box
    cluster_inside = all(is_inside_bbox(p, [min_x, min_y, max_x, max_y]) for p in smallest_cluster)

    # Adjust the bounding box to exclude the smallest cluster
    if cluster_inside:
        centroid_x = np.mean(smallest_cluster, axis=0)[0]
        # check what side should we move the bounding box to exclude the smallest cluster
        if centroid_x < (min_x + max_x) / 2:
            shift = np.max(smallest_cluster, axis=0)[0] - min_x + 0.01
            min_x += shift
            max_x += shift
        else:
            shift = max_x - np.min(smallest_cluster, axis=0)[0] + 0.01
            min_x -= shift
            max_x -= shift

        # Recompute the y values based on the points inside the adjusted bounding box
        points_inside_bbox = [p for p in points if is_inside_bbox(p, [min_x, min_y, max_x, max_y])]
        min_y, max_y = np.min(points_inside_bbox, axis=0)[1], np.max(points_inside_bbox, axis=0)[1]

    return [min_x, min_y, max_x, max_y]

# Compute the exit point
def compute_exit_point(smallest_cluster):
    return np.mean(smallest_cluster, axis=0)

# Get all clusters except the smallest one
def get_clusters(clusters_2d):
    # Sort clusters based on their size
    sorted_clusters = sorted(clusters_2d, key=len)
    return np.vstack(sorted_clusters[1:])