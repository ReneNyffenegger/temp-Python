import plotly.graph_objects as go
import numpy as np
import time

# Generate 100 random x, y, z coordinates
np.random.seed(42)  # for reproducibility
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

# Create a 3D scatter plot
fig = go.Figure(data=[go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(size=6, opacity=0.8)
)])

# Set axis labels
fig.update_layout(scene=dict(
        xaxis_title='X AXIS TITLE',
        yaxis_title='Y AXIS TITLE',
        zaxis_title='Z AXIS TITLE')
)

fig.show()
time.sleep(5)
