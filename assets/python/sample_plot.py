import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

# plt.style.use('dark_background')

# fig, ax = plt.subplots()

# L = 6
# x = np.linspace(0, L)
# ncolors = len(plt.rcParams['axes.prop_cycle'])
# shift = np.linspace(0, L, ncolors, endpoint=False)
# for s in shift:
#     ax.plot(x, np.sin(x + s), 'o-')
# ax.set_xlabel('x-axis')
# ax.set_ylabel('y-axis')
# ax.set_title("'dark_background' style sheet")

# plt.show()

L = 6
x = np.linspace(0, L)
ncolors = len(px.colors.qualitative.Plotly)
shift = np.linspace(0, L, ncolors, endpoint=False)

fig = px.line(x=x, y=[np.sin(x + s) for s in shift], labels={'x': 'x-axis', 'y': 'y-axis'}, title="'dark_background' style sheet")
fig.update_layout(template='plotly_dark')
fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',
})

fig.write_html("./_includes/sample_plot.html")