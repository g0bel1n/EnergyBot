import csv
import datetime

import requests
from bs4 import BeautifulSoup

url = "https://www.date-pratique.fr/heure-lever-coucher-soleil.html"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html5lib")


table = soup.find("div", attrs={"class": "table-responsive-sm text-center col-xl-6"})

sun_hours = []
day = datetime.datetime(2022, 1, 1)
rows = table.findAll("td", attrs={"class": "align-middle"})
for sunrise, sunset in zip(rows[::2], rows[1::2]):

    _sunhour = {"date": day}
    sunrise_h, sunrise_m = sunrise.text.split("h")
    _sunhour["sunrise"] = day + datetime.timedelta(
        hours=int(sunrise_h), minutes=int(sunrise_m)
    )
    sunset_h, sunset_m = sunset.text.split("h")

    _sunhour["sunset"] = day + datetime.timedelta(
        hours=int(sunset_h), minutes=int(sunset_m)
    )
    sun_hours.append(_sunhour)
    day += datetime.timedelta(1)

filename = "data/sunhours22.csv"


with open(filename, "w", newline="") as f:
    w = csv.DictWriter(f, ["date", "sunrise", "sunset"])
    w.writeheader()
    for row in sun_hours:
        w.writerow(row)

