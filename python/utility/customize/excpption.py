'''
Created on Oct 11, 2016

@author: linkcare_l10n_rd
'''


class HTMLException(BaseException):
    def __init__(self, value):
        self.value = value
        
    def __str__(self, *args, **kwargs):
        msg = 'error message: %s from server' % self.value
        return repr(msg)