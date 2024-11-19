import pyttsx3

text_speech = pyttsx3.init()

while True:
    ans = input("What you want to say? ")
    #Program should be exit on writing q
    if ans=="q":
        text_speech.say("Bye Bye Take Care")
        text_speech.runAndWait()
        break
    text_speech.say(ans)
    text_speech.runAndWait()
