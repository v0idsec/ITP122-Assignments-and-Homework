import speech_recognition as sr

#defining speech recognition and instance of recogniser class
def recognize_speech():
    recognizer = sr.Recognizer()


#use the PC default mic as the audio source
    with sr.Microphone() as source:
        print("Say something:")

        #adjust the sensitivity to ambient noise levels
        recognizer.adjust_for_ambient_noise(source)

        #listen for the phrase and extract it into audio data
        audio = recognizer.listen(source)

        try:
            #recognise speech using googles speech recognition service
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
        except sr.UnknownValueError:
            #handle unrecognised speech
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            #Handle API errors 
            print("Sorry, there was an error with the request.")

if __name__ == "__main__":
    recognize_speech()
