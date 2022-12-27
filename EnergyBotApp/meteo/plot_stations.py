import pandas as pd
import plotly.express as px


unique_sta = pd.read_csv("data/unique_station.csv")

color_scale = [(0, "orange"), (1, "red")]

fig = px.scatter_mapbox(
    unique_sta,
    lat="lat",
    lon="lon",
    hover_name="zone",
    hover_data=["height_sta", "zone"],
    color="zone",
    zoom=8,
    height=800,
    width=800,
)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
