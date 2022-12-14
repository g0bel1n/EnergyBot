import pandas as pd

df_NW = pd.read_csv(
    "data/NW2018.csv", chunksize=248, parse_dates=[4], infer_datetime_format=True
)
df_SE = pd.read_csv(
    "data/SE2018.csv", chunksize=482, parse_dates=[4], infer_datetime_format=True
)

# drop nan

NW_data = next(df_NW).dropna()
SE_data = next(df_SE).dropna()

NW_stations_id = NW_data.iloc[:, :4]
SE_stations_id = SE_data.iloc[:, :4]

NW_stations_id["zone"] = "NW"
SE_stations_id["zone"] = "SE"

unique_sta = pd.concat([NW_stations_id, SE_stations_id], ignore_index=True)

unique_sta.to_csv("data/unique_station.csv")
