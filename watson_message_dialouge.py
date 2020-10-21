import json
import ibm_watson
import csv_html
import collecting_tweet
from selenium import webdriver
import speech_recognition as sr
import pyaudio
import sys
r = sr.Recognizer()

def watsoninput(driver):
	service=ibm_watson.AssistantV1(
		version='2019-02-28',
		iam_apikey='rHPoGMbSy7JGmQh3-nMKSSY7AbTeQ6PMh8i18DPaQdZb',
		url='https://gateway.watsonplatform.net/assistant/api'
	)
	while(True):
		with sr.Microphone() as source:
			print('Speak anythin')
			try:
				audio = r.listen(source, timeout=2, phrase_time_limit=4)
				input = r.recognize_google(audio)
			except:
				continue
			print("You said : {}".format(input))
			if input == "hey compass" or input=='a compass' or input=="he compass" or input=="compass" or input=="PGA":
				while (True):
		#input = raw_input()
					
					try:	
						print("go ahead I'm listening")
						audio=r.listen(source, timeout=5, phrase_time_limit=5)
						tointent = r.recognize_google(audio)
						print("You said : {}".format(tointent))
			
					except:
						print("Sorry could not recognize what you said try again")
						continue
					if tointent == "quit":
						print("You are leaving the filtration program")
						break
					elif tointent == "close the program":
						print("closing")
						sys.exit()
					response = service.message(
						workspace_id='9874ed31-4034-444a-9a9a-f1607c806801',
						input={
							'text': tointent
						}
					).get_result()
					
					try:
						if (response['intents'][0]['intent'] == 'sortedall_tweets' or response['intents'][0]['intent'] == 'EnvCanada'):
							csv_html.indexhtml(response['intents'][0]['intent']+".csv")
							driver.refresh()
						elif  " cleared " in tointent:
							print("ITS IN THE ELIFF")
							collecting_tweet.filter('CLEARED', "#"+response['intents'][0]['intent']+".csv")
							csv_html.indexhtml("CLEARED.csv")
							driver.refresh()
							
						elif " collisions " in tointent or " collision " in tointent:
							print("This is collisions")
							# collecting_tweet.filter("COLLISION", "#"+response['intents'][0]['intent']+".csv")
							clean_rows=[]
						
							firstline = True
							with open("#"+response['intents'][0]['intent']+".csv") as csv_file:
								csv_reader = csv.reader(csv_file, delimiter=',') #need to remove the entire row!!
								for row in csv_reader:
									if firstline:
										firstline=False
										print(firstline)
										continue
									if 'CLEARED' not in row[3]:
										clean_rows.append(row)
										print(row)
								# csv_file.truncate()			
							with open("onlycollision.csv", 'w') as csv_file:
								csv_writer = csv.writer(csv_file)
								csv_writer.writerow(["User Name","tweet_id","created_at","Tweet_text"])
								csv_writer.writerows(clean_rows)
							csv_html.pandas("onlycollision.csv")	
							csv_html.indexhtml("sortedonlycollision.csv")
							driver.refresh()
										
						else:	
							csv_html.indexhtml("#"+response['intents'][0]['intent']+".csv")
							driver.refresh()
					except:
						print("No intents created for the verbal input")
							
			elif input == "close the program" or input == "stop the program" or input=="Thats enough":
				print "closing"
				sys.exit()
			else:
				continue
		
					
		
		# response = service.message(
			# workspace_id='9874ed31-4034-444a-9a9a-f1607c806801',
			# input={
				# 'text': tointent
			# }
		# ).get_result()

		print(json.dumps(response, indent=2))
		print(type(response))
		print(response.keys())
		#print(len(response['intents'][0]))
		# if input=='clost the program':
			# sys.exit()
		# try:
			# if (response['intents'][0]['intent'] == 'sortedall_tweets'):
				# csv_html.indexhtml(response['intents'][0]['intent']+".csv")
				# driver.refresh()
			# else:	
				# csv_html.indexhtml("#"+response['intents'][0]['intent']+".csv")
				# driver.refresh()
		# except:
			# print("No intents created for the verbal input")
if __name__ == "__main__":
	print("you'll never need this")