import re
from typing import Text
import pandas as pd


def civility_check(civility: Text) -> bool:
    return civility in ["MR", "MME"]


def email_check(email: Text) -> bool:
    regex = re.compile(
        r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+"
    )
    return re.fullmatch(regex, email)


def postcode_check(postcode: Text) -> bool:
    list_zip_codes = pd.read_csv("data/commune2021.csv")["COM"].unique()
    return str(postcode) in list_zip_codes


def birthyear_check(birthyear: Text) -> bool:
    return 1922 <= int(birthyear) <= 2004 if birthyear.isnumeric() else False


def ecoloscore_check(ecoloscore: Text) -> bool:
    return int(ecoloscore) in {1, 2, 3, 4, 5} if ecoloscore.isnumeric() else False


def workday_check(workday: Text) -> bool:
    return float(workday)<24 if workday.isnumeric() else False


def maxpower_check(maxpower: Text) -> bool:
    if maxpower.isnumeric():
        return int(maxpower) % 3 == 0 and int(maxpower) <= 36
    return False


def consprofile_check(consprofile: Text) -> bool:
    return consprofile in ["RES1", "RES11", "RES2"]


def npersons_check(npersons: Text) -> bool:
    return npersons.isnumeric() and int(npersons) > 0

def device_check(device: Text) -> bool:
    return device.isnumeric() and int(device) >= 0