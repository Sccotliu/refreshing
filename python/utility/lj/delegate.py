'''
Created on 2014-10-17

@author: linkcare_l10n_rd
'''

class Delegate(object):
    def __init__(self, *funs, **opts):
        for fun in funs:
            if not callable(fun):
                raise RuntimeError, '%s not a call able object' % str(fun)
        self.calls = () + funs
        self.empty_except = opts.get('emptyExcept', False)
        self.proto = opts.get('prototype')
        
    def __call__(self, *args, **kwargs):
        if self.empty_except and not self.calls:
            raise RuntimeError, 'No call able objects'
        
        try:
            result = None
            for call in self.calls:
                result = call(*args, **kwargs)
            return result
        except TypeError:
            raise RuntimeError, 'Invalid callable type %s' % str(call)
        
    def __add__(self, call):
        if not callable(call):
            raise RuntimeError, '%s not a callable object' % str(call)
        if call in self.calls:
            return Delegate(*(self.calls))
        return Delegate(*(self.calls + (call,)))
    
    def __iadd__(self, *calls):
        self.calls += calls
        return self
    
    def __sub__(self, call):
        return Delegate(*[x for x in self.calls if x != call])
    
    def __isub__(self, call):
        self.calls = tuple([x for x in self.calls if x != call])
        return self
    
    def __str__(self):
        if self.proto:
            return '<Delegate object, prototype : %s>' % repr(self.proto)
        return repr(self)
    
    def clear(self):
        self.calls = []
        
    def bind(self,call):
        self.__iadd__(call)
        
    def unbind(self, call):
        if call not in self.calls:
            raise RuntimeError, '%s not bind' % str(call)
        self.calls = tuple([x for x in self.calls if x != call])
        
        
        
        
        