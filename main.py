import speech_recognition as sr
from gtts import gTTS
import winsound
from pydub import AudioSegment
import pyautogui
import webbrowser

def listen_for_command():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Escutando os comandos....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio, language="pt-BR")
        print("Você disse: ", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Não consegui entender o audio. Tente novamente.")
        return None
    except sr.RequestError:
        print("Erro no requerimento, tente novamente. ")
        return None

def respond(response_text):
    print(response_text)
    tts = gTTS(text=response_text, lang='pt-BR')
    tts.save("response.mp3")
    sound = AudioSegment.from_mp3("response.mp3")
    sound.export("response.wav", format="wav")
    winsound.PlaySound("response.wav", winsound.SND_FILENAME)

tasks = []
listeningToTask = False

def main():
    global tasks
    global listeningToTask
    respond("iniciando...")
    while True:
        command = listen_for_command()
        
        if command:
            if listeningToTask:
                tasks.append(command)
                listeningToTask = False
                respond("Adicionando " + command + " para sua lista de tarefas. Você tem " + str(len(tasks)) + " tarefa atualmente na sua lista")
            elif "adicione uma tarefa" in command:
                listeningToTask = True
                respond("Claro, qual tarefa? ")
            elif "liste as tarefas" in command:
                respond("Claro, suas tarefas são: ")
                for task in tasks:
                    respond(task)
            elif "tire um print" in command:
                pyautogui.screenshot("print.png")
                respond("Eu tirei um print para você")
            elif "Abra o navegador" in command:
                respond("Abrindo o firefox")
                webbrowser.open("https://www.youtube.com")
            elif "sair" in command:
                respond("Adeus chefe")
                break
            else:
                respond("Desculpe, eu não entendi o comando")

if __name__ == "__main__":
    main()