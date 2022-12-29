<h1 align="center">
  EnergyBot
  <br/>
</h1>


<p align="center">EnergyBot is a Python Project for Ensae's Cloud Computing course.  I is  a interactive platfrom that estimate your energy consumption and provide it with some additional data such as wind estimations, temperatures, suntime, etc ... <br/> </p>

---
<p align="center">
<img alt="GitHub Workflow Status" src="https://img.shields.io/github/actions/workflow/status/g0bel1n/energybot/energybot_test.yml?label=Test%20%26%20Docker%20build&style=for-the-badge">
<a href="https://github.com/g0bel1n/EnergyBot/actions/workflows/gitlab_mirror.yml" 
target="_blank"><img src="https://img.shields.io/github/actions/workflow/status/g0bel1n/EnergyBot/gitlab_mirror.yml?label=GitLab%20Mirror&style=for-the-badge" alt="Tests" /></a>
</p>

<p align="center">
<img src="https://img.shields.io/github/license/g0bel1n/EnergyBot?style=for-the-badge" alt="Licence MIT" />
<img src="https://img.shields.io/github/repo-size/g0bel1N/EnergyBot?style=for-the-badge" alt="Size" />
<a href="https://www.python.org/downloads/release/python-390/" 
target="_blank"><img src="https://img.shields.io/badge/python-3.9-blue.svg?style=for-the-badge" alt="Python Version" /></a>
<img alt="Docker Image Size (latest by date)" src="https://img.shields.io/docker/image-size/g0bel1n/energybot?style=for-the-badge">
</p>

---

## Onboarding 


```
docker pull g0bel1n/energybot:latest
```
```
docker run -p 8501:8501  -d g0bel1n/energybot:latest
```


## The repo in details

### Continuous integration

We have 2 (and a half) continuous integration (CI) procedures that are launched at every push to the main branch
-  Testing. Pytest collects the test from the tests folder and execute them
   -  if Testing goes through, a Docker Image is built and pushed onto the docker hub
- Mirroring. The commits are shared with course gitlab repositorie


### Meteo Data

The meteo data folder contains the scripts to get meteorological data from various sites. 

The data_setup.sh bash scripts checks which files are missing, and download them as well as process them for the plateform. 
There is two main data provider. Meteonet, which is open-sourced data from MeteoFrance. However, only data for the Northwest and sutheast of France are available. We request the file using a wget command.
The second source is dates-pratiques, a website from which we scrap the sunrise and sunset hours for this year, using BeautifulSoup4.

The advantage of our method is that, we don't need to get data during runtime, so we only have to launch this script once.
Even if the base files are about 3 to 4 GB large, once processed, what we need is aroung 30-40 MB. Therefore we decided to add it to in the Docker Image directly instead of running the bash script. It is faster and does not require to waste data downloading the same files at each build. It is a reasonable trade-off as the docker image is about 300MB.

### Something

EnergyBot 
    |-- consumption_prediction
    |-- EnergyBotApp  

run at level EnergyBot

```
docker build -t energybot1 . 
```

to download and process the data 

```
chmod +x meteo/get_data.sh  data_setup.sh
./data_setup.sh -y 2018
```