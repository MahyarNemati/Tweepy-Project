import tweepy, datetime, time
import csv
import sys
from selenium import webdriver
import time
import urllib
import urllib2
import operator
import re
import pandas as pd
from prettytable import PrettyTable
import streamingcollectingtweet as streaming
import json
from Tkinter import *
import ScrolledText as tkst
import csv_html
import filterbykeywordwatson as watson
import os
from more_itertools import unique_everseen
#import watson_message_dialouge as watsonmessage
reload(sys)
sys.setdefaultencoding('utf-8')
import threading
import watson_message_dialouge as watsonmessage
from subprocess import call


consumer_key = "7tnMEONXpqg6SBDW4eec62GI0"
consumer_secret = "pDwKxefBmxUW2AGrdzhprkAiDt8BhOTmmiqMd9BIZAoAbkGvEz"
access_key = "925003211425107968-hAdW9BmUd3L71cJevI3J6Wr9CbgD7AH"
access_secret = "yWpysA00PYcBgCgqdtTgqcrA7HR9A1YFSWjCvjePjUYiD"
'''
handles_list = ["Gavincko","ECAlertON143", "ECAlertON128", "ECAlertON12", "ECAlertON14", "ECAlertON107", "ECAlertON125",
                "ECAlertON47", "ECAlertON77", "ECAlertON95", "ECAlertON79", "ECAlertON68", "ECAlertON24",
                "ECAlertON32", "ECAlertON4", "ECAlertON140", "ECAlertON64", "ECAlertON85", "ECAlertON25",
                "ECAlertON54", "ECAlertON119", "ECAlertON117",  "ECAlertON54", "ECAlertON49", "ECAlertON151",
                "ECAlertON150", "ECAlertON169", "ECAlertON13"]
'''

handles_list = []
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)			
#handles_list = ["Gavincko","ECAlertON143", "ECAlertON128", "ECAlertON12"]	
x = PrettyTable()
#recenttweets = []
follow = []
def add():
	status = Label(bottomFrame, text="Account Added", bd=1, relief=SUNKEN, anchor=W) #shows the status of account added
	status.grid(row=6) #where the status is shown 
	account = Entry.get(entryaccount) #gets the string that typed in the entry bar
	userid = api.get_user(account) #uses the api to get the user_id of the account
	handles_list.append(account) #adds the account to a array called "handles_list"
	follow.append(userid.id)  #adds the userid to a array called "follow"
	if(len(handles_list) > 0): #make sure more than one account in handles_list
		txt.delete(1.0, END) #deletes the strings scrolledtext to print more than one account again,
	for i in range(len(handles_list)):
		txt.insert(INSERT, handles_list[i] + "\n") #inputes the account into the scrolledtext box below
		entryaccount.delete(0, 'end') # deletes the text on the entryaccount bar once add is clicked
		
def delete():
	for i in range (0, len(handles_list)):
		handles_list.pop(0) #removes the first element in the handles_list array 
		follow.pop(0)	#removes the index for handles_list and follow not the element, 
	txt.delete(1.0, END) #deletes the scrolledtext area and makes it empty
	
