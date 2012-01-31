#
#
#
#

""" """

from htmlattrib.attrib import HtmlText
from html2tf.dictionaries.cngrams import BaseString2NgramList 
import tbtools
import numpy as np


class Html2TF(BaseString2TFTP, HtmlText):
    
    def __init__(self, n, lowercase, valid_html):
        HtmlText.__init__(self, valid_html)
        BaseString2TFTP.__init__(self, n)
        if lowercase:
            self._attrib = self.__attrib_lowercase
        
    def _attrib(self, xhtml_str):
        return self.tf_array( self.text( xhtml_str ) )
    
    def __attrib_lowercase(self, xhtml_str):
        return self.tf_array( self.text( xhtml_str ).lower() )
    
    
class Html2TP(BaseString2TFTP, HtmlText):
    
    def __init__(self, n, lowercase, valid_html):
        HtmlText.__init__(self, valid_html)
        BaseString2TFTP.__init__(self, n)
        if lowercase:
            self._attrib = self.__attrib_lowercase
        
    def _attrib(self, xhtml_str):
        return self.tpos_array( self.text( xhtml_str ) )
    
    def __attrib_lowercase(self, xhtml_str):
        return self.tpos_array( self.text( xhtml_str ).lower() )
    