'''
Created on Oct 14, 2016

@author: linkcare_l10n_rd
'''

class Word(object):
    def __init__(self, path):
        self.paper = open(path, 'r')
        
    def __iter__(self):
        line = 'Now bein'
        yield line
        while line:
            line = self.paper.readline()
            if line.strip(' \r\n').strip():
                yield line
        