def done():
	with open('all_tweets.csv', 'w') as f_all: #opens a new file called alltweets.csv as write function and its alias is f_all
		writer = csv.writer(f_all) #name the writer method as writer
		writer.writerow(["User Name","tweet_id","created_at","Tweet_text"]) #writes the first row as four colums using writer method
		for handle in handles_list:
			get_all_tweets(handle, writer) #for every account in handles_list array callls the get_all_tweets function
			print ("Done.") #just a check to make sure all accounts went through the function
	##      reader = csv.reader(f_all, delimiter=',')
	##        firstline = reader.next() #if you want to skip first line
	##        sortedlist = sorted(reader, key=operator.itemgetter(4), reverse=True)
	##          for eachline in sortedlist:
	##            print eachline
	with open('datacollection.csv', 'a') as datacollect: #opens a new file called alltweets.csv as write function and its alias is f_all
		datawriter1 = csv.writer(datacollect) #name the writer method as writer
		if(os.stat("datacollection.csv").st_size == 0):
			datawriter1.writerow(["User Name","tweet_id","created_at","Tweet_text"])
		#datawriter.writeheader()
		for handle in handles_list:
			usefordatacollection(handle, datawriter1)
			print("usedfordata")
		
	csv_html.pandas("datacollection.csv")	

	# follow = ['209015814', '2228665344', '3062851607', '3062719421'] 	

	# twitter_streamer = streaming.TwitterStreamer()
	# twitter_streamer.stream_tweets('all_tweets.csv', follow)
	'''
	# with open('sorteddatacollection.csv', 'r') as csvreader:
		# #rowCount = sum(1 for row in csvreader)
		# #print("rowCount: " + str(rowCount))	
		# reader = csv.DictReader(csvreader)
		# for row in reader:
			# print(row["Tweet_text"])
			# watson.textanalysis(row["Tweet_text"])
		# # print("This is the reader variable " + str(reader))
	# csvreader.close()
	'''
	csv_html.pandas("all_tweets.csv")
	csv_html.indexhtml('sortedall_tweets.csv')
	

	
	# with open('sorteddatacollection.csv', 'r') as analyzetext:
		# reader = csv.DictReader(analyzetext)
		# for row in reader:
			# print(row["Tweet_text"])
	
	
		##    with open('all_tweets.csv', 'r') as f_all:
		##        reader = csv.reader(f_all, delimiter=',')
		##        #can combine both above like reader = csv.reader(open('all_tweets.csv'),delimiter=',')
		##        firstline = reader.next()
		##        sortedlist =  sorted(reader, key=operator.itemgetter(3)) to s
		##        #print(sortedlist)


		##    with open("all_tweets.csv", "wb") as f:
		##        fileWriter = csv.writer(f, delimiter=',')
		##        fileWriter.writerow(["User Name","Twitter_Handle","Twitter_User_Description","tweet_id","created_at","Tweet_text"])
		##        for row in sortedlist:
		##            fileWriter.writerow(row)
		##        

	#follow = ['209015814', '2228665344', '3062851607', '3062719421'] 	
	driver = webdriver.Chrome("C:/Users/Matrix/Downloads/chromedriver_win32/chromedriver.exe")
	driver.get("file:///C:/Users/Matrix/Desktop/FinalTweepy/table.html")
	root.destroy() # destroys root
	followstr = map(str, follow) #makes the user id in to string method
	print(followstr)#check if string in command prompt
			
	thread = threading.Thread(target=watsonmessage.watsoninput, args=(driver,))

	thread.start()
	twitter_streamer = streaming.TwitterStreamer() #creates an object called from teh streamingcollectingtwee tfile to twitter streamer
	twitter_streamer.stream_tweets('all_tweets.csv', 'datacollection.csv', followstr, driver)	#call stream_tweet method in streamingcollecting tweet file
	#print("This is after streaming")
'''	
	return

	def html_code(line):
			line = line.split(',')
			x.add_row([line[0], line[1], line[2], line[3]])
	
def indexhtml():
	csv_file = open('/Users/Gavincko/Documents/Tweepy Project/python/sorted.csv' , 'r') 
	csv_file = csv_file.readlines()

	row_count =  sum(1 for row in csv_file)

	fieldnames = csv_file[0].split(',')
	x.field_names = [fieldnames[0], fieldnames[1], fieldnames[2], fieldnames[3]]

	for i in range (1, row_count):
			line = csv_file[i]

			print line
			html_code(line)

			
	html_code = x.get_html_string()
	html_file = open('/Users/Gavincko/Documents/Tweepy Project/python/table.html', 'w')
	html_file = html_file.write(html_code)
'''			
def datetime_from_utc_to_local(utc_datetime):
	now_timestamp = time.time()
	offset = datetime.datetime.fromtimestamp(now_timestamp) - datetime.datetime.utcfromtimestamp(now_timestamp)
	return utc_datetime + offset

def onlyissued(thetweets):
	issued = []
	ended = []
	for atweet in thetweets:
		
		tweet = atweet.text.encode("utf-8")
	
		if('issued' in tweet):
			  #filt= tweet.replace('issued ', '')
			  issued.append(atweet)
			  

		elif('ended' in tweet):
			#end = tweet.replace('ended ', '')
			ended.append(atweet)
				 
	for tweet in ended:
		endword = tweet.text.encode("utf-8").split()
		length = len(endword) - 2
     
		for tweeti in issued:
			temp=0
			filtword = tweeti.text.encode("utf-8").split();
          
			for i in range(0, len(endword)):
				if(i==0):
					continue
				elif(endword[i] ==  filtword[i]):
					temp = temp + 1
			
			if(temp == length):
				issued.remove(tweeti)
		   
			
	return(issued)
def filter(str, file):
    # read the tweets.csv and store it into a dataframe
    

    # search for the string from the 'text' column in the csv file, the string will store in sub_df
    try:
        df = pd.read_csv(file)
        sub_df = df[df['Tweet_text'].str.contains(str)]
        sub_df.to_csv(str + '.csv', encoding='utf-8', index = False)
    except:
        print("filter didnt work on: " + str)
	# export sub_df to a csv file
    

