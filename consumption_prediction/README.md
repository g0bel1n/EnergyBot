<h1 align="center">
  EnergyBot/Consumption Prediction
  <br/>
</h1>


<p align="center">This repo is designed for the predictive modelling<br/> </p>

The model here is based on synthetic customers base data since we have not owned real ones. The aim is to predict users' daily average consumption.

| Feature | Type of data | Description | Values/Modalities | 
|-:|:--:|:--:|:-:|
| email | Personal | Email address |  |
| postcode | Personal | Zip code |  |
| max_power | Contractual | Subscribed power of the contract | 3, 6, 9, 12, 15, 18, 24, 30, 36 (kVA) |
| cons_Profile | Contractual | Consumption profile to which belongs the customer, obtained from the contract | RES1, RES11, RES2 |
| ecolo score | Behavioural | Auto-valuation as eco-responsible | INT between 1 and 5 |
| workday | Behavioural | Average number of hours at home for working | INT |
| nb_habitant | Energy Landscape | Number of habitants in the household | INT |
| fridge_power | Energy Landscape | Power of owned fridge | Real expressed in Watt |
| dryer_power | Energy Landscape | Power of owned dryer | Real expressed in Watt  |
| dishwasher_power | Energy Landscape | Power of owned dishwasher | Real expressed in Watt  |
| washing machine_power | Energy Landscape | Power of owned washing machine | Real expressed in Watt  |
| target |  | Average daily consumption over a year  | Real expressed in kWh |

## Data Generation
After framing the data dictionnary and before simulation, we preprocessed raw data which reflect the customer consumption according to some contractual characteritics and published by ENEDIS. Afterwards the simulation made in two parts is first based on input features  generation and then the target construction merely obtained by noising weighted input informations.

## Data Modelling
The model rolled out is a RandomForest with <code>n_estimators=100</code> and the other parameters at theirs default values. The model once fitted is dumped into a pickel file stored in EnergyBot/EnergyBotApp/model/rf.pkl...