import sda
import scipy.io.wavfile as wav
from PIL import Image
import sda

#tts
# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
# mytext = input("Enter you text:")

# # Language in which you want to convert
# language = 'en'

# # Passing the text and language to the engine,
# # here we have marked slow=False. Which tells
# # the module that the converted audio should
# # have a high speed
# myobj = gTTS(text=mytext, lang='en')

# # Saving the converted audio in a mp3 file named
# # welcome
# myobj.save("/home/mshakil-ecl/speech-driven-animation-master/example/welcome.wav")

# Playing the converted file
#os.system("mpg321 welcome.mp3")

#video
va = sda.VideoAnimator(gpu=0)#Instantiate t he animator
vid, aud = va("/home/mshakil-ecl/speech-driven-animation-master/example/image.bmp", "/home/mshakil-ecl/speech-driven-animation-master/example/test.wav")

va.save_video(vid, aud, "/home/mshakil-ecl/speech-driven-animation-master/example/bot.mp4")
