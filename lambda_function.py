from __future__ import print_function
import random
import game

# constants
reprompts = ["Try something else", "Another command please", "Try again"]

# --------------- Helpers ----------------------
def build_speechlet_response(output, should_end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>"+output+"</speak>"
        },
        'shouldEndSession': should_end_session
    }

def build_response(speechlet_response):
    """
    Build the full response JSON from the speechlet response
    """
    return {
        'version': '1.0',
        'sessionAttributes': {},
        'response': speechlet_response
    }

# --------------- Skill behavior ------------------

def play(intent):
    res = game.play(intent)
    toSay = res['toSay']
    finish = res['finish']
    return build_response(build_speechlet_response(toSay, finish))

def reprompt(session):
    return build_response(build_speechlet_response(reprompts[random.randint(0,len(reprompts))-1], False))

def start():
    return build_response(build_speechlet_response(
        game.play("",True), False))

def end():
    return build_response(build_speechlet_response(
        "Game quit", True))

def getInventory():
    inv = game.getInventory()
    toSay = ""
    if (inv is None):
        toSay = "You have diddly squat in your inventory"
    else:   
        toSay = "You have "+ ' '.join(inv)+ " in your inventory"
    return build_response(build_speechlet_response(toSay, False))

# --------------- Events ------------------
def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])

def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they want """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return getStartResponse()

def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "CommandStart":
        return start()
    if intent_name == "DoGame":
        return play(intent_request['intent']['slots'])
    if intent_name =="CommandInventory":
        return getInventory()
    elif intent_name == "AMAZON.HelpIntent":
        return start()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return end("Game saved")
    else:
        return reprompt(session)

def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session. Is not called when the skill returns should_end_session=true """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])

# --------------- Main handler ------------------
def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])

# -- RESPONSE -- 
start_r = {
  "session": {
    "new": False,
    "sessionId": "SessionId.850f9d57-0269-497f-a8a2-494af350863b",
    "application": {
      "applicationId": "amzn1.ask.skill.0a173718-903e-48e5-b0cc-592f61de28a6"
    },
    "attributes": {},
    "user": {
      "userId": "amzn1.ask.account.AHRB4ZWZZ5GBFEUARZGNCN47CZDDVSBX4KNOMUGEPUFSPAOEM2S72DYICBN5YJZZ3MU4G2RWO5XTDCBVJJPI2DTGX4NCOJVSWR6VJ2UWRMLSGIQJBYVNNTL762YIXXXXEVUQSBYONRMMFGK73AAJTTGR7XFVUVF4XEKSV7GENDMIUSKT3WYG3VSXGGKVUPCI6JL2N6TDAGIW5DQ"
    }
  },
  "request": {
    "type": "IntentRequest",
    "requestId": "EdwRequestId.63aff37d-df73-49b8-b3e1-693f8063a3f7",
    "intent": {
      "name": "CommandStart",
      "slots": {}
    },
    "locale": "en-US",
    "timestamp": "2018-01-28T05:56:29Z"
  },
  "context": {
    "AudioPlayer": {
      "playerActivity": "IDLE"
    },
    "System": {
      "application": {
        "applicationId": "amzn1.ask.skill.0a173718-903e-48e5-b0cc-592f61de28a6"
      },
      "user": {
        "userId": "amzn1.ask.account.AHRB4ZWZZ5GBFEUARZGNCN47CZDDVSBX4KNOMUGEPUFSPAOEM2S72DYICBN5YJZZ3MU4G2RWO5XTDCBVJJPI2DTGX4NCOJVSWR6VJ2UWRMLSGIQJBYVNNTL762YIXXXXEVUQSBYONRMMFGK73AAJTTGR7XFVUVF4XEKSV7GENDMIUSKT3WYG3VSXGGKVUPCI6JL2N6TDAGIW5DQ"
      },
      "device": {
        "supportedInterfaces": {}
      }
    }
  },
  "version": "1.0"
}

