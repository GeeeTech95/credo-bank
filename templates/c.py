import pyttsx3

speak = pyttsx3.init()
text = 'hello i a coming'.decode('utf-8')
print(type(text))
speak.say()
speak.runAndWait()