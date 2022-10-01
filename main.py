import speech_recognition as sr
import pyttsx3
import datetime

audio = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo..')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'Iza' in comando:
                comando = comando.replace('Iza', '')
                maquina.say('comando')
                maquina.runAndWait()
    except:
        print('Microfone ão está ok')
    
    return comando

def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora São' + hora)
        maquina.runAndWait()

comando_voz_usuario()
