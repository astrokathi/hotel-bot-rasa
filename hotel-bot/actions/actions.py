from typing import Any, Text, Dict, List

from rasa.core.actions.forms import FormAction, Event
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import Restarted


class RestartConversation(Action):

    def name(self) -> Text:
        return "action_restart"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template='utter_anything_else')
        return [Restarted()]
