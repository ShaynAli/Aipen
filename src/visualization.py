import data as dt

from bokeh.plotting import figure, output_file, show


def plot_line(data_class, x_label, y_label):
    # Output to static HTML file
    output_file("lines.html")

    # Use hover tool
    tools = "hover"

    # Create a plot with specified parameters
    p = figure(tooltips=tools, x_axis_label=x_label, y_axis_label=y_label)

    # Designate as line graph with given appearance properties
    p.line(data_class.data[:, 0], data_class.data[:, 1], line_width=2)
    p.toolbar.logo = "grey"
    p.background_fill_color = "#dddddd"
    p.hover.tooltips = [
        (x_label, "@x"),
        (y_label, "@y")
    ]

    # Display
    show(p)


def plot_scatter(data_class, x_label, y_label):
    # Output to static HTML file
    output_file("scatter.html")

    # Use hover tool
    tools = "hover"

    # Create a plot with specified parameters
    p = figure(tooltips=tools, x_axis_label=x_label, y_axis_label=y_label)

    # Designate as scatter and customize appearance
    p.scatter(data_class.data[:, 0], data_class.data[:, 1], radius=0.2)
    p.toolbar.logo = "grey"
    p.background_fill_color = "#dddddd"
    p.hover.tooltips = [
        (x_label, "@x"),
        (y_label, "@y")
    ]

    # Display
    show(p)


# Test data for both types of plots
# testData = dt.Data()
# testData.set_linear(50, 2, -50)
#
# plot_line(testData, "Generation", "Accuracy")
#
# testRandom = dt.Data()
# testRandom.set_random(1000, -100, 100)
#
# plot_scatter(testRandom, "Generation", "Accuracy")
