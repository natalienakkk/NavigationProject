from preprocessing import read_xyz, remove_noise, downsample
from visualization import plot_data, plot_clusters_with_exit,plot_clusters_with_bounding,plot_clusters
from FindExit import extract_clusters, get_clusters, compute_exit_point, bounding_box
from projection import projection,compute_plane
import open3d as o3d


def get_params_from_filename(filename):
    if "room1" in filename:
        return {"eps": 0.08, "min_samples": 13}
    elif "room2" in filename:
        return {"eps": 0.03, "min_samples": 25}
    elif "room3" in filename:
        return {"eps": 0.03, "min_samples": 30}
    elif "room4" in filename:
        return {"eps": 0.03, "min_samples": 6}
    elif "map" in filename:
        return {"eps": 0.1, "min_samples": 30}


# Main function
def main():
    print("choose the room by typing a it's number: \n1.room1\n2.room2\n3.room3\n4.room4\n5.map\n")
    chosen_room_num = int(input("chosen room: "))

    # read xyz file and extract all points (x,y,z) according to chosen room.
    if chosen_room_num == 1:
        data = read_xyz("room1.xyz")
    elif chosen_room_num == 2:
        data = read_xyz("room2.xyz")
    elif chosen_room_num == 3:
        data = read_xyz("room3.xyz")
    elif chosen_room_num == 4:
        data = read_xyz("room4.xyz")
    else:
        data = read_xyz("map.xyz")

    cloud = o3d.geometry.PointCloud()
    cloud.points = o3d.utility.Vector3dVector(data)

    # Compute the best-fit plane for the original point cloud.
    centroid, normal = compute_plane(cloud)

    # Plot data points after projection from 3D->2D.
    points_2d = projection(cloud, centroid, normal)
    plot_data(points_2d, "Original data")

    # Plot data points after removing noise and projection from 3D->2D.
    cloud = remove_noise(cloud)
    points_2d = projection(cloud, centroid, normal)
    plot_data(points_2d, "Data After Noise Removal")

    # Plot data points after down sampling and projection from 3D->2D.
    cloud = downsample(cloud)
    points_2d = projection(cloud, centroid, normal)
    plot_data(points_2d, "Data After Downsampling")

    # Extract clusters
    if chosen_room_num == 1:
        params = get_params_from_filename("room1.xyz")
    elif chosen_room_num == 2:
        params = get_params_from_filename("room2.xyz")
    elif chosen_room_num == 3:
        params = get_params_from_filename("room3.xyz")
    elif chosen_room_num == 4:
        params = get_params_from_filename("room4.xyz")
    else:
        params = get_params_from_filename("map.xyz")

    clusters_2d = extract_clusters(points_2d, eps=params["eps"], min_points=params["min_samples"])

    # Sort clusters and get the smallest one.
    sorted_clusters = sorted(clusters_2d, key=len)
    all_except_smallest = get_clusters(clusters_2d)

    # Calculate bounding rectangle
    bounding_rectangle = bounding_box(all_except_smallest, sorted_clusters[0])

    # Plot the 2D clusters with the bounding rectangle around the combined clusters
    plot_clusters_with_bounding(clusters_2d, bounding_rectangle)
    plot_clusters(clusters_2d)

    # Compute the exit point
    exit_point = compute_exit_point(sorted_clusters[0])
    print(f"Exit Point (x, y): {exit_point}")

    # Plot the 2D clusters with the exit point highlighted
    plot_clusters_with_exit(clusters_2d, exit_point)



if __name__ == "__main__":
    main()