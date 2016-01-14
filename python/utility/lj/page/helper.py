'''
Created on 2013-12-2

@author: linkcare_l10n_rd
'''
import importlib

class OOPHelper(object):
    def __init__(self, model_name, dynamic_class_name, request):
        self.model_name = model_name
        self.dynamic_class_name = dynamic_class_name
        self.request = request
        
    @property
    def dynamic_class(self):
        mod = importlib.import_module(self.model_name)
        dynamic_class = getattr(mod, self.dynamic_class_name)
        return dynamic_class(self.request)