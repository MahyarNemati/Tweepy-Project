import json
import ibm_watson


service=ibm_watson.AssistantV1(
    version='2019-02-28',
    iam_apikey='rHPoGMbSy7JGmQh3-nMKSSY7AbTeQ6PMh8i18DPaQdZb',
    url='https://gateway.watsonplatform.net/assistant/api'
)

defaultintent=service.create_intent(
	workspace_id='9874ed31-4034-444a-9a9a-f1607c806801',
	intent= 'sortedall_tweets',
	decription = 'to show the default page',
	examples=[
		{'text' : 'back to the recent tweets from all the accounts'},
		{'text' : 'show the default page'},
		{'text' : 'show the home page'},
		{'text' : 'display original page'},
		{'text' : 'Go back to original page'},
		{'text' : "Let's go back to the beginning"}

	]
).get_result()


print(json.dumps(defaultintent, indent=2))