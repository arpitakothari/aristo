## happy path
* greet
  - utter_greet
* question
  - utter_wait
  - action_question_ask
  - utter_did_that_help

## sad path 1
* greet
  - utter_greet
* question
  - utter_wait
  - action_question_ask
  - utter_did_that_help
* affirm
  - utter_happy

## happy path 3
* greet
  - utter_greet
* question
  - utter_wait
  - action_question_ask
* question
  - utter_wait
  - action_question_ask
* question
  - utter_wait
  - action_question_ask
  - utter_did_that_help
* deny
  - utter_regret

## say goodbye
* question
  - utter_wait
  - action_question_ask
* goodbye
  - utter_goodbye

<!-- ## happy path
* greet
  - utter_greet
* QuestionWithOption
  - action_question_with_option_ask

## sad path 1
* greet
  - utter_greet
* QuestionWithOption
  - action_question_with_option_ask
* affirm
  - utter_happy

## happy path 3
* greet
  - utter_greet
* QuestionWithOption
  - action_question_with_option_ask
* QuestionWithOption
  - action_question_with_option_ask
* QuestionWithOption
  - action_question_with_option_ask
* deny
  - utter_goodbye

## say goodbye
* QuestionWithOption
  - action_question_with_option_ask
* goodbye
  - utter_goodbye
 -->


## bot challenge
* bot_challenge
  - utter_iamabot
