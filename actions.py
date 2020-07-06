# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from question_find import SimilarityFinder
from question_find import writeToExcel
import time
import nltk
nltk.download('punkt')
# class ActionQuestionAsk(Action):

#     def name(self) -> Text:
#         return "action_question_ask"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        
#         # search_doc = nlp("what is photosynthesis")
#         # main_doc = nlp("photosynthesis")

#         # search_doc_no_stop_words = nlp(' '.join([str(t) for t in search_doc if not t.is_stop]))
#         # main_doc_no_stop_words = nlp(' '.join([str(t) for t in main_doc if not t.is_stop]))

#         # print(search_doc.similarity(main_doc))

#         # print(tracker.latest_message)

#         # dispatcher.utter_message(text="Checking")

#         return []


        
class ActionQuestionAsk(Action) :
    def name(self) -> Text:
        return "action_question_ask"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
             
        print(tracker.latest_message['text'])
        text=tracker.latest_message['text']
        fa=SimilarityFinder(text)
        time.sleep(15)
        dispatcher.utter_message(fa[0])
        writeToExcel(fa[1])
        return []

class ActionQuestionWithOptionAsk(Action) :
    def name(self) -> Text:
        return "action_question_with_option_ask"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
             
        print(tracker.latest_message['text'])
        text=tracker.latest_message['text']
        fa=SimilarityFinder(text)
        time.sleep(15)
        dispatcher.utter_message(fa[0])
        writeToExcel(fa[1])        
        return []

