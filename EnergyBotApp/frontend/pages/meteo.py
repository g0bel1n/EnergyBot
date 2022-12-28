import streamlit as st
import plotly.express as px
import pandas as pd
import json
import pgeocode
from sklearn.neighbors import NearestNeighbors


def have_data(adress, min_lat, max_lat, min_lon, max_lon):

    lon, lat, place_name, state_name = pgeocode.Nominatim("fr").query_postal_code(
        adress
    )[["longitude", "latitude", "community_name", "state_name"]]

    if min_lat <= lat <= max_lat and min_lon <= lon <= max_lon:
        return True, lon, lat, f"{str(place_name)}, {str(state_name)}"

    return (False, 0, 0, 0)


def plot_selected_stations(stations, lat, lon):
    color_scale = [(False, "red"), (True, "green")]

    fig = px.scatter_mapbox(
        stations,
        lat="lat",
        lon="lon",
        hover_name="selected",
        hover_data=["height_sta", "zone"],
        color="selected",
        center=dict(lat=lat, lon=lon),
        zoom=8,
        height=800,
        width=800,
        color_discrete_map=color_scale,
        color_discrete_sequence=["red", "green"],
        range_color=[False, True],
    )

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    return fig


def plot_meteo_data(lon, lat):
    stations = pd.read_csv("data/unique_station.csv", index_col=0)
    nn = NearestNeighbors(n_neighbors=3).fit(stations[["lat", "lon"]])
    distances, closest_stations = nn.kneighbors([[lat, lon]])
    weights = 1 / distances[0]
    weights /= sum(weights)

    zone = stations.iloc[closest_stations[0][0], 4]

    ### Suntime
    suntime = pd.read_csv(
        f"data/{zone}daily_suntime.csv",
        infer_datetime_format=True,
        parse_dates=[0],
    ).set_index("date")
    extracted_suntime = pd.concat(
        (
            suntime[suntime["number_sta"] == sta]["precip"]
            for sta in stations.iloc[closest_stations[0], 0]
        ),
        axis=1,
    ).interpolate("time")
    extracted_suntime.index = extracted_suntime.index.map(
        lambda x: x.replace(year=2023)
    )
    extracted_suntime.columns = stations.iloc[closest_stations[0], 0]
    extracted_suntime["Daily suntime (Hours)"] = sum(
        weights[i] * extracted_suntime.loc[:, el]
        for i, el in enumerate(stations.iloc[closest_stations[0], 0])
    )
    extracted_suntime = extracted_suntime.rolling(7, center=True).mean()
    fig_suntime = px.line(extracted_suntime, y="Daily suntime (Hours)")
    figs = [fig_suntime]
    ### Precipitation
    precip = pd.read_csv(
        f"data/{zone}_precip.csv",
        index_col=1,
        parse_dates=[1],
        infer_datetime_format=True,
    )

    extracted_precip = pd.concat(
        (
            precip[precip["number_sta"] == sta]["precip"]
            for sta in stations.iloc[closest_stations[0], 0]
        ),
        axis=1,
    ).interpolate("time")

    extracted_precip.index = extracted_precip.index.map(lambda x: x.replace(year=2023))
    extracted_precip.columns = stations.iloc[closest_stations[0], 0]
    extracted_precip["Daily Precipitation (mm)"] = sum(
        weights[i] * extracted_precip.loc[:, el]
        for i, el in enumerate(stations.iloc[closest_stations[0], 0])
    )
    extracted_precip = extracted_precip.rolling(7, center=True).mean()
    fig_precip = px.line(extracted_precip, y="Daily Precipitation (mm)")
    figs.append(fig_precip)

    ### Wind_direction
    wind_direction = pd.read_csv(
        f"data/{zone}_wind_d.csv",
        index_col=1,
        parse_dates=[1],
        infer_datetime_format=True,
    )
    extracted_wind_direction = pd.concat(
        (
            wind_direction[wind_direction["number_sta"] == sta]["dd"]
            for sta in stations.iloc[closest_stations[0], 0]
        ),
        axis=1,
    ).interpolate("time")
    # set extracted_wind_direction index to 2023
    extracted_wind_direction.index = extracted_wind_direction.index.map(
        lambda x: x.replace(year=2023)
    )
    extracted_wind_direction.columns = stations.iloc[closest_stations[0], 0]
    extracted_wind_direction["Daily Wind Direction (°)"] = sum(
        weights[i] * extracted_wind_direction.loc[:, el]
        for i, el in enumerate(stations.iloc[closest_stations[0], 0])
    )
    extracted_wind_direction = extracted_wind_direction.rolling(7, center=True).mean()
    fig_wf = px.line(extracted_wind_direction, y="Daily Wind Direction (°)")
    figs.append(fig_wf)

    ### Wind_force
    wind_force = pd.read_csv(
        f"data/{zone}_wind_f.csv",
        index_col=1,
        parse_dates=[1],
        infer_datetime_format=True,
    )
    extracted_wind_force = pd.concat(
        (
            wind_force[wind_force["number_sta"] == sta]["ff"]
            for sta in stations.iloc[closest_stations[0], 0]
        ),
        axis=1,
    ).interpolate("time")
    # set extracted_wind_force index to 2023
    extracted_wind_force.index = extracted_wind_force.index.map(
        lambda x: x.replace(year=2023)
    )
    extracted_wind_force.columns = stations.iloc[closest_stations[0], 0]
    extracted_wind_force["Daily Wind Force (m/s)"] = sum(
        weights[i] * extracted_wind_force.loc[:, el]
        for i, el in enumerate(stations.iloc[closest_stations[0], 0])
    )
    extracted_wind_force = extracted_wind_force.rolling(7, center=True).mean()
    fig_wf = px.line(extracted_wind_force, y="Daily Wind Force (m/s)")
    figs.append(fig_wf)

    stations["selected"] = False
    stations.loc[closest_stations[0], "selected"] = True

    fig_sta = plot_selected_stations(stations[stations.zone == zone], lat, lon)

    with st.expander("Show stations"):
        st.plotly_chart(fig_sta, use_container_width=True)

    st.subheader("Yearly average")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Suntime (Hours)",
            extracted_suntime["Daily suntime (Hours)"].mean().__format__("0.2f"),
        )

    with col2:
        st.metric(
            "Precipitation (mm)",
            extracted_precip["Daily Precipitation (mm)"].mean().__format__("0.2f"),
        )

    with col3:
        st.metric(
            "Wind Direction (°)",
            extracted_wind_direction["Daily Wind Direction (°)"]
            .mean()
            .__format__("0.2f"),
        )

    with col4:
        st.metric(
            "Wind Force (m/s)",
            extracted_wind_force["Daily Wind Force (m/s)"].mean().__format__("0.2f"),
        )

    for fig in figs:
        st.plotly_chart(fig)


def main(adress):
    st.set_page_config(page_title="Meteo", page_icon="🌍")
    st.title("Meteo")
    st.write("This is the meteo page")

    if adress is not None:
        data_bool, lon, lat, place_name = have_data(adress, 41.2, 51.2, -5.5, 9.5)
        if data_bool:
            st.write("We have data for your adress")
            st.write("Your adress is in ", place_name)

            plot_meteo_data(lon, lat)

        else :
            st.write("We don't have data for your adress")
    else:
        st.write("You didn't enter your adress yet")


if __name__ == "__main__":
    try:
        postcode = json.load(open("data/user_data.json"))["postcode"]
    except json.JSONDecodeError:
        postcode = None

    main(adress=postcode)
