#
#    Module: Words-TF - from html row text/files to scipy.sparse.csr_matrix Words-TF
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2vect.sparse.words: submodule of `html2vect` module defines the classes: Html2TF() """

from ..base.features.html2attrib import BaseHTML2Attributes
from ..base.vectortypes.string2tf import BaseString2TF
from ..base.convert.tfdtools import TFDictTools
from io import General_IO

from ..base.termstypes.words import String2WordList

import scipy.sparse as ssp
import numpy as np



class Html2TF(BaseString2TF, TFDictTools, BaseHTML2Attributes, General_IO):
    
    def __init__(self, attrib, lowercase, valid_html):
        General_IO.__init__(self)
        BaseHTML2Attributes.__init__(self, valid_html)
        BaseString2TF.__init__(self, String2WordList() )
        if attrib == "text":
            self._attrib_ = self.text
        elif attrib == "tags":
            self._attrib_ = self.tags            
        if lowercase:
            self._attrib_ = self._lower( self._attrib_ )
            
        
    def _attrib(self, xhtml_file_l, tid_dictionary, norm_func, encoding, error_handling):  
        #Create the Dictionary from the given corpus if not given form the use
        if tid_dictionary == None:
            print "Creating Dictionary"
            tf_d = dict()
            #Merge All Term-Frequency Dictionaries created by the Raw Texts
            for html_str in self.load_files(xhtml_file_l, encoding, error_handling):
                tf_d = self.merge_tfds( tf_d, self.tf_dict( self._attrib_( html_str ) ) )
                
            #Create The Terms-Index Dictionary that is shorted by Frequency descending order
            tid_dictionary = self.tf2tidx( tf_d )
            
        print "Creating Words-TF"
        #Create the Words-TF Sparse Matrix for the whole corpus
        fq_lst = list()
        for html_str in self.load_files(xhtml_file_l, encoding, error_handling):
            fq_lst.append( self.f_sparse(self._attrib_( html_str ), tid_dictionary, norm_func) )
        
        #Pack it as a sparse vstack and return it
        copus_fq_array = ssp.vstack( fq_lst )
        return ( ssp.csr_matrix(copus_fq_array, shape=copus_fq_array.shape, dtype=np.float32), tid_dictionary )
    
    
    def _lower(self, methd):
        def lowerCase(*args, **kwrgs):
            return methd(*args, **kwrgs).lower()
        return lowerCase
    

    