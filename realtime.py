
import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()



try:
		
	with sr.Microphone() as source2:
		r.adjust_for_ambient_noise(source2, duration=0.02)
		print("Talk now")
		audio2 = r.listen(source2)
		
		MyText = r.recognize_google(audio2)
		MyText = MyText.lower()

		print("Did you say \n"+MyText)
			
			
except sr.RequestError as e:
	print("Could not request results; {0}".format(e))
		
except sr.UnknownValueError:
	print("unknown error occured")
