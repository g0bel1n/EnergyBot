<h1 align="center">
  EnergyBot/Consumption Prediction
  <br/>
</h1>


<p align="center">This repo is designed for the predictive modelling<br/> </p>

The model here is based on synthetic customer base data since we have not owned real ones. The aim is to predict users' daily average consumption.

| Feature | Type of data | Description | Values/Modalities | 
|-:|:--:|:--:|:-:|
| Cons_Profile | Contractual | Profile to which belongs the customer, obtained from  | RES1, RES11, RES2 |
| subscribed_power | Contractual |  |  |
| ecolo score | Behavioural |  |  |
| worday | Behavioural | Average number of hour spent at home during working days |  |
| nb_habitant |  | Number of habitants in the household | INT |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
| target |  | Average daily consumption over a year  |  |

# Data Generation
After framing the data dictionnary and before simulation, we preprocessed raw data which reflect the customer consumption according to some contractual characteritics and published by ENEDIS. Afterwards the simulation made in two parts is first based on input features  generation and then the target construction merely obtained by noising weighted input informations.

# Data Modelling
The model rolled out is a RandomForest with <code>n_estimators=100<\code> and the other parameters at theirs default values. The model once fitted is dumped into a picke file stored in EnergyBot/EnergyBotApp/model/rf.pkl.