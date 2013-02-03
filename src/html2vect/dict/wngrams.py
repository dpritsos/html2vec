#
#    Module: Words - from html row text/files to native python character Words TF dictionaries
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2vect.dict.wngrams: submodule of `html2vect` module defines the classes: HtmlTF(), HtmlTPL()"""

from cngrams import Html2TF as CHtml2TF
from ..base.vectortypes.string2tf import BaseString2TF
from ..base.termstypes.wngrams import String2WNGramsList



class Html2TF(CHtml2TF):
    
    
    def __init__(self, n, attrib, lowercase, valid_html):
        
        #Initialise Character N Grams Class 
        CHtml2TF.__init__(self, n, attrib, lowercase, valid_html)
        
        #Change the BaseSting Class to be initialised with Word N-grams
        self.s2tf = BaseString2TF( String2WNGramsList( n ) )
        
              
        

#Deleted from the previous version now is need to be re-written    
class Html2TPL():
    
    def __init__(self):
        pass