import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile(r"C:\Users\arul_\Desktop\Anand\Speech Recognition\hello.wav") as source:   
    
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
    try:
        text = r.recognize_google(audio_text)
        print('Converting audio transcripts into text ...')
        print(text)
     
    except:
         print('Sorry.. run again...')