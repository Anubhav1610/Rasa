# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import requests
import json

# The Covid Data Api is hosted on PythonAnywhere Cloud Platform


IP = "https://api.rootnet.in/covid19-in/stats/history"


class ActionSearchNoPatients(Action):

    def name(self) -> Text:
        return "action_search_no_patients"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        responses = requests.get("https://api.rootnet.in/covid19-in/stats/history").json()

        entities = tracker.latest_message['entities']
        print("Now Showing Data For:", entities)
        state = None

        for i in entities:
            if i["entity"] == "state":
                state = i["value"]

        message = "Please Enter Correct State Name !"

        if state == "india":
            state = "Total"
        for data in responses["data"]:
            if data["state"] == state.title():
                print(data)
                message = "Confirmed Cases For --> " + data["regional"[""confirmedCasesIndian"]] + "As Per Data On: " + data[
                              "day"]

        print(message)
        dispatcher.utter_message(message)

        return []

class ActionSearchCasesOnDate(Action):

    def name(self) -> Text:
        return "action_search_cases_ondate"
  
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
      
        day = tracker.get_slot('day')
       
        params = {
  			'day': day
		}

        data = requests.get(IP, params)

        data = data.json()
 
        if(data['status']=='1'):
            confirmed = data['confirmedCasesIndian']
            day = data['day']

            response = """On {} in {}. Confirmed cases: {}""".format(day,"INDIA", confirmed)
        else:
            response = """Invalid date!! Please Try again"""
         
        dispatcher.utter_message(response)


        return []