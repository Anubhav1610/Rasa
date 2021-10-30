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
                break

        message = "Please Enter Correct State Name !"

        if state == "india" or state == "India":
            d = "2021-10-10"
            for data in responses["data"]:
               a = 0
               if (data["day"] == d):
                  for dt in data["summary"].values():
                     a = a+1
                     if(a == 2):
                         x = dt
                     if(a == 4):
                         y = dt
                     if(a == 5):
                         z = dt
                         break
            message = "Active Cases For --> India on: 2021-10-10 was " + str(x-y-z)
        
        else:    
           for data in responses["data"]:
              for dt in data["regional"]:
                 if (dt["loc"] == state and data["day"] == "2021-10-10"):  #2021-10-10 is the last day in the Api
                    message = "Active Cases For --> " + state + ", on: 2021-10-10 was " + str(dt["confirmedCasesIndian"]-(dt["discharged"]+dt["deaths"]))
        
        print(message)
        dispatcher.utter_message(message)

        return []

class ActionSearchCasesOnDate(Action):

    def name(self) -> Text:
        return "action_search_cases_ondate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        responses = requests.get("https://api.rootnet.in/covid19-in/stats/history").json()

        entities = tracker.latest_message['entities']
        print("Now Showing Data For:", entities)
        state = None

        for i in entities:
            if i["entity"] == "day":
                day = i["value"]

        message = "Please Enter Correct Date !"

        
        for data in responses["data"]:
               a = 0
               if (data["day"] == day):
                  for dt in data["summary"].values():
                     a = a+1
                     if(a == 2):
                         x = dt
                     if(a == 4):
                        y = dt
                     if(a == 5):
                        z = dt
                        break

        message = "As Per Data On: " + str(day) + " Active Cases in India was "  + str(x-y-z)
            

        print(message)
        dispatcher.utter_message(message)

        return []

class ActionSearchCasesOnDate2(Action):

    def name(self) -> Text:
        return "action_search_cases_ondate2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        responses = requests.get("https://api.rootnet.in/covid19-in/stats/history").json()

        entities = tracker.latest_message['entities']
        print("Now Showing Data For:", entities)
        state = None

        for i in entities:
            if i["entity"] == "day":
                day1 = i["value"]
                break


        a = 0

        for i in entities:
            if i["entity"] == "day":
                a = a+1
                if a == 2:
                   day2 = i["value"]
                

        message = "Please Enter Correct Date !"

        
        for data in responses["data"]:
               a = 0
               if (data["day"] == day1):
                  for dt in data["summary"].values():
                     a = a+1
                     if(a == 2):
                         x = dt
                     if(a == 4):
                        y = dt
                     if(a == 5):
                        z = dt
                        break
        d1 = x-y-z

        for data in responses["data"]:
               a = 0
               if (data["day"] == day2):
                  for dt in data["summary"].values():
                     a = a+1
                     if(a == 2):
                         x = dt
                     if(a == 4):
                        y = dt
                     if(a == 5):
                        z = dt
                        break
        d2 = x-y-z

        message = "Cases from " + str(day1) + " to " + str(day2) + " was "  + str(d1+d2)
            

        print(message)
        dispatcher.utter_message(message)

        return []

class ActionSearchNoPatients2(Action):

    def name(self) -> Text:
        return "action_search_no_patients2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        responses = requests.get("https://api.rootnet.in/covid19-in/stats/history").json()

        entities = tracker.latest_message['entities']
        print("Now Showing Data For:", entities)
        state1 = None
        state2 = None

        for i in entities:
            if i["entity"] == "state":
                state1 = i["value"]
                break

        a = 0
        for i in entities:
            if i["entity"] == "state":
                a = a+1
                if a == 2:
                    state2 = i["value"]
                    break


        message = "Please Enter Correct State Name !"

        for data in responses["data"]:
            for dt in data["regional"]:
                 if (dt["loc"] == state1 and data["day"] == "2021-10-10"):
                      x = dt["confirmedCasesIndian"]-(dt["discharged"]+dt["deaths"])
                      break

        for data in responses["data"]:
            for dt in data["regional"]:
                 if (dt["loc"] == state2 and data["day"] == "2021-10-10"):
                      y = dt["confirmedCasesIndian"]-(dt["discharged"]+dt["deaths"])
                      break

        message = "Combined cases of " + state1 + " and " + state2 + " on 2021-10-10 was " + str(x+y) 


        print(message)
        dispatcher.utter_message(message)

        return []

