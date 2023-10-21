#Text to Audio with moudle pyttsx3

#First enter on Terminal pip install pyttsx3 than=>

import pyttsx3
engine = pyttsx3.init()
#write your letter in ()below=>
engine.say('hello python')
engine.runAndWait()