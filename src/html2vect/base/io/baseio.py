#
#    Module: Base I/O   
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2vect.base.io.baseio: submodule of `html2vect` module defines the class BaseIO """ 

import abc
from .basefilehandlers import BaseFileHandler


class BaseIO(BaseFileHandler):
    __metaclass__ = abc.ABCMeta
    
    def __init__(self):
        BaseFileHandler.__init__(self)
    
    
    @abc.abstractmethod
    def _attrib(self, xhtml_str): #Abstract method cannot be private (__methodname) method!
        pass
    
    
    @abc.abstractmethod
    def from_src(self, xhtml_str):
        pass


    @abc.abstractmethod    
    def from_files(self, xhtml_file_l, encoding='utf8', error_handling='strict'):
        pass


    @abc.abstractmethod        
    def from_paths(self, basepath, filepath_l, encoding='utf8', error_handling='strict'):
        pass
    


 
    
    