import bokeh
from bokeh.plotting import figure, output_file, show


def plot_line(data_class, x_label, y_label):
    # Use hover tool
    tools = "hover"

    # Create a plot with specified parameters
    p = figure(tooltips=tools, x_axis_label=x_label, y_axis_label=y_label)

    # Get data from data class
    data = data_class.data

    # Designate as line graph with given appearance properties
    p.line(data[0], data[1], line_width=2)
    p.plot_height = 300
    p.plot_width = 600
    p.toolbar.logo = "grey"
    p.toolbar.autohide = True
    p.background_fill_color = "#dddddd"
    p.hover.tooltips = [
        (x_label, "@x"),
        (y_label, "@y")
    ]

    # Return the plot for display purposes
    return p


def plot_scatter(data, x_label, y_label):
    # Use hover tool
    tools = "hover"

    # Create a plot with specified parameters
    p = figure(tooltips=tools, x_axis_label=x_label, y_axis_label=y_label)

    # Designate as scatter and customize appearance
    p.scatter(data[0], data[1], radius=0.2)
    p.toolbar.logo = "grey"
    p.background_fill_color = "#dddddd"
    p.hover.tooltips = [
        (x_label, "@x"),
        (y_label, "@y")
    ]

    # Return the plot for display purposes
    return p


def multi_line(data):
    # Use hover tool
    tools = "hover"

    # Create a plot with specified parameters
    p = figure(tooltips=tools, x_axis_label="X", y_axis_label="Y")

    for k, v in data.items():
            generations = [e[0] for e in v]
            scores = [e[1] for e in v]
            p.line(generations, scores, line_width=2, legend=k)
            p.legend.click_policy = "hide"

    p.plot_height = 300
    p.plot_width = 600
    p.toolbar.logo = "grey"
    p.toolbar.autohide = True
    p.background_fill_color = "#dddddd"
    p.hover.tooltips = [
        ("X", "@x"),
        ("Y", "@y")
    ]

    # Return the plot for display purposes
    return p


def empty_plot():
    p = figure()
    p.plot_height = 300
    p.plot_width = 600
    p.toolbar.logo = "grey"
    p.toolbar.autohide = True
    p.background_fill_color = "#dddddd"

    return p

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
