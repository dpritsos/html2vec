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

from .cngrams import Html2TF as CHtml2TF
from ..base.vectortypes.string2tf import BaseString2TF
from ..base.termstypes.wngrams import String2WNGramsList



class Html2TF(CHtml2TF):
    
    def __init__(self, n, attrib, lowercase, valid_html):
        
        #Initialise Character N Grams Class 
        CHtml2TF.__init__(self, n, attrib, lowercase, valid_html)
               
        #Change the BaseSting Class to be initialised with Word N-grams
        self.s2tf = BaseString2TF( String2WNGramsList( n ) )
        
        

#To Be Written    
class Html2TPL():
    
    def __init__(self):
        pass