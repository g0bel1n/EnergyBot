# CHATBOT

To install RASA execute the following lines:

<code>conda create -n rasa-app python=3.9</code>

<code>conda activate rasa-app</code>

<code>pip3 install rasa</code>

To initialize a RASA project:

<code>rasa init --no-prompt</code>

To train a RASA model:

<code>rasa train</code>

To start an interactive session with the bot:

<code>rasa shell --endpoints endpoints.yml</code>

To enable the API for direct interaction with conversation trackers and other bot endpoints, add the --enable-api parameter to your run command:

<code>rasa run -m models --enable-api --debug</code>

The request url is then http://localhost:5005/model/parse

Useful links on RASA:
https://rasa.com/docs/rasa/domain/#slot-mappings
https://www.analyticsvidhya.com/blog/2022/02/a-simple-guide-to-rasa-3-x/
https://medium.com/voice-tech-podcast/how-to-create-chatbot-using-rasa-82954e141ae7
https://sysdig.com/blog/dockerfile-best-practices/
