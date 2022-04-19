import sys
from textwrap import indent
import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth
import time
#ff99a558b3c21e403d194fdec905d48717f79dae

def checkCurrentDevice(sp,device_ID):
    playback = sp.current_playback()
    return(playback != None and playback['device']['id']==device_ID)
    
def transferPlayback(sp,device_ID):
    sp.transfer_playback(device_id=device_ID)

def pausePlayback(sp):
    sp.pause_playback()

def findItem(sp,data):
    first = True
    type = ""
    queryString = ""

    if(data['songName']!=''):
        if(first):
            queryString+="track:\""+data['songName']+"\""
            first = False
        else:
            queryString+="+track:\""+data['songName']+"\""
        type += 'track'
        if(data['artist']!=''):
            if(first):
                queryString+="artist:\""+data['artist']+"\""
                first = False
            else:
                queryString+="+artist:\""+data['artist']+"\""
        if(queryString!=""):
            tracks = sp.search(queryString,limit=1,type=type)
            songID = tracks['tracks']['items'][0]['uri']
    else:
        
def play(sp,data):
    
            playback = sp.current_playback()
            if(songID==playback['item']['uri'] and playback['is_playing']==False):
                sp.start_playback()
            else:
                sp.start_playback(uris=[songID])
        else:
            sp.start_playback()

def callSpotifyAPI(action,data):

    device_ID = "8fb94490ca698113be12efc8251f424fe432c41e"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="9fe021b24a6a437dae1144e135c0bb7d",
    client_secret = "d54215d8d0714a22b20aa5e15d0e079f",
    redirect_uri="http://localhost/8888/callback",
    scope="streaming,user-library-read,user-modify-playback-state,user-read-currently-playing,user-read-playback-state"))
    
    if(not checkCurrentDevice(sp,device_ID)):
       transferPlayback(sp,device_ID)
    
    if(action=='play'):
        return 

    
songName=""
artist = ""
for i in range(1,len(sys.argv)):
    if(i==1):
        action = sys.argv[1]
    elif(i==2):
        songName = sys.argv[2].replace(","," ")
    elif(i==3):
        artist = sys.argv[3].replace(","," ")

data = {'artist':'','songName':''}
data['artist']=artist
data['songName']=songName
callSpotifyAPI(action,data)
