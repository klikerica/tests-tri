import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from scipy.spatial import Delaunay

def plot_tri_simple(ax, points, tri):
    for tr in tri.simplices:
        pts = points[tr, :]
        ax.plot3D(pts[[0,1],0], pts[[0,1],1], pts[[0,1],2], color='r', lw='0.3')
        ax.plot3D(pts[[0,2],0], pts[[0,2],1], pts[[0,2],2], color='r', lw='0.3')
        ax.plot3D(pts[[0,3],0], pts[[0,3],1], pts[[0,3],2], color='r', lw='0.3')
        ax.plot3D(pts[[1,2],0], pts[[1,2],1], pts[[1,2],2], color='r', lw='0.3')
        ax.plot3D(pts[[1,3],0], pts[[1,3],1], pts[[1,3],2], color='r', lw='0.3')
        ax.plot3D(pts[[2,3],0], pts[[2,3],1], pts[[2,3],2], color='r', lw='0.3')

    ax.scatter(points[:,0], points[:,1], points[:,2], color='b')

points= np.array([[1,2,2],[3,2.8,2],[5,2.5,2],[5,3,2],[2,2.2,3],[4,2.8,5],[3,2.6,6]])
tri = Delaunay(points)

def plot_tri_2(ax, points, tri):
    edges = collect_edges(tri)
    x = np.array([])
    y = np.array([])
    z = np.array([])
    for (i,j) in edges:
        x = np.append(x, [points[i, 0], points[j, 0], np.nan])      
        y = np.append(y, [points[i, 1], points[j, 1], np.nan])      
        z = np.append(z, [points[i, 2], points[j, 2], np.nan])
    ax.plot3D(x, y, z, color='g', lw='0.1')

    ax.scatter(points[:,0], points[:,1], points[:,2], color='b')


def collect_edges(tri):
    edges = set()

    def sorted_tuple(a,b):
        return (a,b) if a < b else (b,a)
    # Add edges of tetrahedron (sorted so we don't add an edge twice, even if it comes in reverse order).
    for (i0, i1, i2, i3) in tri.simplices:
        edges.add(sorted_tuple(i0,i1))
        edges.add(sorted_tuple(i0,i2))
        edges.add(sorted_tuple(i0,i3))
        edges.add(sorted_tuple(i1,i2))
        edges.add(sorted_tuple(i1,i3))
        edges.add(sorted_tuple(i2,i3))
    return edges


fig = plt.figure()
ax = plt.axes(projection='3d')
plot_tri_simple(ax, points, tri)
plt.show()
