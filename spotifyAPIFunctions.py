import sys
from textwrap import indent
import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth
import time
#ff99a558b3c21e403d194fdec905d48717f79dae
def callSpotifyAPI(action,data):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id="9fe021b24a6a437dae1144e135c0bb7d",
        client_secret = "d54215d8d0714a22b20aa5e15d0e079f",
        redirect_uri="http://localhost/8888/callback",
        scope="streaming,user-library-read,user-modify-playback-state,user-read-currently-playing,user-read-playback-state"))
    
    devices = sp.devices()
    print(devices)
    # deviceID = ""
    # if(len(devices['devices'])==0):
    #     time.sleep(10)
    #     devices = sp.devices()
    #     for device in devices['devices']:
    #         if('raspotify' in device['name'] and device['type']=='Computer'):
    #             deviceID = device['id']
    #             print(device)
    #             if(device['is_active']==False):
    #                 sp.transfer_playback(device_id=deviceID,force_play=False)
    #                 time.sleep(2)
            
    # playback = sp.current_playback()        
    
    # if(action=="pause"):
    #     if(playback['is_playing']):
    #         sp.pause_playback(device_id=deviceID)
    # elif(action=="play"):
    #     first = True
    #     type = ""
    #     queryString = ""

    #     if(data['songName']!=''):
    #         if(first):
    #             queryString+="track:\""+data['songName']+"\""
    #             first = False
    #         else:
    #             queryString+="+track:\""+data['songName']+"\""
    #         type += 'track'
    #     if(data['artist']!=''):
    #         if(first):
    #             queryString+="artist:\""+data['artist']+"\""
    #             first = False
    #         else:
    #             queryString+="+artist:\""+data['artist']+"\""
    #     if(queryString!=""):
    #         tracks = sp.search(queryString,limit=1,type=type)
    #         songID = tracks['tracks']['items'][0]['uri']
    #         if(songID==playback['item']['uri'] and playback['is_playing']==False):
    #             sp.start_playback(device_id=deviceID)
    #         else:
    #             sp.start_playback(device_id=deviceID,uris=[songID])
    #         time.sleep(2)
    #         playback = sp.current_playback()  
            
    
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
