import numpy as np

# Computes the best-fit plane for a set of 3D points using Singular Value Decomposition and returns the centroid of
# the points and the normal to the plane.
def fit_plane(points):
    centroid = points.mean(axis=0)
    shifted_points = points - centroid
    u, s, vh = np.linalg.svd(shifted_points)
    normal = vh[-1]
    return centroid, normal

# Projects a set of 3D points onto a plane defined by its centroid and normal vector.
def project_to_plane(points, centroid, normal):
    d = np.dot(points - centroid, normal)
    projected_points = points - np.outer(d, normal)
    return projected_points

# Constructs two orthogonal basis vectors for a given plane normal, ensuring they are not parallel to the plane.
def construct_basis_vectors(normal):
    if np.abs(normal[2]) < 0.9:
        non_parallel = np.array([0, 0, 1])
    else:
        non_parallel = np.array([1, 0, 0])
    basis1 = np.cross(normal, non_parallel)
    basis1 /= np.linalg.norm(basis1)
    basis2 = np.cross(normal, basis1)
    basis2 /= np.linalg.norm(basis2)
    return basis1, basis2

#Transforms 3D points to a 2D coordinate system defined by the plane's centroid and its basis vectors.
def transform_to_2d(points, centroid, basis1, basis2):
    shifted_points = points - centroid
    x_coords = np.dot(shifted_points, basis1)
    y_coords = np.dot(shifted_points, basis2)
    return np.column_stack((x_coords, y_coords))

# Compute the best-fit plane for the original point cloud and returns its centroid and normal.
def compute_plane(cloud):
    points = np.asarray(cloud.points)
    centroid, normal = fit_plane(points)
    return centroid, normal

# Main function that uses all other function to project the points of a given 3D point cloud onto a plane and then
# transforms them to a 2D coordinate system.
def projection(cloud, centroid, normal):
    points = np.asarray(cloud.points)
    projected_points = project_to_plane(points, centroid, normal)
    basis1, basis2 = construct_basis_vectors(normal)
    points_2d = transform_to_2d(projected_points, centroid, basis1, basis2)
    return points_2d