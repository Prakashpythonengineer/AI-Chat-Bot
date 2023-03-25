import speech_recognition
import pyttsx3
import openai
openai.api_key = "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"



eng = pyttsx3.init()
voice = eng.getProperty('voices') 
eng.setProperty('voice', voice[0].id)
eng.setProperty('rate',145) 
eng.say("Your Jarvis is ready!!")
eng.runAndWait()
    
messages = []
messages.append({"role": "user", "content": "Your name is Jarvis from now"})


r = speech_recognition.Recognizer()

while True:
    try:
        with speech_recognition.Microphone() as mic:
            r.adjust_for_ambient_noise(mic,duration=0.2)
            audio = r.listen(mic)
            text = r.recognize_google(audio)
            text = text.lower()
            print(f"Recognized {text}")
            message = text
            if text == 'goodbye':
                break
            else:
                messages.append({"role": "user", "content": message})
                response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages)
                reply = response["choices"][0]["message"]["content"]
                messages.append({"role": "assistant", "content": reply})
                eng.say(reply)
                eng.runAndWait()
            
    except:
        r = speech_recognition.Recognizer()
        continue