#
#    Module: Base I/O   
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2vect.base.io.baseio: submodule of `html2tf` module defines the class BaseIO """ 

import abc
from .basefilehandlers import BaseFileHandler
import numpy as np

class BaseIO(BaseFileHandler):
    __metaclass__ = abc.ABCMeta
    
    def __init_(self):
        BaseFileHandler.__init__(self)
    
    @abc.abstractmethod
    def _attrib(self, xhtml_str): #Abstract method cannot be private (__methodname) method!
        pass
    
    def from_src(self, xhtml_str):
        return self._attrib(xhtml_str)
        
    def from_files(self, xhtml_file_l, encoding='utf8', error_handling='strict'):
        text_l = [ self._attrib(html_str) for html_str in self.load_files(xhtml_file_l, encoding, error_handling) ]
        return text_l  
        
    def from_paths(self, basepath, filepath_l, encoding='utf8', error_handling='strict'):
        flist = self.file_list_frmpaths(basepath, filepath_l)
        wpg_txt_ll = list()
        for filename in flist:
            xhtml_src = self.load_files(filename, encoding, error_handling)
            wpg_txt_ll.append( [filename, self._attrib(xhtml_src)]  )
        return wpg_txt_ll
    


 
    
    