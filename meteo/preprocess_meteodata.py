import datetime
import os

import pandas as pd
from tqdm import tqdm

sunhours = pd.read_csv(
    filepath_or_buffer="data/sunhours22.csv",
    infer_datetime_format=True,
    parse_dates=[0, 1, 2],
)
sunhours.set_index("date", inplace=True)

with tqdm(total=10, desc="Processing Meteorological data") as pbar:
    for zone in ("NW", "SE"):
        df = pd.read_csv(
            f"data/{zone}2018.csv",
            parse_dates=[1],
            infer_datetime_format=True,
            usecols=["number_sta", "date", "dd", "ff", "precip", "t"],
        )
        pbar.update()

        df.set_index("date", inplace=True)
        daily_precipitation = (
            df.groupby(by=["number_sta", pd.Grouper(freq="1D")])["precip"]
            .sum()
            .to_csv(f"data/{zone}_precip.csv")
        )
        pbar.update()
        daily_wind_f = (
            df.groupby(by=["number_sta", pd.Grouper(freq="1D")])["ff"]
            .mean()
            .to_csv(f"data/{zone}_wind_f.csv")
        )
        pbar.update()
        daily_wind_d = (
            df.groupby(by=["number_sta", pd.Grouper(freq="1D")])["dd"]
            .mean()
            .to_csv(f"data/{zone}_wind_d.csv")
        )
        pbar.update()
        daily_suntime = []
        for i, (_, _df) in enumerate(df.groupby(by=pd.Grouper(freq="1D"))):
            sunrise, sunset = sunhours.iloc[i]
            
            d_s = (
                _df[
                    (_df.index > sunrise - datetime.timedelta(days=4 * 365.25))
                    & (_df.index < sunset - datetime.timedelta(days=4 * 365.25))
                    & (_df.precip == 0.0)
                ]
                .groupby(by="number_sta")
                .count() /10.
            )
            d_s["date"] = sunrise.normalize()
            daily_suntime.append(d_s[["date", "precip"]])

        pd.concat(daily_suntime).reset_index().set_index("date").to_csv(
            f"data/{zone}daily_suntime.csv"
        )
        pbar.update()

    