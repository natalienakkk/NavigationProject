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

How to run the project:

5 databases of rooms and 5 files included in this project:

1. preprocessing :  preprocessing of the data , noise removal and down sampling
2. FindExit : this part finds the exit by using clustering.
3. projection : projection to work with 2D instead of 3D
4. visualization: this part is responsibale for the results plotting.
5. main: this is the main file that uses all the other files and runs the code.

To run the project :
choose the room you want to find its exit from the files: room1,room2,room3,room4,map ,choice is made by typing number of the room your intrested in .
