# NavigationProject
Indoor Navigation Using Drones: A Real-Time Systems  Approach        

Description of the project:
This project is a Python-based application that utilizes point cloud data to identify and locate the exit point of a room. The application processes 3D spatial data, performs noise removal, downsampling, and projects the data to 2D. It then applies the DBSCAN clustering algorithm to extract clusters representing different parts of the room and calculates the bounding box to separate the room from the exit. The exit point is computed as the mean of the smallest cluster and visualized in both 2D and 3D plots.


Features:

1.Data Preprocessing: Reads XYZ file format, removes noise, and performs downsampling.

2.Projection: Projects 3D point cloud data to 2D for further processing.

3.Clustering: Utilizes DBSCAN clustering algorithm to segregate the room and exit points.

4.Bounding Box Calculation: Computes a bounding box that fits all clusters except the smallest one, defining the room and separating it from the exit.

5.Exit Point Computation: Calculates the exit point as the mean of the smallest cluster.

6.Visualization: Provides 2D and 3D plots of the data points, clusters, bounding box, and exit point.

7.Parameter Adjustment: Allows adjustment of DBSCAN parameters based on the input file name.

Dependencies: NumPy,Open3D,scikit-learn,Matplotlib
