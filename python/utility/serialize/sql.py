# -*- coding:utf8 -*-
'''
Created on 20151230

@author: linkcare_l10n_rd
'''
import json

from sqlalchemy.ext.declarative import DeclarativeMeta

class AlchemyEncodere(json.JSONEncoder):
    def default(self, o):
        if isinstance(o.__class__, DeclarativeMeta):
            fields = {}
            for field in [x for x in dir(o) if not x.startswith('_') and x != 'metadata']:
                data = o.__getattribute__(field)
                try:
                    json.dumps(data)
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            return fields
        return json.JSONEncoder.default(self, o)
    
def load_query(query, deepin=None):
    """
    @desc : covert query to json data.
    @param deepin: format {children:[{field:fieldname,children:[{...}]},{...}]}
    """
    data = []
    for row in query.all():
#         obj = json.dumps(row, cls=AlchemyEncodere)
        encoder = AlchemyEncodere()
        obj = encoder.default(row)
        if deepin is not None:
            for deep in deepin['children']:
                if deep.has_key('foreign_key'):
                    sub_row = eval('row.%s' % (deep['foreign_key']))
                    obj[deep['foreign_key']] = encoder.default(sub_row)
                elif deep.has_key('children'):
                    obj[deep['field']] = load_query(eval('row.%s' % deep['field']), deep)
                else:
                    obj[deep['field']] = load_query(eval('row.%s' % deep['field']))
        data.append(obj)
        
    return data