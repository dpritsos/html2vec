#
#    Module: Character NGrams - from html row text/files to native python character ngrams TF dictionaries
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2vect.dict.cngrams: submodule of `html2vect` module defines the classes: HtmlTF(), HtmlTPL()"""

import warnings
from ..base.features.html2attrib import BaseHTML2Attributes
from ..base.vectortypes.string2tf import BaseString2TF
from ..base.io.baseio import BaseIO
from ..base.termstypes.cngrams import String2CNGramsList
from ..base.html2terms import Html2Attr



class Html2TF(BaseIO, Html2Terms):
    
    def __init__(self, n, attrib, lowercase, valid_html):
        
        #Initialise BaseIO Class
        BaseIO.__init__(self)
        
        #Initialise Html2Terms
        Html2Attr.__init__(self, attrib, lowercase, valid_html)
        
        #String to Term Frequency Class using String to Character N-Grams Class as argument 
        self.s2tf = BaseString2TF( String2CNGramsList( n ) )    
        
        
    def _tf(self, xhtml_str, tid_vocabulary):
        return self.s2tf.tf_dict( self._attrib( xhtml_str ), tid_vocabulary)
    
        
    def build_vocabulary(self,xhtml_file_l, encoding, error_handling):
         
        #The TF Dictionary 
        tf_d = dict()
        #Merge All Term-Frequency Dictionaries created by the Raw Texts
        for html_str in self.load_files(xhtml_file_l, encoding, error_handling):
            tf_d = tfdtools.merge_tfds( tf_d, self.s2tf.tf_dict( self._attrib( html_str ) ) )
            
        #Create The Terms-Index Vocabulary that is shorted by Frequency descending order
        tid_vocabulary = tfdtools.tf2tidx( tf_d )
        
        return tid_vocabulary
    
 
    def from_src(self, xhtml_str, tid_vocabulary=None):
        
        #Create the Vocabulary from the given corpus if not given as argument
        if tid_vocabulary == None:
            tid_vocabulary = self.build_vocabulary()
            
        return (self._tf(xhtml_str, tid_vocabulary), tid_vocabulary)

        
    def from_files(self, xhtml_file_l, tid_vocabulary=None, encoding='utf8', error_handling='strict'):
        
        #Create the Vocabulary from the given corpus if not given as argument
        if tid_vocabulary == None:
            tid_vocabulary = self.build_vocabulary()
        
        tfd_l = [ self._tf(html_str, id_vocabulary) for html_str in self.load_files(xhtml_file_l, encoding, error_handling) ]
        
        return (tfd_l, tid_vocabulary)  

        
    def from_paths(self, basepath, filepath_l, tid_vocabulary=None, encoding='utf8', error_handling='strict'):
        
        #Create the Vocabulary from the given corpus if not given as argument
        if tid_vocabulary == None:
            tid_vocabulary = self.build_vocabulary()
        
        flist = self.file_list_frmpaths(basepath, filepath_l)
        wpg_txt_ll = list()
        
        for filename in flist:
            xhtml_src = self.load_files(filename, tid_vocabulary, encoding, error_handling)
            wpg_tfd_ll.append( [filename, self._tf(xhtml_src, tid_vocabulary) ]  )
            
        return (wpg_tfd_ll, tid_vocabulary) 
    
    
    
#Deleted from the previous version now is need to be re-written    
class Html2TPL(BaseIO):
    
    def __init__(self):
        pass
        
        

    