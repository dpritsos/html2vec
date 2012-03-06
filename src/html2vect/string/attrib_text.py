#
#    Module: Base I/O   
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2vect.string.attrib_text: submodule of `html2tf` module defines the classes:
    HtmlFullText(), HtmlTagText(), HtmlScriptText(), HtmlStyleText()  """

from ..base.features.html2attrib import BaseHTML2Attributes
from ..base.io.baseio import BaseIO
  
             
class HtmlFullText(BaseHTML2Attributes, BaseIO):
    
    def __init__(self, valid_html):
        BaseIO.__init__(self)
        BaseHTML2Attributes.__init__(self, valid_html)
    
    def _attrib(self, xhtml_str):
        return self.text(xhtml_str)

    
class HtmlTagText(BaseHTML2Attributes, BaseIO):
    
    def __init__(self, valid_html):
        BaseIO.__init__(self)
        BaseHTML2Attributes.__init__(self, valid_html)
    
    def _attrib(self, xhtml_str):
        return self.tags(xhtml_str)


class HtmlScriptText(BaseHTML2Attributes, BaseIO):
    
    def __init__(self, valid_html):
        BaseIO.__init__(self)
        BaseHTML2Attributes.__init__(self, valid_html)
    
    def _attrib(self, xhtml_str):
        return self.scripts(xhtml_str)


class HtmlStyleText(BaseHTML2Attributes, BaseIO):
    
    def __init__(self, valid_html):
        BaseIO.__init__(self)
        BaseHTML2Attributes.__init__(self, valid_html)
    
    def _attrib(self, xhtml_str):
        return self.styles(xhtml_str)
    
