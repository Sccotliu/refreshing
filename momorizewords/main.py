'''
Created on Oct 12, 2016

@author: linkcare_l10n_rd
'''

import pyttsx

if __name__ == '__main__':
    engine = pyttsx.init()
    engine.setProperty('rate', 0)
    engine.say('anticipate')
    engine.runAndWait()
    