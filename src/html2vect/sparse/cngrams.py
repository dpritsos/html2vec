#
#    Module: Words-TF - from html row text/files to scipy.sparse.csr_matrix Words-TF
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2vect.sparse.cngrams: submodule of `html2vect` module defines the classes: Html2TF() """

from ..base.html2terms import BaseHtml2TF
from ..base.termstypes.cngrams import String2CNGramsList
 
import scipy.sparse as ssp
import numpy as np



class Html2TF(BaseHtml2TF):
    
    #Define the TermsType to be produced from this class 
    s2ngl = String2CNGramsList()
    
       
    def __init__(self, *args, **kwrgs):
            
        #Initialise BaseHtml2TF Class   
        super(Html2TF, self).__init__(*args, **kwrgs)
            
        
    def yield_(self, xhtml_file_l, tid_dictionary, norm_func, encoding, error_handling):
        
        #Create the Dictionary from the given corpus if not given form the use
        if tid_dictionary == None:
            tid_dictionary = self.__build_vocabulery(xhtml_file_l, encoding, error_handling)
            
        print "Creating NGrams-TF"
        #Create the NGrams-TF Sparse Matrix for the whole corpus
        fq_lst = list()
        for html_str in self.load_files(xhtml_file_l, encoding, error_handling):
            fq_lst.append( self.s2tf.f_sparse(self._attrib( html_str ), tid_dictionary, norm_func) )
        
        #Pack it as a sparse vstack and return it
        copus_fq_array = ssp.vstack( fq_lst )
        return ( ssp.csr_matrix(copus_fq_array, shape=copus_fq_array.shape, dtype=np.float32), tid_dictionary )
    
    
    def from_src(self, xhtml_str):
        raise Exception("Please use from_files() or from_paths() methods instead")
    
        
    def from_files(self, xhtml_file_l, tid_dictionary=None, norm_func=None, encoding='utf8', error_handling='strict'):
        return self.yield_(xhtml_file_l, tid_dictionary, norm_func, encoding, error_handling)  
    
        
    def from_paths(self, basepath, filepath_l, tid_dictionary=None, norm_func=None, encoding='utf8', error_handling='strict'):
        
        #Get the filenames located in the paths given 
        xhtml_file_l = self.file_list_frmpaths(basepath, filepath_l)
        
        #Create the vectors sparse matrix for this files
        matrix, tid_dict = self.from_files(xhtml_file_l, tid_dictionary, norm_func, encoding, error_handling)
        
        #Return the matrix, the dictionary created and the xhtml_files_list
        return (matrix, tid_dict, xhtml_file_l)
    
    
    
#To Be Written    
class Html2TPL(object):
    
    def __init__(self):
        pass
        
    