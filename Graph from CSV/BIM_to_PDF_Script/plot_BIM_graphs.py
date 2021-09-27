import os
import errno
from pathlib import Path
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio

#creating subplots

def generate_Plots(plotData):

    #Set up paths to save files
    plotName = plotData["plotName"]
    savePath = str(Path(__file__).absolute().parent)
    fullSavePath = savePath  + "\images\\" + plotName + ".png"
    ##Create directory to store file in
    if not os.path.exists(os.path.dirname(fullSavePath)):
        try:
            os.makedirs(os.path.dirname(fullSavePath))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    primaryPlot = plotData

    right_axis_title = plotData["right_axis_title"]
    right_axis_unit = plotData["right_axis_unit"]
    # print(len(plotData["time"]))
    # print(plotData["time"][0])
    # print(plotData["time"][len(plotData["time"]) - 1])
    
    # primaryPlot = {
    #     "x_values": [0,1,2,3,4,5],
    #     "y1_values": [0,1,2,3,4,5],
    #     "y2_values": [5,4,3,2,1,0],
    #     "y1_name": "temperature 1",
    #     "y2_name": "temperature 2"

    # }
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Add traces
    fig.add_trace(
        go.Scatter(x=primaryPlot["x_values"], y=primaryPlot["era_temps"], name="tempERA"),
        secondary_y=False,
    )

    fig.add_trace(
        go.Scatter(x=primaryPlot["x_values"], y=primaryPlot["ura_temps"], name="tempURA"),
        secondary_y=False,
    )

    #Secondary Plot 1
    fig.add_trace(
        go.Scatter(x=primaryPlot["x_values"], y=primaryPlot["y1_values"], name=primaryPlot["y1_name"]),
        secondary_y=True,
    )
    #Secondary Plot 2
    fig.add_trace(
        go.Scatter(x=primaryPlot["x_values"], y=primaryPlot["y2_values"], name=primaryPlot["y2_name"]),
        secondary_y=True,
    )

    # Add figure title
    fig.update_layout(
        title_text=plotData["plotName"]
    )
    # # Add annotation for Maximum value
    # y1_max_value = max(plotData["y1_values"])
    # y1_max_index = plotData["y1_values"].index(y1_max_value)
    # # max_string = f"Max: {y1_max_value}"
    # y1_min_value = min(plotData["y1_values"])
    # y1_min_index = plotData["y1_values"].index(y1_min_value)

    # print(y1_max_value)
    # print(y1_max_index)
    # ## Max Annotation
    # fig.add_annotation(x=y1_max_index, y=y1_max_value,
    #         xref="x",
    #         yref="y2",
    #         text=f"Max : {round(y1_max_value,2)}",
    #         showarrow=True,
    #         arrowhead=1)
    # ## Min annotation
    # fig.add_annotation(x=y1_min_index, y=y1_min_value,
    #         xref="x",
    #         yref="y2",
    #         text=f"Min : {round(y1_min_value,2)}",
    #         showarrow=True,
    #         arrowhead=1)

    #Add annotations
    addAnnotations(fig, plotData["y1_values"], plotData["y1_name"])
    addAnnotations(fig, plotData["y2_values"], plotData["y2_name"])

    # Set x-axis title
    fig.update_xaxes(title_text="Time")

    # Set y-axes titles
    fig.update_yaxes(title_text="Temperature <b>(deg)</b>", secondary_y=False)
    fig.update_yaxes(title_text=f"{right_axis_title} <b>{right_axis_unit}</b>", secondary_y=True)

    #Update x-ticks
    fig.update_layout(
        xaxis = dict(
            tickmode = 'array',
            tickvals = [0, len(plotData["time"]) - 1],
            ticktext = [plotData["time"][0], plotData["time"][len(plotData["time"]) - 1] ]
        )
)
    # fig.show()

    #export
    pio.write_image(fig, fullSavePath, width=1000, height=600)
    # fig.write_image("images/multiple_figures_bim.png")
    print(plotName + " Generated")

def addAnnotations(fig, values, name):
    max_value = max(values)
    max_index = values.index(max_value)
    # max_string = f"Max: {y1_max_value}"
    min_value = min(values)
    min_index = values.index(min_value)

    print(name)
    print(max_value)
    print(max_index)
    
    ## Max Annotation
    fig.add_annotation(x=max_index, y=max_value,
            xref="x",
            yref="y2",
            text=f"Max {name}: {round(max_value,2)}",
            showarrow=True,
            arrowhead=1)
    ## Min annotation
    fig.add_annotation(x=min_index, y=min_value,
            xref="x",
            yref="y2",
            text=f"Min {name}: {round(min_value,2)}",
            showarrow=True,
            arrowhead=1)

# generate_Plots()
