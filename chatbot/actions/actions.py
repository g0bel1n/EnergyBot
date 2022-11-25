from typing import Any, Text, Dict, List
from rasa_sdk import Tracker, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction

from actions.database_connector import DataUpdate
from actions.testing_slots import email_isValid, zipcode_isValid, civility_isValid, birthyear_isValid, ecoloscore_isValid, workdayoccupation_isValid, consprofile_isValid, maxpower_isValid


class PersonalInfosFormValidation(FormValidationAction):
    """Example of a form validation action."""
    def name(self) -> Text:
        return "validate_personal_data_form"

    def validate_civility(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate civility value."""

        if civility_isValid(value):
            # validation succeeded, set the value of the "civility" slot to value
            return {"civility": value}
        else:
            dispatcher.utter_message(response="utter_wrong_civility")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"civility": None}

    def validate_firstname(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate first name value."""

        if len(value) > 1:
            # validation succeeded, set the value of the "firstname" slot to value
            return {"firstname": value}
        else:
            dispatcher.utter_message(response="utter_wrong_firstname")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"firstname": None}

    def validate_lastname(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate last name value."""

        if len(value) > 1:
            # validation succeeded, set the value of the "lastname" slot to value
            return {"lastname": value}
        else:
            dispatcher.utter_message(response="utter_wrong_lastname")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"lastname": None}

    def validate_zipcode(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate zipcode value."""

        if zipcode_isValid(value):
            # validation succeeded, set the value of the "zipcode" slot to value
            return {"zipcode": value}
        else:
            dispatcher.utter_message(response="utter_wrong_zipcode")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"zipcode": None}

    def validate_email(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate email value."""

        if email_isValid(value):
            # validation succeeded, set the value of the "birthyear" slot to value
            return {"email": value}
        else:
            dispatcher.utter_message(response="utter_wrong_email")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"email": None}

    def validate_birthyear(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate birthyear value."""

        if birthyear_isValid(value):
            # validation succeeded, set the value of the "birthyear" slot to value
            return {"birthyear": value}
        else:
            dispatcher.utter_message(response="utter_wrong_birthyear")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"birthyear": None}

    def validate_ecoloscore(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate ecoloscore value."""

        if ecoloscore_isValid(value):
            # validation succeeded, set the value of the "ecoloscore" slot to value
            return {"ecoloscore": value}
        else:
            dispatcher.utter_message(response="utter_wrong_ecoloscore")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"ecoloscore": None}

    def validate_workdayoccupation(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate workdayoccupation value."""

        if workdayoccupation_isValid(value):
            # validation succeeded, set the value of the "workdayoccupation" slot to value
            return {"workdayoccupation": value}
        else:
            dispatcher.utter_message(response="utter_wrong_workdayoccupation")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"workdayoccupation": None}

    def validate_maxpower(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate maxpower value."""

        if maxpower_isValid(value):
            # validation succeeded, set the value of the "maxpower" slot to value
            return {"maxpower": value}
        else:
            dispatcher.utter_message(response="utter_wrong_maxpower")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"maxpower": None}

    def validate_consprofile(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate consprofile value."""

        if consprofile_isValid(value):
            # validation succeeded, set the value of the "consprofile" slot to value
            return {"consprofile": value}
        else:
            dispatcher.utter_message(response="utter_wrong_consprofile")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"consprofile": None}


class ActionSubmitForm(Action):

    def name(self) -> Text:
        return "action_submit_form"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
     ) -> List[Dict]:

        DataUpdate(
            tracker.get_slot("civility"), tracker.get_slot("lastname"), 
            tracker.get_slot("firstname"), tracker.get_slot("email"), 
            tracker.get_slot("zipcode"), tracker.get_slot("birthyear"),
            tracker.get_slot("ecoloscore"), tracker.get_slot("workdayoccupation"), 
            tracker.get_slot("maxpower"), tracker.get_slot("consprofile"))

        dispatcher.utter_message(template="utter_submit")
        return []

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions
