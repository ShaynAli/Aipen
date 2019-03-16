from data import data as dt

from bokeh.plotting import figure, output_file, show

testData = dt.Data()
testData.set_linear(10, 2, -3)

# prepare some data
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

# output to static HTML file
output_file("lines.html")

TOOLS = "hover"

# create a new plot with a title and axis labels
p = figure(tooltips=TOOLS, title="simple line example", x_axis_label='x', y_axis_label='y')

# add a line renderer with legend and line thickness
p.line(testData.data[:, 0], testData.data[:, 1], legend="Test", line_width=2)
p.toolbar.logo = "grey"
p.background_fill_color = "#dddddd"
p.hover.tooltips = [
    ("x", "@x"),
    ("y", "@y")
]

# show the results
show(p)
