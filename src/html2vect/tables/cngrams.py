#
#    Module: Character NGrams - from html row text/files to PyTables EArrays character ngrams TF dictionaries
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2vect.dict.cngrams: submodule of `html2vect` module defines the classes: HtmlTF(), HtmlTPL()"""

from ..base.features.html2attrib import BaseHTML2Attributes
from ..base.vectortypes.string2tf import BaseString2TF
from ..base.vectortypes.string2tpl import BaseString2TPL
from io import IO

from ..base.termstypes.cngrams import String2CNGramsList


class Html2TF(BaseString2TF, BaseHTML2Attributes, IO):
    
    def __init__(self, n, lowercase, valid_html, ndtype):
        IO.__init__(self)
        BaseHTML2Attributes.__init__(self, valid_html)
        BaseString2TF.__init__(self, String2CNGramsList( n ) )
        if lowercase:
            self._attrib = self.__attrib_lowercase
        self.ndtype = ndtype
        
    def _attrib(self, xhtml_str):
        return self.tf_narray( self.text( xhtml_str ), self.ndtype )
    
    def __attrib_lowercase(self, xhtml_str):
        return self.tf_narray( self.text( xhtml_str ).lower(), self.ndtype )
    
    
class Html2TPL(BaseString2TPL, BaseHTML2Attributes, IO):
    
    def __init__(self, n, lowercase, valid_html, ndtype):
        IO.__init__(self)
        BaseHTML2Attributes.__init__(self, valid_html)
        BaseString2TPL.__init__(self, String2CNGramsList( n ) )
        if lowercase:
            self._attrib = self.__attrib_lowercase
        self.ndtype = ndtype
        
    def _attrib(self, xhtml_str):
        return self.tpl_narray( self.text( xhtml_str ), self.ndtype)
    
    def __attrib_lowercase(self, xhtml_str):
        return self.tpl_narray( self.text( xhtml_str ).lower(), self.ndtype)


    