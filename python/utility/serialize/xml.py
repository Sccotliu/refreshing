#!/usr/local/bin/python2.7
# encoding: utf-8
'''
Created on 2015-7-8

@author: linkcare_l10n_rd
'''
import json
import re
import os

from lxml.etree import _ElementTree
from module.xml.xmlio import XmlIO
from parsers.src.xml.treeviewxmlparser import TreeViewXMLParser


class XMLSerialize(object):
    '''
    Xml serialize
    '''

    HAS_NO_CHILDREN = re.compile(r'^/?[^/]*/?$')
    def __init__old(self, doc):
        '''
        Constructor
        '''
        self._doc = doc
        if not isinstance(doc, _ElementTree):
            xml_obj = XmlIO(doc)
            xml_obj.get_xml()                                                                                                                                                                                                                                                                                                                                                                                                
            self._doc = xml_obj.root   
        
        self.mainparagraph = self._initializer()
        
    def __init__(self, doc, rule, encoding='utf-8'):
        self._doc = doc
        self._rule = rule
        parser = TreeViewXMLParser()
        
        self.xpath_list = parser.parse_for_treeview(parser.get_file_content(self._doc, encoding), encoding)
#         print self.xpath_list
        self.mainparagraph = self._initializer()
        
    def _initializer_old(self):
        mainparagraph = self._doc.getroot()
        def recursive(el):
            cabinet = []
            tag_name = (lambda: el.tag if type(el.tag) == str else '#comment')()
            icon = (lambda:'folder-node' if len(el.getchildren()) > 0 else 'leaf-node')()
            tag = {'text': tag_name, 'iconCls':icon}
            if el.attrib:
#                 attributes = []
                for attr in el.attrib:
#                     if tag.has_key('children'):
#                     attrs = {'text': '%s:%s' % (attr,el.attrib[attr]), 'iconCls':'attribute-node'}
                    tag_attr = {'attri_name':attr, 'attri_value':el.attrib[attr].replace('\\', '\\\\')}
#                     attributes.append(attrs)
                tag['attributes'] = tag_attr
#                 tag['attributes'] = attributes
#                 if tag.has_key('children'):
#                     tag['children'] += attributes
#                 else:
#                     tag['children'] = attributes
            cabinet.append(tag)
            for sub_element in el.iterchildren():
                if tag.has_key('children'):
                    tag['children'] += recursive(sub_element)
                else:
                    tag['children'] = recursive(sub_element)
                tag['state'] = 'open'
            return cabinet
        return recursive(mainparagraph)
    
    def _children(self, el):
        children = []
        for key, value in self.xpath_list.iteritems():
            segment = (lambda seg:seg if el != '/' else key)(os.path.relpath(key, el).replace('\\','/'))
            if self.HAS_NO_CHILDREN.match(segment):
                del self.xpath_list[key]
                children.append( (key, value, segment.replace('/','')))
        return children
    
    def _initializer(self):
        mainparagraph = ('/', {'attribute':[]}, '\\')
        def recursive(el):
            cabinet = []
            tag = {'text':el[2]}
            if el[1]['attribute']:
                attributes = []
                for attri in el[1]['attribute']:
                    attributes.append({'text':attri,
                                       'type':'attribute-node', 
                                       'iconCls':'attribute-node %s' % (lambda s:'include-node' if s else 'exclude-node')(self._rule.status(el[0], '@%s' % attri))})
            
                    
                if tag.has_key('children'):
                    tag['children'] += attributes
                else:
                    tag['children'] = attributes
                    
            if el[1].has_key('namespace'):
                namespaces= []
                for key, value in el[1]['namespace'].items():
                    namespaces.append({'prefix':key, 'text':value})
#                 if tag.has_key('namespace'):
#                     tag['namespace'] += namespaces
#                 else:
                tag['namespace'] = namespaces
            cabinet.append(tag)
            for sub_element in self._children(el[0]):
                if tag.has_key('children'):
                    tag['children'] += recursive(sub_element)
                else:
                    tag['children'] = recursive(sub_element)
            icon = (lambda:'folder-node' if tag.has_key('children') else 'leaf-node')()
            status = (lambda:'include-node' if self._rule.status(el[0], 'text') else 'exclude-node')()
            tag['iconCls'] = '%s %s' % (icon, status)
            tag['type'] = icon
            return cabinet
            
        
        return recursive(mainparagraph)
        
        
    def to_json(self):
        return json.dumps(self.mainparagraph)
        
        
        