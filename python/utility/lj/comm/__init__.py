# Private function
# Subsititute express( bool?value1:value2) in c/c++
#
import os
import re
#from utility import ordereddict


def _when(b, o1, o2):
    if b:
        return o1
    else:
        return o2
    

#def obj2dict(obj):
    #_dict = ordereddict()
    #memlst = [m for m in dir(obj)]
    #for m in memlst:
        #if m[0] != "_" and not callable(m):
            #_dict[m] = getattr(obj, m)
    #return _dict

def comparepropertyforlist(_list, property,value, callable):
    if callable:
        for instance in _list:
            if getattr(instance, property)() == value:
                return True
    else:
        for instance in _list:
            if getattr(instance, property) == value:
                return True
    return False

def inside(attr_name, value, list):
    for item in list:
        if item[attr_name] == value:
            return True
    return False

def getitemforlist(_list, property, value, callable):
    
    if callable:
        for instance in _list:
#            print "%s\n%s" % (getattr(instance, property)(), value)
            if getattr(instance, property)() == value:
                return instance
    else:
        for instance in _list:
            if getattr(instance, property) == value:
                return instance
    return None

def strIsNumber(s):
    """
    @note: Determine whether a string is a legitimate float or integer
    @author: Linkcare_l10n_rd
    """
    if type(s) == int or type(s) == float:
        return s
    if not isinstance(s, basestring):
        return False
    #regex = re.compile(r'^[\d]+[.]*[\d]*$')
    regex = re.compile(r'^-?[\d]+[.]*[\d]*$')
    return regex.match(s) is not None
            
            
def sortListBy(lst, opt):
    for i in range(len(lst)-1,0,-1):
        for j in range(i):
            if lst[j][opt] > lst[j+1][opt]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
    
def sort_by_custom_compare(_lst, compareFun, order = 1):
    for i in range(len(_lst)-1, -1, -1):
        for j in range(i):
            if compareFun(_lst[j], _lst[j+1]) == order:
                _lst[j], _lst[j+1] = _lst[j+1], _lst[j]
    return _lst
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
