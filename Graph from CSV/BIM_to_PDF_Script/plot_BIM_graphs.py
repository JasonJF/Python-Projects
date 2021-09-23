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

    # Set x-axis title
    fig.update_xaxes(title_text="Time")

    # Set y-axes titles
    fig.update_yaxes(title_text="Temperature <b>(deg)</b>", secondary_y=False)
    fig.update_yaxes(title_text="Power <b>(dBm)</b>", secondary_y=True)

    # fig.show()

    #export
    pio.write_image(fig, fullSavePath, width=1000, height=600)
    # fig.write_image("images/multiple_figures_bim.png")
    print(plotName + " Generated")

# generate_Plots()
