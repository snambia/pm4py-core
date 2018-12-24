from matplotlib import pyplot
from pm4py.visualization.graphs.util import common

ATTRIBUTE_LABEL = "Attribute value"
DENSITY_LABEL = "Density"

def apply_plot(x, y, parameters=None):
    """
    Plot (non-logarithmic way) the graph with axis values contained in x and y

    Parameters
    ------------
    x
        Values for x-axis
    y
        Values for y-axis
    parameters
        Parameters of the algorithm, including:
            format -> Format of the target image

    Returns
    ------------
    temp_file_name
        Representation temporary file name
    """
    if parameters is None:
        parameters = {}

    format = parameters["format"] if "format" in parameters else "png"
    filename = common.get_temp_file_name(format)

    pyplot.plot(x, y)
    pyplot.xlabel(ATTRIBUTE_LABEL)
    pyplot.ylabel(DENSITY_LABEL)
    pyplot.savefig(filename)

    return filename


def apply_semilogx(x, y, parameters=None):
    """
    Plot (semi-logarithmic way) the graph with axis values contained in x and y

    Parameters
    ------------
    x
        Values for x-axis
    y
        Values for y-axis
    parameters
        Parameters of the algorithm, including:
            format -> Format of the target image

    Returns
    ------------
    temp_file_name
        Representation temporary file name
    """
    if parameters is None:
        parameters = {}

    format = parameters["format"] if "format" in parameters else "png"
    filename = common.get_temp_file_name(format)

    pyplot.semilogx(x, y)
    pyplot.xlabel(ATTRIBUTE_LABEL)
    pyplot.ylabel(DENSITY_LABEL)
    pyplot.savefig(filename)

    return filename