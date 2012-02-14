#
#    Module: Words - from html row text/files to native python character Words TF dictionaries
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2vect.dict.words: submodule of `html2vect` module defines the classes: HtmlTF(), HtmlTP()"""

from ..base.features.html2attrib import BaseHTML2Attributes
from ..base.vectortypes.string2tf import BaseString2TF
from ..base.vectortypes.string2tpl import BaseString2TPL
from ..base.io.baseio import BaseIO

from ..base.termstypes.words import String2WordList


class Html2TF(BaseString2TF, BaseHTML2Attributes, BaseIO):
    
    def __init__(self, lowercase, valid_html):
        BaseIO.__init__(self)
        BaseHTML2Attributes.__init__(self, valid_html)
        BaseString2TF.__init__(self, String2WordList() )
        if lowercase:
            self._attrib = self.__attrib_lowercase
        
    def _attrib(self, xhtml_str):
        return self.tf_dict( self.text( xhtml_str ) )
    
    def __attrib_lowercase(self, xhtml_str):
        return self.tf_dict( self.text( xhtml_str ).lower() )
    
    
class Html2TP(BaseString2TPL, BaseHTML2Attributes, BaseIO):
    
    def __init__(self, lowercase, valid_html):
        BaseIO.__init__(self)
        BaseHTML2Attributes.__init__(self, valid_html)
        BaseString2TPL.__init__(self, String2WordList() )
        if lowercase:
            self._attrib = self.__attrib_lowercase
        
    def _attrib(self, xhtml_str):
        return self.tpl_dict( self.text( xhtml_str ) )
    
    def __attrib_lowercase(self, xhtml_str):
        return self.tpl_dict( self.text( xhtml_str ).lower() )
    