#!"C:\ProgramData\Anaconda3\python.exe"
import speech_recognition as sr
import pyttsx3
import os
import getpass
engine=pyttsx3.init()
engine.say("Hello there!!! plz enter the text for search")
engine.runAndWait()
mic=sr.Microphone()
rec=sr.Recognizer()
with mic as source:
	audio=rec.listen(source)
	text=rec.recognize_google(audio)
	print(text)
username=getpass.getuser()
print(username)
import webbrowser
string='https://www.google.com/search?q='	
string+=text
print(string)
str1='&rlz1C1CHBF_enIN824IN824&oq='
str1+=username
str2='&aqs=chrome..69i57j69i61j69i60l2j0l2.3189j0j8&sourceid=chrome&ie=UTF-8'
str1+=str2
string+=str1
print(string)
url=string
#url = "https://www.google.com/search?q=&rlz=1C1CHBF_enIN824IN824&oq=kailash&aqs=chrome..69i57j69i61j69i60l2j0l2.3189j0j8&sourceid=chrome&ie=UTF-8"
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open(url)	