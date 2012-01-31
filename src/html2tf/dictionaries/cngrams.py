""" """

from htmlattrib.attrib import HtmlText
  

class Html2TF(BaseString2TFTP, HtmlText):
    
    def __init__(self, n, lowercase, valid_html):
        HtmlText.__init__(self, valid_html)
        BaseString2TFTP.__init__(self, n)
        if lowercase:
            self._attrib = self.__attrib_lowercase
        
    def _attrib(self, xhtml_str):
        return self.nf_dict( self.text( xhtml_str ) )
    
    def __attrib_lowercase(self, xhtml_str):
        return self.nf_dict( self.text( xhtml_str ).lower() )
    
    
class Html2TP(BaseString2TFTP, HtmlText):
    
    def __init__(self, n, lowercase, valid_html):
        HtmlText.__init__(self, valid_html)
        BaseString2TFTP.__init__(self, n)
        if lowercase:
            self._attrib = self.__attrib_lowercase
        
    def _attrib(self, xhtml_str):
        return self.npos_dict( self.text( xhtml_str ) )
    
    def __attrib_lowercase(self, xhtml_str):
        return self.npos_dict( self.text( xhtml_str ).lower() )
    