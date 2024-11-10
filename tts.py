# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
# mytext = input("Enter for tts: ")
mytext = ('Japan—a land where modern marvels meet ancient traditions.In Tokyo, every street hums with life, each corner a blend of fast-paced energy and unexpected calm. '
          'Yet, amidst the rush, you’ll find places where time seems to stand still—like these tranquil shrines and sacred spaces.'
          'Japan’s soul lives in these moments. The slow, graceful art of tea-making—a reminder to savor each second.'
          'Nature here is breathtaking. From majestic Mount Fuji to hidden forest trails, Japan’s landscapes offer a quiet power that stays with you.'
          'So whether you’re exploring city lights or timeless traditions, Japan’s magic is everywhere, waiting to be discovered. Ready '
          'or your own adventure? Japan awaits.')
# Language in which you want to convert
language = 'en'
accent = 'co.uk'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
# myobj = gTTS(text=mytext, lang=language, slow=False)
myobj = gTTS(text=mytext, lang=language, tld=accent)

# myobj.runAndWait()
# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted file
os.system("start welcome.mp3")
