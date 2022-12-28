<h1 align="center">
  EnergyBot
  <br/>
</h1>


<p align="center">EnergyBot is a Python Project for Ensae's Cloud Computing course <br/> </p>

---
<p align="center">
<a href="https://github.com/g0bel1n/EnergyBot/actions/workflows/energybot_test.yml" 
target="_blank"><img src="https://img.shields.io/github/actions/workflow/status/g0bel1n/EnergyBot/energybot_test.yml?label=Tests&style=for-the-badge" alt="Tests" /></a>
<a href="https://github.com/g0bel1n/EnergyBot/actions/workflows/docker-builder.yml" 
target="_blank"><img src="https://img.shields.io/github/actions/workflow/status/g0bel1n/EnergyBot/docker-builder.yml?label=Docker%20Build&style=for-the-badge" alt="Tests" /></a>
<a href="https://github.com/g0bel1n/EnergyBot/actions/workflows/gitlab_mirror.yml" 
target="_blank"><img src="https://img.shields.io/github/actions/workflow/status/g0bel1n/EnergyBot/gitlab_mirror.yml?label=GitLab%20Mirror&style=for-the-badge" alt="Tests" /></a>
</p>

<p align="center">
<img src="https://img.shields.io/github/license/g0bel1n/EnergyBot?style=for-the-badge" alt="Licence MIT" />
<img src="https://img.shields.io/github/repo-size/g0bel1N/EnergyBot?style=for-the-badge" alt="Size" />
<a href="https://www.python.org/downloads/release/python-390/" 
target="_blank"><img src="https://img.shields.io/badge/python-3.9-blue.svg?style=for-the-badge" alt="Python Version" /></a>
</p>

---

## Onboarding 


## The repo in details

### Meteo Data
blablabla

EnergyBot |
          |- consumption_prediction
          |- EnergyBotApp  

run at level EnergyBot

```
docker build -t energybot1 . 
```

to download and process the data 

```
chmod +x meteo/get_data.sh  data_setup.sh
./data_setup.sh -y 2018
```

