import json
import numpy as np
import pickle
import pandas as pd

from .checkers import (
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

from typing import Text

__devices__ = ("fridge", "washingmachine", "dryer", "dishwasher")


class TalkyChatbot:
    def __init__(self, id=1) -> None:
        self.id = id
        with open("talky/script.json", "r") as f:
            self.script = json.load(f)
        self.steps = list(self.script.keys())

        self.is_finished = False

        self.email_check = email_check
        self.postcode_check = postcode_check
        self.birthyear_check = birthyear_check
        self.ecoloscore_check = ecoloscore_check
        self.workday_check = workday_check
        self.maxpower_check = maxpower_check
        self.consprofile_check = consprofile_check
        self.npersons_check = npersons_check
        self.device_check = device_check

        self.steps_to_ask = self.steps[1:-1]
        self.n_questions = len(self.steps_to_ask)
        self.rng = np.random.default_rng()

        self.current_step = "greetings"

        self.data = {}

    def greetings(self) -> Text:
        return [self.script["greetings"]["question"]]

    def _get_next_step(self):
        if len(self.steps_to_ask) == 0:
            self.is_finished = True
            return None
        nxt_step = self.rng.choice(self.steps_to_ask)
        self.steps_to_ask.remove(nxt_step)
        return nxt_step

    def _save_data(self):
        """
        It checks that the number of questions answered is equal to the number of questions in the survey,
        and if so, it saves the data to a file
        """
        assert (
            len(self.data.keys()) == self.n_questions
        ), "Not all questions were answered"
        with open("data/user_data.json", "w") as f:
            json.dump(self.data, f)

    def _check(self, *args):
        return getattr(
            self,
            f"{'device' if self.current_step in __devices__ else self.current_step}_check",
        )(*args)

    """
    It checks if the input text is valid for the current step
    
    :param input_text: The user's input
    :type input_text: Text
    :return: True or False
    """

    def _is_valid(self, input_text: Text) -> bool:
        if self.current_step == "greetings":
            return True
        for el in input_text.split():
            if self._check(el):
                self.data[self.current_step] = el
                return True
        return False

    def process_answer(self, input_text: Text):
        """
        It takes the user's input, checks if it's valid, and returns a list of strings to be sent to the
        user
        
        :param input_text: The user's input text
        :type input_text: Text
        :return: A list of strings.
        """
        if a := self._is_valid(input_text):
            answer = [self.script[self.current_step]["ok"]]
            self.current_step = self._get_next_step()
            if self.current_step is None:
                self._save_data()
                answer += [self.script["end"]]
            else:
                answer += [self.script[self.current_step]["question"]]
        else:
            answer = [
                self.script[self.current_step]["error"],
                self.script[self.current_step]["question"],
            ]

        return answer

    @staticmethod
    def _load_model():
        return pickle.load(open("model/rf.pkl", "rb"))

    def get_prediction(self):
        """
        It loads the model, creates a dataframe with the data, and then predicts the consumption.
        """
        rf = self._load_model()
        x = np.array(
            [self.data["ecoloscore"], self.data["workday"]]
            + [self.data[el] for el in __devices__]
            + [self.data["npersons"]]
        ).reshape(1, -1)
        fnames = [  # To fix features name warning
            "ecolo score",
            "worday",
            *[f"paysage_{i}" for i in range(4)],
            "nb_habitant",
        ]
        x = pd.DataFrame(x, columns=fnames)
        pred = rf.predict(x)

        return f"Your energy consumption is estimated to be {pred[0]:.2f} kWh per day"

    def get_recommendation(self):
        """
        It returns a list of strings, each string being a recommendation for the user. If the user has no
        recommendations, it returns a list with one element, the string "You are doing great!"
        :return: A list of strings.
        """
        recommandation = []
        if float(self.data["fridge"]) > 5:
            recommandation.append("You should buy a fridge with a better energy label")
        if float(self.data["washingmachine"]) > 5:
            recommandation.append(
                "You should buy a washing machine with a better energy label"
            )
        if float(self.data["dryer"]) > 5:
            recommandation.append("You should buy a dryer with a better energy label")
        if float(self.data["dishwasher"]) > 5:
            recommandation.append(
                "You should buy a dishwasher with a better energy label"
            )

        return recommandation or ["You are doing great!"]


if __name__ == "__main__":
    chatbot = TalkyChatbot()
    while not chatbot.is_finished:
        print(chatbot.process_answer(input()))
