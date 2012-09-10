#
#    Module: I/O   
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2vect.sparse.io: submodule of `html2vect` module defines the class IO """ 

import abc
from ..base.io.baseio import BaseIO

class IO(BaseIO):
    __metaclass__ = abc.ABCMeta
    
    def __init__(self):
        BaseIO.__init__(self)
    
    @abc.abstractmethod
    def _attrib(self, xhtml_str): #Abstract method cannot be private (__methodname) method!
        pass
    
    
    def from_src(self, xhtml_str):
        raise Exception("Please use from_files() or from_paths() methods instead")
    
        
    def from_files(self, xhtml_file_l, smth_pos_l, smth_sigma, tid_dictionary=None, encoding='utf8', error_handling='strict'):
        return self._attrib(xhtml_file_l, smth_pos_l, smth_sigma, tid_dictionary, encoding, error_handling)  
    
        
    def from_paths(self, basepath, filepath_l, smth_pos_l, smth_sigma, tid_dictionary=None, encoding='utf8', error_handling='strict'):
        #Get the filenames located in the paths given 
        xhtml_file_l = self.file_list_frmpaths(basepath, filepath_l)
        
        #Create the lowbow vectors sparse matrix for this files
        lowbow_matrix, tid_dict = self.from_files(xhtml_file_l, smth_pos_l, smth_sigma, tid_dictionary, encoding, error_handling)
        
        #Return the lowbow matrix, the dictionary created and the xhtml_files_list
        return (lowbow_matrix, tid_dict, xhtml_file_l)
    
    
class General_IO(IO):
    __metaclass__ = abc.ABCMeta
    
    def __init__(self):
        BaseIO.__init__(self)
    
    @abc.abstractmethod
    def _attrib(self, xhtml_str): #Abstract method cannot be private (__methodname) method!
        pass
    
    
    def from_src(self, xhtml_str):
        raise Exception("Please use from_files() or from_paths() methods instead")
    
        
    def from_files(self, xhtml_file_l, tid_dictionary=None, norm_func=None, encoding='utf8', error_handling='strict'):
        return self._attrib(xhtml_file_l, tid_dictionary, norm_func, encoding, error_handling)  
    
        
    def from_paths(self, basepath, filepath_l, tid_dictionary=None, norm_func=None, encoding='utf8', error_handling='strict'):
        #Get the filenames located in the paths given 
        xhtml_file_l = self.file_list_frmpaths(basepath, filepath_l)
        
        #Create the vectors sparse matrix for this files
        matrix, tid_dict = self.from_files(xhtml_file_l, tid_dictionary, norm_func, encoding, error_handling)
        
        #Return the matrix, the dictionary created and the xhtml_files_list
        return (matrix, tid_dict, xhtml_file_l)
    
