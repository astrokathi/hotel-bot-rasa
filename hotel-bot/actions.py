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

from typing import Any, Text, Dict, List

from rasa.core.actions.forms import FormAction
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, Restarted


class RestartConversation(Action):

    def name(self) -> Text:
        return "action_restart"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("Restarting the conversation...")
        return [Restarted()]


# class MyFormAction(FormAction):
#     def name(self) -> Text:
#         return "booking_form"
#
#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         return ["reservation_type", "person_name", "num_people", "start_date", "end_date", "num_rooms"]
#
#     def slot_mappings(self) -> Dict[Text, Any]:
#         return {"reservation_type": self.from_text(),
#                 "person_name": self.from_text(),
#                 "num_people": self.from_text(),
#                 "start_date": self.from_text(),
#                 "end_date": self.from_text(),
#                 "num_rooms": self.from_text()
#                 }
#
#     def submit(
#         self,
#         dispatcher: CollectingDispatcher,
#         tracker: Tracker,
#         domain: Dict[Text, Any],
#     ) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message("Form submitted! Starting a new session.")
#         print("restarting the form")
#         return [
#             SlotSet("reservation_type", None),
#             SlotSet("person_name", None),
#             SlotSet("num_people", None),
#             SlotSet("start_date", None),
#             SlotSet("end_date", None),
#             SlotSet("num_rooms", None)
#         ]