class ActionSearchCasesOnDatename(Action):

    def name(self) -> Text:
        return "action_search_cases_ondatename"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        responses = requests.get("https://api.rootnet.in/covid19-in/stats/history").json()

        entities = tracker.latest_message['entities']
        print("Now Showing Data For:", entities)
        state1 = None
        state2 = None

        for i in entities:
            if i["entity"] == "month":
                month = i["value"]
            if i["entity"] == "monthday":
                day = i["value"]

        month = month.lower()
        month = month[:3]
        
        if month != '':
          if month == 'jan':
            date = '2021-01-'

          if month == 'feb':
            date = '2021-02-'

          if month == 'mar':
            date = '2021-03-'

          if month == 'apr':
            date = '2021-04-'

          if month == 'may':
            date = '2021-05-'

          if month == 'jun':
            date = '2021-06-'
          
          if month == 'jul':
            date = '2021-07-'

          if month == 'aug':
            date = '2021-08-'

          if month == 'sep':
            date = '2021-09-'

          if month == 'oct':
            date = '2021-10-'

          if month == 'nov':
            date = '2021-11-'

          if month == 'dec':
            date = '2021-12-'
          
        date = date + str(day)
        

        message = "Please Enter Correct State Name !"

        for data in responses["data"]:
               a = 0
               if (data["day"] == day):
                  for dt in data["summary"].values():
                     a = a+1
                     if(a == 2):
                         x = dt
                     if(a == 4):
                        y = dt
                     if(a == 5):
                        z = dt
                        break

        message = "As Per Data On: " + str(day) + " Active Cases in India was "  + str(x-y-z)
        

        print(message)
        dispatcher.utter_message(message)

        return []

class ActionSearchCasesOnDatenameAndState(Action):

    def name(self) -> Text:
        return "action_search_cases_ondatename_and_state"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        responses = requests.get("https://api.rootnet.in/covid19-in/stats/history").json()

        entities = tracker.latest_message['entities']
        print("Now Showing Data For:", entities)
        month = ''
        date = ''
        state = ''
        day = 0

        for i in entities:
            if i["entity"] == "month":
                month = i["value"]
            if i["entity"] == "monthday":
                day = i["value"]
            if i["entity"] == "state":
                state = i["value"]


        month = month.lower()
        month = month[:3]
        
        if month != '':
          if month == 'jan':
            date = '2021-01-'

          if month == 'feb':
            date = '2021-02-'

          if month == 'mar':
            date = '2021-03-'

          if month == 'apr':
            date = '2021-04-'

          if month == 'may':
            date = '2021-05-'

          if month == 'jun':
            date = '2021-06-'
          
          if month == 'jul':
            date = '2021-07-'

          if month == 'aug':
            date = '2021-08-'

          if month == 'sep':
            date = '2021-09-'

          if month == 'oct':
            date = '2021-10-'

          if month == 'nov':
            date = '2021-11-'

          if month == 'dec':
            date = '2021-12-'
          
        date = date + str(day)
        

        message = "Please Enter Correct State Name !"

        if state == "india" or state == "India":
            for data in responses["data"]:
               a = 0
               if (data["day"] == date):
                  for dt in data["summary"].values():
                     a = a+1
                     if(a == 2):
                         x = dt
                     if(a == 4):
                         y = dt
                     if(a == 5):
                         z = dt
                         break
            message = "Active Cases For --> India on: " + str(date) + " was " + str(x-y-z)
        
        else:    
           for data in responses["data"]:
              for dt in data["regional"]:
                 if (dt["loc"] == state and data["day"] == "2021-10-10"):  #2021-10-10 is the last day in the Api
                    message = "Active Cases For --> " + state + ", on: " + str(state) + " was " + str(dt["confirmedCasesIndian"]-(dt["discharged"]+dt["deaths"]))
        
        

        print(message)
        dispatcher.utter_message(message)

        return []

class ActionSearchCasesOnDateAndState(Action):

    def name(self) -> Text:
        return "action_search_cases_ondate_and_state"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        responses = requests.get("https://api.rootnet.in/covid19-in/stats/history").json()

        entities = tracker.latest_message['entities']
        print("Now Showing Data For:", entities)
        month = ''
        date = ''
        state = ''
        day = 0

        for i in entities:
            if i["entity"] == "day":
                date = i["value"]
            if i["entity"] == "state":
                state = i["value"]

        message = "Please Enter Correct State Name !"

        if state == "india" or state == "India":
            for data in responses["data"]:
               a = 0
               if (data["day"] == date):
                  for dt in data["summary"].values():
                     a = a+1
                     if(a == 2):
                         x = dt
                     if(a == 4):
                         y = dt
                     if(a == 5):
                         z = dt
                         break
            message = "Active Cases For --> India on: " + str(date) + " was " + str(x-y-z)
        
        else:    
           for data in responses["data"]:
              for dt in data["regional"]:
                 if (dt["loc"] == state and data["day"] == "2021-10-10"):  #2021-10-10 is the last day in the Api
                    message = "Active Cases For --> " + state + ", on: " + str(state) + " was " + str(dt["confirmedCasesIndian"]-(dt["discharged"]+dt["deaths"]))
        
        

        print(message)
        dispatcher.utter_message(message)

        return []