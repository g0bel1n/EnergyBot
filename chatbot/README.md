# CHATBOT

### what is RASA?
Rasa is an open source implementation for Natural Language Understanding (NLU) and Dual Intent Models and Entity Transformers (DIET). 
It can interact with databases, APIs, conversational streams for interactive learning with neural network reinforcement.

Rasa Conversational AI assistant normally consists of two components: Rasa NLU and Rasa Core. 
Rasa NLU can be treated simply as an ear that takes user input and Rasa Core is like the brain that will make decisions based on user input. 
customers (customer service), or interact with customers (sales and marketing), or do both.

The main advantages of RASA over other chatbots are

Free and open source ; Easy to use;  Highly customisable;
On-premise, deploy on own server/compatible with all cloud platforms;
A growing community; Can be integrated with popular email platforms.

### Why not RASA?

As far as the implementation of EneryBot is concerned, we have abandoned the use of RASA. Indeed, the use of RASA required three (3) terminals: one for the action, a second for the database and a third for the API. 
This required the creation of three dockerfiles and the linking of these files, which was not easy. 
Also, the Bot only recognised a well-defined lexical field and only returned Expressions defined in nlu.yaml and domain.yaml. It was no different from a Question Answer system.



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

The request url is then "http://localhost:5005/webhooks/rest/webhook"

Useful links on RASA:
https://rasa.com/docs/rasa/domain/#slot-mappings
https://www.analyticsvidhya.com/blog/2022/02/a-simple-guide-to-rasa-3-x/
https://medium.com/voice-tech-podcast/how-to-create-chatbot-using-rasa-82954e141ae7
https://sysdig.com/blog/dockerfile-best-practices/

