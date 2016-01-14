'''
Created on 2014-10-20

@author: linkcare_l10n_rd
'''
from webserver.apps.utility.lj.delegate import Delegate 

class Event(Delegate):
    def __add__(self, call):
        super(Event, self).__add__(call)
    
    
class EventArgs(object):
    def __new__(cls):
        return super(EventArgs, cls).__new__(cls)