## happy path
* greet
  - utter_greet
* question
  - action_question_ask

## sad path 1
* greet
  - utter_greet
* question
  - action_question_ask
* affirm
  - utter_happy

## happy path 3
* greet
  - utter_greet
* question
  - action_question_ask
* question
  - action_question_ask
  * question
  - action_question_ask
* deny
  - utter_goodbye

## say goodbye
* question
  - action_question_ask
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
