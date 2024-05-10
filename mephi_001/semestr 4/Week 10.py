import numpy as np
from scipy.interpolate import interpn
import plotly.graph_objects as go

data = np.load("data_3d.npy")

x = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6])
y = x.copy()
z = x.copy()

new_count = 100

x_new = np.linspace(x.min(), x.max(), new_count)
y_new = x_new.copy()
z_new = x_new.copy()

points = (x, y, z)
xi, yi, zi = np.meshgrid(x_new, y_new, z_new, indexing='ij')
data_interp = interpn(points, data, (xi, yi, zi))


def surface_create(x, y, z, title):
    fig = go.Figure(data=[go.Surface(x=x, y=y, z=z)])
    fig.update_layout(title=title, scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='Density'))
    fig.show()


def heatmap_create(x, y, z, title):
    fig = go.Figure(data=go.Heatmap(x=x, y=y, z=z, colorscale='Viridis'))
    fig.update_layout(title=title, xaxis_title='x', yaxis_title='y')
    fig.show()


# for z in (0.5, 1.5, 2.5, 3.0):
#     z_idx = np.argmin(np.abs(z_new - z))
#     surface_create(xi[:, :, z_idx], yi[:, :, z_idx], data_interp[:, :, z_idx], f"Electron Density (z = {z})")
#     heatmap_create(x_new, y_new, data_interp[:, :, z_idx], f"Electron Density (z = {z})")
#
for z in (0.5, 1.5, 2.5, 3.0):
    z_idx = np.argmin(np.abs(z_new - z))
    x_idx = np.argmin(np.abs(x_new - 0))

    surface_create(xi[:, :, z_idx], yi[:, :, z_idx], data_interp[:, :, z_idx], f"Electron Density (z = {z})")
    heatmap_create(x_new, y_new, data_interp[:, :, z_idx], f"Electron Density (z = {z})")


    go.Figure(data=go.Scatter(x=y_new, y=data_interp[x_idx, :, z_idx], mode='lines')).update_layout(
        xaxis_title='y',
        yaxis_title='Density'
    ).show()