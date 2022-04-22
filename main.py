import speech_recognition as sr
import pyttsx3
import pywhatkit
import spotifyAPIFunctions

listener = sr.Recognizer()#initialize the speech recognizer
response = pyttsx3.init()#initialize the speaker 
voices = response.getProperty('voices')
response.setProperty('voice', voices[0].id)#set the voice to male english for speaking

#--------------------------------------------
#------------------- talk -------------------
#--------------------------------------------
# Ouputs the given text to the default speaker
# 
def talk(text):
    response.say(text)
    response.runAndWait()


# take_command obtains the input from the user
# Upon running the script, the user is asked as to which song they would like to play
# The user's input is then passed to the run_player function to be processed
# User input must include play for the script to work properly

def take_command():
    
    command=""
    try:
        with sr.Microphone() as source:
            
            listener.adjust_for_ambient_noise(source)
            talk('I am listening')
            print("start speaking:")
            audio = listener.listen(source)
            command = listener.recognize_google(audio,language = "en-US")
            command = command.lower()
            if 'spotify' in command:
                command = command.replace('spotify ', '')
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
    data = {'artist':'','songName':''}
    command = take_command()
    print(command)
    if 'play' in command:
        if len(command) > 4:
            playIdx = command.index('play')
            byIdx = None
            try: 
                byIdx = command.index('by')
            except:
                byIdx=None
            if(byIdx==None):
                song = command[playIdx+4]
            else:
                song = command[playIdx+4:byIdx]
                artist = command[byIdx+2:]
                data['artist']=artist
            data['songName']=song   
            
        flag = spotifyAPIFunctions.callSpotifyAPI('play',data)
        if(flag):
            if(byIdx==None):
                song = command[playIdx+4]
                talk('now playing' + song)
        
            else:
                song = command[playIdx+4:byIdx]
                artist = command[byIdx+2:]
                talk('now playing' + song + "by" + artist)
        elif(flag==False):
            talk('I could not find that song')
        # pywhatkit.playonyt(song)
    elif 'pause' in command:
        spotifyAPIFunctions.callSpotifyAPI('pause',data)


run_player()
