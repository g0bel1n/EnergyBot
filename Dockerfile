FROM python:3.9-slim

ADD ./EnergyBotApp .
COPY . .

RUN pip install --upgrade pip && pip install -r requirements.txt 

WORKDIR ./EnergyBotApp

RUN chmod +x data_setup.sh meteo/get_data.sh  \
    && apt-get update \
    && apt-get install -y wget unzip \
    && ./data_setup.sh -y 2018 \

EXPOSE 8501

CMD ["streamlit run", "interface/streamlit_app.py"]
