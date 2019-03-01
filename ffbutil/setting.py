import matplotlib.pyplot as plt

# Font
line_of_axes = 1.0
plt.rcParams.update({
    'axes.grid': True,
    'font.family': 'Arial',
    'font.size': 12.0,
    'grid.linestyle': '--',
    'grid.linewidth': 0.5,
    'legend.edgecolor': 'black',
    'legend.fancybox': False,
    'legend.framealpha': 1.0,
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'axes.linewidth': line_of_axes,
    'xtick.major.width': line_of_axes,
    'ytick.major.width': line_of_axes,
    'xtick.minor.width': line_of_axes,
    'ytick.minor.width': line_of_axes,
})
inch2mm = 2.54
# 1. [inches] single-column figure size
width = 8.0 / inch2mm
# golden ratio
# height = width / 1.618
# same ratio
height = width
fontsizefig = 8.0
extension = ".jpg"
fig_dpi = 300
