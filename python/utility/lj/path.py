# -*- coding:utf8 -*-

'''
Created on 2015��11��19��

@author: linkcare_l10n_rd
'''
import re

def compare(path1, path2):
    return not path2.find(path1) 

#0:equal
#1:path1 is sub folder of path2
#-1:path2 is sub folder of path1
#2: unrelated
def comparePath(path1, path2):
    if not path1 or not path1:
        return 2
 
    path1Len =  len(path1)
    path2Len =  len(path2)
 
    if path1Len > path2Len:
        longPath = path1
        shortPath = path2
        cmpFator  = 1
    else:
        longPath = path2
        shortPath = path1
        cmpFator  = -1
 
    shortPathLen = len(shortPath)
    longPathLen = len(longPath)
    i = 0
    j = 0
    while i < shortPathLen and j < longPathLen:
        c1 = shortPath[i]
        c2 = longPath[j]
        if isSlash(c1):
            if not isSlash(c2):
                return 2
            while i < shortPathLen and isSlash(shortPath[i]):
                i += 1
            while j < longPathLen and isSlash(longPath[j]):
                j += 1
        else:
            if c1 != c2:
                if i == shortPathLen:
                    return cmpFator
                else:
                    return 2
            i += 1
            j += 1
 
    if i == shortPathLen:
        if j == longPathLen:
            return 0
        while j < longPathLen:
            if not isSlash(longPath[j]):
                return cmpFator
            j += 1
        return 0
    else:
        return 2
     
def isSlash(c):
    return c == '/' or c == '\\'


class FolderPath(object):
    def __init__(self, path):
        self.path = path
        
    def has_sub_folder(self, path):
        '''
        @note: 
        @return: 
            1 : the path is object's sub folder
            0 : same path
            -1　: no relate path
        '''
        if self.path == '':
            return 1
        path_arr = re.split('[\\\\/]+', self.path)
        subpath_arr = re.split('[\\\\/]+', path)
        if len(path_arr) == len(subpath_arr):
            return 0
        index = 0
        for folder_name in path_arr:
            if not folder_name == subpath_arr[index]:
                return -1
            index += 1
        return 1 
        
        
        
        
        
        
        
        