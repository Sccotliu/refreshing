'''
Created on Sep 23, 2016

@author: linkcare_l10n_rd
'''
import importlib
from webserver.apps.utility.lj.delegate import Delegate

# from webserver.myapplication import getApp


class ParamsSerializer(object):
    NUMBER = None
    def __init__(self, depot_type = None, **kwargs):
        if depot_type:
            self.depot_type = depot_type
        self.app = kwargs.get('app')
        
    def _utilities(self):
        if self.app:
            ProjectModelPKG = importlib.import_module('webserver.apps.projectsettings.models')
            ProjectModel = getattr(ProjectModelPKG, 'Project')
            self.project = self.app.conn.query(ProjectModel).first()
        else:
            from config.project import Configuration
            from webserver.myapplication import get_app
            cfg = Configuration(get_app())
            self.project = cfg.project
        self.git_or_p4 = self.project.git_or_p4
        self.depot_type = self.git_or_p4
        self.workspace = self.project.workspace
        params = {}
        params['git_or_p4'] = self.git_or_p4
        params['workspace'] = self.workspace
        
        return params
        
    def do_serializer(self):
        raise NotImplementedError('')
    
    def serializer(self):
        params = self._utilities()
        if self.NUMBER == self.depot_type:
            if params:
                params.update(self.do_serializer())
        return params
    
#     def incode(self, house = None):
#         
#         params = self._utilities()
#         if self.NUMBER == self.depot_type:
#             house = self.serializer(params)
#         else:
#             house = None
#         return house

class P4Params(ParamsSerializer):
    NUMBER = 1
    def do_serializer(self):
        params = {}
        p4 = self.project.p4.first()
        params['username'] = p4.username # if self.project.p4 else ''
        params['password'] = p4.PASSWORD #if self.project.p4 else ''
        params['address'] = p4.address #if self.project.p4 else ''
        params['p4_workspace'] = p4.workspace #if self.project.p4 else ''
        return params  

class GitParams(ParamsSerializer):
    NUMBER = 2
    def do_serializer(self):
        return {}

class SDepotUtility(object):
    delegate = Delegate()
    def __init__(self, project = None, app = None):
        self.app = app
        if project:
            from webserver.prjoectsettings import create_connection
#         self.app = getApp((), globals())
            create_connection(project)
        
        p4 = P4Params(app = self.app)
        git = GitParams(app = self.app)
        self.delegate += p4.serializer
        self.delegate += git.serializer
        
#         self.delegate += p4.incode
#         self.delegate += git.incode
        
    def serializer(self, codeline=None):
        params = {}
        params['codeline'] = codeline
#         params += self.delegate()
#         return params
        house = None
#         self.delegate(house)
#         if house:
#             params.update(house)
        for _call in self.delegate.calls:
            house = _call()
            if house:
                params.update(house)
        return params