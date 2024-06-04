import pyttsx3

def text_to_speech(text, language='en', speed=150):
    engine = pyttsx3.init()
    engine.setProperty('rate', speed)  # Adjust speed (words per minute)
    engine.setProperty('voice', language)  # Change language
    engine.say(text)
    engine.runAndWait()

text_to_speech("welcome to my github account", language='bn', speed=50)
