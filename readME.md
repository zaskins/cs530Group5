INTRODUCTION
------------

This is group 5's project for CS 530 at SDSU. This project is the attempt at making a voice controlled speaker
that plays songs from Spotify.

REQUIREMENTS
------------

This project requires the following:

Raspotify - https://github.com/dtcooper/raspotify - allows raspberry PI to be used as the output device

portAudio - this is a dependency on one of the python packages pyaudio. 

pip - installer to get all the python libraries specified in requirements.txt

Other dependencies that are needed are in the requirements.txt

USAGE
-----

1. Run python3 main.py
2. After running, wait for the terminal to output "start speaking:"
3. If you want to play a song say "Spotify play (Song name)" if you want to be more specific
   about the artist then say "Spotify play (song name) by (artist name)"
    a. If the song is found then the song will start playing 
    b. If not then will say song could not be found 
4. If you want to resume playing the current song then say "Spotify play"
5. If you want to pause what is currently playing then say "Spotify pause"
6. Repeat

