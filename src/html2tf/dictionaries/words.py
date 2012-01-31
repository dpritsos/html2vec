#
#    Module: words - Natural Language Dictionary Words as Terms Types      
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2tf.termstypes.words: submodule of `html2tf` module defines the class String2CNGramsList """ 

import re
from htmlattrib.attrib import HtmlText
import tfdhandler




   
class Html2TF(BaseString2TF, HtmlText):
    
    def __init__(self, lowercase=False):
        HtmlText.__init__(self)
        BaseString2TF.__init__(self)
        if lowercase:
            self._attrib = self.__attrib_lowercase
        
    def _attrib(self, xhtml_str):
        return self.tf_dict( self.text( xhtml_str ) )
    
    def __attrib_lowercase(self, xhtml_str):
        return self.tf_dict( self.text( xhtml_str ).lower() )
    
    
    