search_r = {
  "session": {
    "new": False,
    "sessionId": "SessionId.850f9d57-0269-497f-a8a2-494af350863b",
    "application": {
      "applicationId": "amzn1.ask.skill.0a173718-903e-48e5-b0cc-592f61de28a6"
    },
    "attributes": {},
    "user": {
      "userId": "amzn1.ask.account.AHRB4ZWZZ5GBFEUARZGNCN47CZDDVSBX4KNOMUGEPUFSPAOEM2S72DYICBN5YJZZ3MU4G2RWO5XTDCBVJJPI2DTGX4NCOJVSWR6VJ2UWRMLSGIQJBYVNNTL762YIXXXXEVUQSBYONRMMFGK73AAJTTGR7XFVUVF4XEKSV7GENDMIUSKT3WYG3VSXGGKVUPCI6JL2N6TDAGIW5DQ"
    }
  },
  "request": {
    "type": "IntentRequest",
    "requestId": "EdwRequestId.14a35585-fb1b-4b47-8eb8-a9eca383357a",
    "intent": {
      "name": "DoGame",
      "slots": {
        "BLoc": {
          "name": "BLoc"
        },
        "ANoun": {
          "name": "ANoun"
        },
        "CLoc": {
          "name": "CLoc"
        },
        "CNoun": {
          "name": "CNoun"
        },
        "CUsing": {
          "name": "CUsing"
        },
        "BVerb": {
          "name": "BVerb"
        },
        "BNoun": {
          "name": "BNoun",
          "value": "north"
        },
        "AVerb": {
          "name": "AVerb",
          "value": "go"
        },
        "DNoun": {
          "name": "DNoun"
        },
        "BSwitch": {
          "name": "BSwitch"
        }
      }
    },
    "locale": "en-US",
    "timestamp": "2018-01-28T05:57:06Z"
  },
  "context": {
    "AudioPlayer": {
      "playerActivity": "IDLE"
    },
    "System": {
      "application": {
        "applicationId": "amzn1.ask.skill.0a173718-903e-48e5-b0cc-592f61de28a6"
      },
      "user": {
        "userId": "amzn1.ask.account.AHRB4ZWZZ5GBFEUARZGNCN47CZDDVSBX4KNOMUGEPUFSPAOEM2S72DYICBN5YJZZ3MU4G2RWO5XTDCBVJJPI2DTGX4NCOJVSWR6VJ2UWRMLSGIQJBYVNNTL762YIXXXXEVUQSBYONRMMFGK73AAJTTGR7XFVUVF4XEKSV7GENDMIUSKT3WYG3VSXGGKVUPCI6JL2N6TDAGIW5DQ"
      },
      "device": {
        "supportedInterfaces": {}
      }
    }
  },
  "version": "1.0"
}

attack_r = {
  "session": {
    "new": False,
    "sessionId": "SessionId.da1f9049-56f0-498d-9fd0-8055f51fabcc",
    "application": {
      "applicationId": "amzn1.ask.skill.0a173718-903e-48e5-b0cc-592f61de28a6"
    },
    "attributes": {},
    "user": {
      "userId": "amzn1.ask.account.AH5JKB3UIZLYS3GIFJA25Z6YKBSJV2KUO4NZKCAXQ3IBHEJLYJP7IVURZOX5BCPGICTJ3RR3AQOAHRIPXGV7EMAFHGOSXDEJOROU7I77MXWDST5UX3VQXNQHYR6F2M65DFO7ONXUVNFQABCZWIMUOUF2Y6NM3B6TQ7VWH6OGL4DSA4UHDTAZ2L7QUCL7OLIP2IEOBJPKCANKSEA"
    }
  },
  "request": {
    "type": "IntentRequest",
    "requestId": "EdwRequestId.e0c92d5c-3647-4a20-8493-cd9d8aa8a426",
    "intent": {
      "name": "DoGame",
      "slots": {
        "BLoc": {
          "name": "BLoc"
        },
        "ANoun": {
          "name": "ANoun"
        },
        "CLoc": {
          "name": "CLoc"
        },
        "CNoun": {
          "name": "CNoun"
        },
        "CUsing": {
          "name": "CUsing",
          "value": "with"
        },
        "BVerb": {
          "name": "BVerb"
        },
        "BNoun": {
          "name": "BNoun",
          "value": "mutant"
        },
        "AVerb": {
          "name": "AVerb",
          "value": "attack"
        },
        "BSwitch": {
          "name": "BSwitch"
        },
        "DNoun": {
          "name": "DNoun",
          "value": "machete"
        }
      }
    },
    "locale": "en-US",
    "timestamp": "2018-01-28T12:20:11Z"
  },
  "context": {
    "AudioPlayer": {
      "playerActivity": "IDLE"
    },
    "System": {
      "application": {
        "applicationId": "amzn1.ask.skill.0a173718-903e-48e5-b0cc-592f61de28a6"
      },
      "user": {
        "userId": "amzn1.ask.account.AH5JKB3UIZLYS3GIFJA25Z6YKBSJV2KUO4NZKCAXQ3IBHEJLYJP7IVURZOX5BCPGICTJ3RR3AQOAHRIPXGV7EMAFHGOSXDEJOROU7I77MXWDST5UX3VQXNQHYR6F2M65DFO7ONXUVNFQABCZWIMUOUF2Y6NM3B6TQ7VWH6OGL4DSA4UHDTAZ2L7QUCL7OLIP2IEOBJPKCANKSEA"
      },
      "device": {
        "supportedInterfaces": {}
      }
    }
  },
  "version": "1.0"
}

# print(lambda_handler(start_r,""))
print(lambda_handler(search_r,""))
# print(lambda_handler(attack_r,""))