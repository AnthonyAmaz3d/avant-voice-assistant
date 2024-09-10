import speech_recognition as sr
from gtts import gTTS
import winsound
from pydub import AudioSegment
import pyautogui
import webbrowser
import sqlite3
import os

connection = sqlite3.connect("tasks.db")
cursor = connection.cursor()

def open_steam():
    os.startfile("C:/Program Files (x86)/Steam/steam.exe")

def open_wow():
    os.startfile("C:/Program Files (x86)/World of Warcraft/World of Warcraft Launcher.exe")

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

listeningToTask = False

def main():
    global tasks
    global listeningToTask
    respond("iniciando...")
    
    cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
    
    while True:
        command = listen_for_command()
        
        if command:
            if listeningToTask:
                db = "INSERT INTO tasks (name) VALUES (?)"
                args = (command,)
                cursor.execute(db, args)
                connection.commit()
                listeningToTask = False
                cursor.execute("SELECT COUNT(*) FROM tasks")
                task_count = cursor.fetchone()[0]
                respond("Adicionando " + command + " para sua lista de tarefas. Você tem "+ str(task_count) + " tarefa atualmente na sua lista")
            elif "adicione uma tarefa" in command:
                listeningToTask = True
                respond("Claro, qual tarefa? ")
            elif "liste as tarefas" in command:
                respond("Claro, suas tarefas são: ")
                cursor.execute("SELECT * FROM tasks")
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
            elif "tire um print" in command:
                pyautogui.screenshot("print.png")
                respond("Eu tirei um print para você")
            elif "youtube" in command:
                respond("Abrindo o youtube")
                webbrowser.open("https://www.youtube.com")
            elif "steam" in command:
                respond("Abrindo a steam")
                open_steam()
            elif "world of warcraft" in command:
                respond("Abrindo o wow")
                open_wow()
            elif "sair" in command:
                respond("Adeus chefe")
                break
            else:
                respond("Desculpe, eu não entendi o comando")

if __name__ == "__main__":
    main()
    connection.close()