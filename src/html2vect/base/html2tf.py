#
#    Module: html2terms
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2vect.base.html2terms: submodule of `html2vect` module defines the classes: BaseHtml2TF"""

import abc
import warnings
from ..base.features.html2attrib import BaseHTML2Attributes
from ..base.vectortypes import termslist2tf 
from ..base.io.basefilehandlers import BaseFileHandler
from ..utils import tfdutils



class BaseHtml2TF(BaseFileHandler):
    __metaclass__ = abc.ABCMeta


    def __init__(self, n, html_attrib, lowercase, valid_html):
        
        #Initialise BaseFileHandler Class
        super(BaseHtml2TF, self).__init__()   
        
        #HTML to attributes Class
        self.h2attr = BaseHTML2Attributes( valid_html )
        
        #Initialised the TermsType to be produced from this class stored in as class attribute 
        self.__class__.s2ngl.N = n
        
        #String to Term Frequency Class using  
        self.tl2tf = termslist2tf 
        
        if html_attrib == "text":
            self.html_attrib__ = self.h2attr.text
        elif attrib == "tags":
            self.html_attrib__ = self.h2attr.tags
        else:
            raise Exception("Invalid attribute: only HTML 'text' or 'tags' can be retured for now")
                        
        if lowercase:
            self.html_attrib = self._lower( self.html_attrib__ )    
        else:
            self.html_attrib = self.html_attrib__
   
    
    def _lower(self, methd):
        
        def lowerCase(*args, **kwrgs):
            return methd(*args, **kwrgs).lower()
        
        return lowerCase
    
    
    def build_vocabulary(self,xhtml_file_l, encoding, error_handling):
         
        #The TF Dictionary 
        tf_d = dict()
        #Merge All Term-Frequency Dictionaries created by the Raw Texts
        for html_str in self.load_files(xhtml_file_l, encoding, error_handling):
            #print self.html_attrib( html_str ).encode('utf8')
            print self.__class__.s2ngl.terms_lst( self.html_attrib( html_str ) )
            0/0
            tf_d = tfdutils.merge_tfds( tf_d, self.tl2tf.trms2tf_dict( self.__class__.s2ngl.terms_lst( self.html_attrib( html_str ) ) ) )
            
        #Create The Terms-Index Vocabulary that is shorted by Frequency descending order
        #tid_vocabulary = tfdtools.tf2tidx( tf_d )

        tid_vocabulary = tf_d
        
        return tid_vocabulary
    
    
    def __build_vocabulary(self,*args, **kwrgs):
        
        #Warn me that a Vocabulary is automaticaly buildined  
        warnings.warn("Automated Vocabulary Building has been triggered: NONE tid_vocabulary has been given as argument")
        
        #Build and return the Vocabulary
        return self.build_vocabulary(*args, **kwrgs)
        
        
    @abc.abstractmethod        
    def yield_(self, xhtml_str, tid_vocabulary): 
        #The main method that will produce the Term-Frequency or Frequency Dictionaries/Lists
        pass
    
     
    @abc.abstractmethod    
    def from_src(self, xhtml_str, tid_vocabulary=None):
        pass


    @abc.abstractmethod    
    def from_files(self, xhtml_file_l, tid_vocabulary=None, encoding='utf8', error_handling='strict'):
        pass

    
    @abc.abstractmethod    
    def from_paths(self, basepath, filepath_l, tid_vocabulary=None, encoding='utf8', error_handling='strict'):
       pass
            

        
        

    