def usefordatacollection(screen_name, writer):
	new_tweets = api.user_timeline(screen_name = screen_name, count=10)
	for tweet in new_tweets: 
		#print(tweet)
		created_date_local = datetime_from_utc_to_local(tweet.created_at)
		writer.writerows([[tweet.user.name, tweet.id_str, created_date_local, tweet.text.encode("utf-8")]])
		try:
			watson.textanalysis(tweet.text.encode("utf-8"))
		except:
			pass
	# with open('datacollection.csv', 'r') as csvreader:
		# rowCount = sum(1 for row in csvreader)
		# print("rowCount: " + str(rowCount))
		# # for i in range (0, rowCount):
			# # if tweet
		# reader = csv.DictReader(csvreader)
		# print("This is the reader variable " + str(reader))
		
	# csvreader.close()
	
	
		# for tweet in new_tweets: 
			# #print(tweet)
			# created_date_local = datetime_from_utc_to_local(tweet.created_at)
			# # writer.writerows([[tweet.user.name, tweet.id_str, created_date_local, tweet.text.encode("utf-8")]])
			# # watson.textanalysis(tweet.text.encode("utf-8"))
				# # created_date_local = datetime_from_utc_to_local(tweet.created_at)
			# for row in reader:
				# print("row in for loop" + str(row))
				# if (tweet.id_str == row['tweet_id']):
				
					# continue
				# else:
					# writer.writerow([[tweet.user.name, tweet.id_str, created_date_local, tweet.text.encode("utf-8")]])
					# watson.textanalysis(tweet.text.encode("utf-8"))
					# break
					
			
		
	
def get_all_tweets(screen_name, writer): #the account and the writer method are passed from the function call

	issuedtweets= [] 
	endedtweets = []
	recenttweets = []
	new_tweets = api.user_timeline(screen_name = screen_name, count=10) #collects the last 200 tweets from the account 
	recenttweets.extend(new_tweets) #recent tweets array has all the tweets from all the accounts

	for tweet in recenttweets: #iterating over a the recenttweets array
		created_date_local = datetime_from_utc_to_local(tweet.created_at) # to convert the tweets time to local time than gmt

		if(datetime.datetime.now() - created_date_local).days < 1: #check if the tweets are less than one day old
			
			Resultingtweets= [tweet.user.name, tweet.id_str, created_date_local, tweet.text.encode("utf-8")] 
			'''
			The resulting tweets varoable contains the elements of the tweet we want to put into the csv file, which includes 
			username, the tweet id, date and time tweet was created, and the tweet contents.
			'''
			#watson.textanalysis(tweet.text.encode("utf-8"))
			
			try:
				writer.writerows([Resultingtweets]) #the writer is used to write the tweet into the csv file accordingly
				# print (Resultingtweets)
			except UnboundLocalError: #an unbounderror occurs at the end of every account, when this occurs just pass and continue the function
				pass

'''
            if(thetweet.find("issued")):
               #issued = re.compile('(\s*)issued(\s*)')
                #issued.sub('', thetweet)
                issued = thetweet.replace('issued', '')
                print(issued)
                issuedtweets.append(issued)
            elif (thetweet.find("ended")):
                ended = re.compile('(\s*)ended(\s*)')
                ended.sub('', thetweet)
                endedtweets.append(ended)
                 print(tweet.text.encode("utf-8") + "\n")

'''  
##                for issued in issuedtweets:
##                    issuedtweets.append(thetweet)    
                    
			


    #writer.writerow(["User Name","Twitter_Handle","Twitter_User_Description","tweet_id","created_at","Tweet_text"])
   


                
if __name__ == '__main__':

	


	
	exit_code = call("python Frontend.py", shell=True)


	with open('UserInput.txt', 'r') as f:
		handles_list = [line.strip() for line in f]
		print(handles_list)

	with open('all_tweets.csv', 'wb') as f_all:
		writer = csv.writer(f_all)
		writer.writerow(["User Name", "tweet_id", "created_at", "Tweet_text"])
		for handle in handles_list:
			get_all_tweets(handle, writer)
			print("Done.")

			# csv_html.pandas("all_tweets.csv")
			csv_html.indexhtml("all_tweets.csv")

			follow = map(str, follow)
			print(follow)
			driver = webdriver.Chrome("C:/Users/Matrix/Downloads/chromedriver_win32/chromedriver.exe")
			driver.get("file:///C:/Users/Matrix/Desktop/tweepy%20latest/table.html")

			twitter_streamer = streaming.TwitterStreamer()
			twitter_streamer.stream_tweets('all_tweets.csv', follow, driver)
