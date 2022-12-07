FROM python:3.9-slim

# create a conda env with required modules
RUN conda env create -f environments.yml

# Copy project files on the Docker image
WORKDIR /chatbot
COPY . .

# Set the user to run
USER 1001

RUN rasa train nlu

# Set entry point for interactive shells
ENTRYPOINT [ "rasa" ]

# Command to run when container is called to run
CMD [ "run", "--enable-api", "--port", "8080" ]
