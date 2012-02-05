

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
    
    
    