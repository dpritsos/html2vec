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
from ..base.io.baseio import BaseIO
from ..base.termstypes.cngrams import String2CNGramsList
from ..base.convert.tfdtools import TFDictTools
 
import scipy.sparse as ssp
import numpy as np



class Html2TF(BaseIO):
    
    #Term Frequency Dictionary Tools Class
    tfdtools = TFDictTools()
    
    
    def __init__(self, n, attrib, lowercase, valid_html):
               
        #Initialise IO Class
        BaseIO.__init__(self)
        
        #HTML to attributes Class
        self.h2attr = BaseHTML2Attributes( valid_html )
        
        #String to Term Frequency Class using String to Character N-Grams Class as argument 
        self.s2tf = BaseString2TF( String2CNGramsList( n ) ) 
        
        if attrib == "text":
            self._attrib_ = self.h2attr.text
        elif attrib == "tags":
            self._attrib_ = self.s2tf.tags
                        
        if lowercase:
            self._attrib_ = self._lower( self._attrib_ )
            
        
    def _attrib(self, xhtml_file_l, tid_dictionary, norm_func, encoding, error_handling):
        
        #Create the Dictionary from the given corpus if not given form the use
        if tid_dictionary == None:
            print "Creating Dictionary"
            tf_d = dict()
            #Merge All Term-Frequency Dictionaries created by the Raw Texts
            for html_str in self.load_files(xhtml_file_l, encoding, error_handling):
                tf_d = tfdtools.merge_tfds( tf_d, self.tf_dict( self._attrib_( html_str ) ) )
                
            #Create The Terms-Index Dictionary that is shorted by Frequency descending order
            tid_dictionary = tfdtools.tf2tidx( tf_d )
            
        print "Creating NGrams-TF"
        #Create the NGrams-TF Sparse Matrix for the whole corpus
        fq_lst = list()
        for html_str in self.load_files(xhtml_file_l, encoding, error_handling):
            fq_lst.append( self.s2tf.f_sparse(self._attrib_( html_str ), tid_dictionary, norm_func) )
        
        #Pack it as a sparse vstack and return it
        copus_fq_array = ssp.vstack( fq_lst )
        return ( ssp.csr_matrix(copus_fq_array, shape=copus_fq_array.shape, dtype=np.float32), tid_dictionary )
    
    
    def _lower(self, methd):
        
        def lowerCase(*args, **kwrgs):
            return methd(*args, **kwrgs).lower()
        
        return lowerCase
    
    
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
    
    
    
#To Be Written    
class Html2TPL():
    
    def __init__(self):
        pass
        
    