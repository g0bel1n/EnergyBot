from actions.database_connector import DataUpdate
from typing import Any, Text, Dict, List
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import EventType


class PersonalInfosFormValidation(FormValidationAction):
    """Example of a form validation action."""
    def name(self) -> Text:
        return "validate_personal_data_form"

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
     ) -> List[Dict]:

        dispatcher.utter_message(template="utter_submit")

        DataUpdate(
            tracker.get_slot("firstname"), tracker.get_slot("lastname"),
            tracker.get_slot("email"), tracker.get_slot("zipcode"))
        return []

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
