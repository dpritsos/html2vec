#
#    Module: Character NGrams - from html row text/files to PyTables EArrays character NGrams Frequencies
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2vect.tables.cngrams: submodule of `html2vect` module defines the classes: Html2TF() """

from ..base.html2terms import BaseHtml2TF
from ..base.termstypes.cngrams import String2CNGramsList
 
import numpy as np
import tables as tb


class Html2TF(BaseHtml2TF):
    
    #Define the TermsType to be produced from this class 
    s2ngl = String2CNGramsList()
    
       
    def __init__(self, *args, **kwrgs):

        #Initialise BaseHtml2TF Class   
        super(Html2TF, self).__init__(*args, **kwrgs)
            
        
    def yield_(self, xhtml_file_l, h5_fname, tid_dictionary, norm_func, encoding, error_handling):
        
        #Creating h5file
        h5f = tb.openFile(h5_fname, 'w')

        #Initializing EArray. NOTE: expectedrow is critical for very large scale corpora
        fq_earray = tb.createEArray(h5f, 'corpus_earray', tb.Float64Atom(), shape=(0,), expectedrows=len(xhtml_file_l) )

        #Creating the Dictionary from the given corpus if not given form the use
        if tid_dictionary == None:
            tid_dictionary = self.__build_vocabulery(xhtml_file_l, encoding, error_handling)
            
        print "Creating NGrams-TF"
        #Create the NGrams-TF Sparse Matrix for the whole corpus
        for html_str in self.load_files(xhtml_file_l, encoding, error_handling):
            fq_earray.append( self.s2tf.f_narray(self._attrib( html_str ), tid_dictionary, norm_func) )
        
        #Return Corpus Frequencie's-per-Document EArray
        return (fq_earray, h5f, tid_dictionary)
    
    
    def from_src(self, xhtml_str):
        raise Exception("Please use from_files() or from_paths() methods instead")
    
        
    def from_files(self, xhtml_file_l, h5_fname, tid_dictionary=None, norm_func=None, encoding='utf8', error_handling='strict'):
        return self.yield_(xhtml_file_l, h5_fname, tid_dictionary, norm_func, encoding, error_handling)  
    
        
    def from_paths(self, basepath, filepath_l, h5_fname, tid_dictionary=None, norm_func=None, encoding='utf8', error_handling='strict'):
        
        #Get the filenames located in the paths given 
        xhtml_file_l = self.file_list_frmpaths(basepath, filepath_l)
        
        #Create the vectors sparse matrix for this files
        matrix, h5f, tid_dict = self.from_files(xhtml_file_l, h5_fname, tid_dictionary, norm_func, encoding, error_handling)
        
        #Return the matrix, the dictionary created and the xhtml_files_list
        return (matrix, h5f, tid_dict, xhtml_file_l)
    
    
    
#To Be Written    
class Html2TPL(object):
    
    def __init__(self):
        pass
