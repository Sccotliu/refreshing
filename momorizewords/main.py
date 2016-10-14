'''
Created on Oct 12, 2016

@author: linkcare_l10n_rd
'''

import pyttsx
from document.paper import Word
from time import sleep

if __name__ == '__main__':
    engine = pyttsx.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    for voice in engine.getProperty('voices'):
        print '%s age: %s, gender: %s, name: %s' % (voice.id, voice.age, voice.gender, voice.name)
        engine.setProperty('voice', voice.id)
        engine.say('Hello, a lot of money')
        engine.runAndWait()
#     for word in Word('words.txt'):
#         print word
#         engine.say(word)
#         engine.runAndWait()
#         sleep(3)
    