import pyjokes

joke = pyjokes.get_joke()
print(joke)

import pyttsx3
engine = pyttsx3.init()
engine.say("Nice To Meet You Akash SIR")
engine.runAndWait()