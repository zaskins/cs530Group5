import speech_recognition as sr
import pyttsx3
import pywhatkit

listener = sr.Recognizer()
response = pyttsx3.init()
voices = response.getProperty('voices')
response.setProperty('voice', voices[1].id)  # changes voice type to female (completely irrelevant)


def talk(text):
    response.say(text)
    response.runAndWait()


# take_command obtains the input from the user
# Upon running the script, the user is asked as to which song they would like to play
# The user's input is then passed to the run_player function to be processed
# User input must include play for the script to work properly

def take_command():
    try:
        with sr.Microphone() as source:
            talk('which song should I play')
            audio = listener.listen(source)
            command = listener.recognize_google(audio)
            command = command.lower()
            if 'spotify' in command:
                command = command.replace('spotify', '')

    except:
        pass
    return command


# The run_player command is used to play the song given by the user
# Therefore, the spotify connectivity should most likely be located in this function
# Currently, the code obtains the song name from the user and then plays it from YouTube
# Perhaps the user can choose which streaming site to use
# For example, say 'play xyz from YouTube' would play the song 'xyz' from YouTube
# Then we can use the snippet from lines 28-30 to remove the streaming site from the command

def run_player():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')  # removing the word 'play' from the response
        talk('now playing' + song)
        pywhatkit.playonyt(song)


run_player()
