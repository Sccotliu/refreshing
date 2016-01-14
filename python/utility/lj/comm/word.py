'''
Created on 2012-11-2

@author: linkcare_l10n_rd
'''
import re

def words(s, encode):
    _dict = {}
    exec("_dict = words_%s(s)" % encode)
    return _dict

def words_en(s):
    r = "(?x) (?: [\w-]+  | [\x80-\xff]{3} )"
    regex = re.compile(r)
    return regex.findall(s)

class CssClass(object):
    def __init__(self):
        self.css = {}
        
    def __setitem__(self, key, value):
        self.css[key] = value
        
    def __str__(self):
        css_text = ''
        for value in self.css.itervalues():
            css_text += ' ' + value
        return css_text.strip()
        
        
        
    