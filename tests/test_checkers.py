from EnergyBotApp import (
    email_check,
    postcode_check,
    birthyear_check,
    ecoloscore_check,
    workday_check,
    maxpower_check,
    consprofile_check,
    npersons_check,
    device_check,
)

import pytest

@pytest.mark.parametrize(
    "email, is_valid",
    [("jeanbon@gmail.com", True), ("jeanbon@gmail", False), ("jeanbon", False)],
)
def test_email_check(email, is_valid):
    assert email_check(email) == is_valid

@pytest.mark.parametrize(
    "postcode, is_valid",
    [("13001", True), ("7500", False), ("7500A", False), ("7500 1", False)],
)  
def test_postcode_check(postcode, is_valid):
    assert postcode_check(postcode) == is_valid

@pytest.mark.parametrize(
    "birthyear, is_valid",
    [("1990", True), ("199", False), ("199A", False), ("1990-01-01", False)],
)
def test_birthyear_check(birthyear, is_valid):
    assert birthyear_check(birthyear) == is_valid

@pytest.mark.parametrize(
    "ecoloscore, is_valid",
    [("10", False), ("1", True), ("A", False), ("1A", False)],
)
def test_ecoloscore_check(ecoloscore, is_valid):
    assert ecoloscore_check(ecoloscore) == is_valid

@pytest.mark.parametrize(
    "workday, is_valid",
    [("25", False), ("1", True), ("A", False), ("1A", False)],
)
def test_workday_check(workday, is_valid):
    assert workday_check(workday) == is_valid

@pytest.mark.parametrize(
    "maxpower, is_valid",
    [("100", False), ("9", True), ("3", True), ("8", False)],
)
def test_maxpower_check(maxpower, is_valid):
    assert maxpower_check(maxpower) == is_valid

@pytest.mark.parametrize(
    "consprofile, is_valid",
    [("RES1", True), ("RES11", True), ("RES2", True), ("RES3", False), ("RES", False)],
)
def test_consprofile_check(consprofile, is_valid):
    assert consprofile_check(consprofile) == is_valid

@pytest.mark.parametrize(
    "npersons, is_valid",
    [("1", True), ("2", True), ("0", False), ("A", False), ("1A", False)],
)
def test_npersons_check(npersons, is_valid):
    assert npersons_check(npersons) == is_valid

@pytest.mark.parametrize(
    "device, is_valid",
    [("1", True), ("2", True), ("-1", False), ("A", False), ("1A", False)],
)
def test_device_check(device, is_valid):
    assert device_check(device) == is_valid


