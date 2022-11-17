from actions.database_connector import DataUpdate
from typing import Any, Text, Dict, List
from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
# from rasa_sdk.events import EventType


class PersonalInfosFormValidation(FormValidationAction):
    """Example of a form validation action."""
    def name(self) -> Text:
        return "validate_personal_data_form"

    def validate_lastname(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate last name value."""

        if len(value) > 1:
            # validation succeeded, set the value of the "size" slot to value
            return {"lastname": value}
        else:
            dispatcher.utter_message(response="utter_wrong_lastname")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"lastname": None}

    def validate_firstname(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate first name value."""

        if len(value) > 1:
            # validation succeeded, set the value of the "size" slot to value
            return {"firstname": value}
        else:
            dispatcher.utter_message(response="utter_wrong_firstname")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"firstname": None}

    def validate_email(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate email value."""

        if len(value) > 1:
            # validation succeeded, set the value of the "size" slot to value
            return {"email": value}
        else:
            dispatcher.utter_message(response="utter_wrong_email")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"email": None}

    def validate_zipcode(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate zipcode value."""

        if len(value) == 5:
            # validation succeeded, set the value of the "size" slot to value
            return {"zipcode": value}
        else:
            dispatcher.utter_message(response="utter_wrong_zipcode")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"zipcode": None}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
     ) -> List[Dict]:

        DataUpdate(
            tracker.get_slot("firstname"), tracker.get_slot("lastname"),
            tracker.get_slot("email"), tracker.get_slot("zipcode"))

        dispatcher.utter_message(template="utter_submit")
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
