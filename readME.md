INTRODUCTION
------------

This is group 5's project for CS 530 at SDSU. This project is the attempt at making a voice controlled speaker
that plays songs from Spotify through a Raspberry PI.

REQUIREMENTS
------------

This project requires the following:

1. Spotify Premium Account

Hardware:

1. Raspberry PI Model with wifi or ethernet capability
2. USB Microphone 
3. USB Speaker

Software:

1. Raspotify - https://github.com/dtcooper/raspotify - allows raspberry PI to be used as the output device
2. portAudio - this is a dependency on one of the python packages pyaudio
3. espeak - a dependency needed for the speech recognition
4. flac - a dependency for recognizing the usb microphone
5. pip - installer to get all the python libraries specified in requirements.txt
6. Chromium or an equivalent web browser 

Other dependencies that are needed are in the requirements.txt

SETUP
-----

1. Install the dependencies that are required:
   Run the following:
   1. sudo apt update
   2. sudo apt upgrade 
   3. sudo apt install raspotify
   4. sudo apt install portAudio
   5. sudo apt install espeak
   6. sudo apt install flac 
   7. sudo apt install pip
   8. sudo apt install git
2. Create a new directory and clone this repository 
   1. mkdir [directory name goes here]
   2. git clone https://github.com/zaskins/cs530Group5
3. Install the python library dependencies 
   1. cd [directory name specified in step 2]
   2. pip install -r requirements.txt
4. Setup the microphone 
   1. Run arecord -l 
      1. Find the microphone you plugged in and take note of the card number and the device number
   2. Navigate to /home/pi/.asoundrc
      1. If the directory is not available just navigate to /home
   3. Run the following nano .asoundrc 
   4. Paste the following on a new line 
      pcm.!default {
       type asym
       capture.pcm "mic"
      }
      pcm.mic {
       type plug
       slave {
       pcm "hw:2,0"
       }
      }
    5. Save the file
5. Login into your spotify account from the browser
6. Run python3 main.py 
   1. Say Spotify Play [song name goes here]
   2. A web browser will pop up asking for you to authorize app to access your spotify account
   3. Click yes, then copy the link in the address bar into the command line and click the enter key
7. Everything should be setup

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

