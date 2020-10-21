import json
import ibm_watson
#from _future_ import print_function
import json
import os

service=ibm_watson.AssistantV1(
    version='2019-02-28',
    iam_apikey='rHPoGMbSy7JGmQh3-nMKSSY7AbTeQ6PMh8i18DPaQdZb',
    url='https://gateway.watsonplatform.net/assistant/api'
)
'''
response=service.create_workspace(
    name='watson assistant',
    description='Example workspace created via API'
).get_result()
# '''
#Q = raw_input("How may i help you: ")
'''
inputtext = service.message(
	#workspace_id = 'b918a20c-a6cb-40af-b428-0f1101436259',
	workspace_id = '19580f54-86d0-45a4-a418-6b02bd93c711',
	input = {
		'text' : 'collision tweets on the 401'
	}
).get_result()
'''


def createintent(str):
	intent=service.create_intent(
		workspace_id='9874ed31-4034-444a-9a9a-f1607c806801',
		intent= str,
		decription = 'assitant used to filter collision tweets',
		examples=[
			{'text' : 'List collisions that occurred on the ' + str},
			{'text' : 'accidents that happened on the ' + str},
			{'text' : 'what happened on the ' + str},
			{'text' : 'collision tweets that happened on the ' + str},
			{'text' : 'show all tweets related to ' + str},
			{'text' : 'what are the tweets related to ' + str},
			{'text' : str}
		]
	).get_result()
	
	
''''

updateintent= service.update_intent(
	workspace_id='5e93ab40-a7bd-444e-b286-3ff7bd4eecf9',
	intent= '401',
	new_examples = [
		{'text' : 'what happened on the 401'},
		{'text' : 'collision tweets that happened on the 401'}
	]
).get_result()
'''
# entity = service.create_entity(
	# workspace_id='9874ed31-4034-444a-9a9a-f1607c806801',
	# entity='beverage'

if __name__ == '__main__':

	response=service.list_intents(
		workspace_id= '9874ed31-4034-444a-9a9a-f1607c806801'
	).get_result()
	#print(response['workspace_id'])
	print(json.dumps(response, indent=2))
	
	directory = 'C:\Users\Gavincko\Documents\Tweepy Project\python'
	
	for filename in os.listdir(directory):
		if filename.endswith(".csv") and filename.startswith("#"):
			filenamecompressed = filename[:-4].strip()
			filenamecompressed = filenamecompressed.replace("#", "")
			filenamecompressed = filenamecompressed.replace(" ", "")
			filenamecompressed = filenamecompressed.replace("^", "")
			filenamecompressed = filenamecompressed.replace("@", "")
					
			print(filenamecompressed)
			try:
				createintent(filenamecompressed)
			except BaseException as e:
				print("Error on data: %s" % str(e))
				
#print(json.dumps(intent, indent=2))
#print(json.dumps(inputtext, indent=2))

'''
create_workspace_data = {
    "name":  
    "test_workspace",
    "description":
    "integration tests",
    "language":
    "en",
    "intents": [{
        "intent": "#401",
        "description": "string",
        "examples": [{
            "text": "good morning"
        }]
    }],
    "entities": [{
        "entity": "pizza_toppings",
        "description": "Tasty pizza toppings",
        "metadata": {
            "property": "value"
        }
    }],
    "counterexamples": [{
        "text": "string"
    }],
    "metadata": {},
}
'''
