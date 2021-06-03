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
from ..base.io.basefilehandlers import BaseFileHandler
from ..base.io.basefilehandlers import file_list_frmpaths

  
             
class HtmlFullText(BaseHTML2Attributes, BaseFileHandler):
    
    def __init__(self, valid_html):
        BaseFileHandler.__init__(self)
        BaseHTML2Attributes.__init__(self, valid_html)
    
    def _attrib(self, xhtml_str):
        return self.text(xhtml_str)

    def from_src(self, xhtml_str):
        return self._attrib(xhtml_str)

    def from_files(self, xhtml_file_l, encoding='utf8', error_handling='strict'):
        return [
            self.from_src(html_str)
            for html_str in self.load_files(xhtml_file_l, encoding, error_handling)
        ]

    def from_paths(self, basepath, filepath_l, encoding='utf8', error_handling='strict'):
        
        flist = file_list_frmpaths(basepath, filepath_l)
        
        fname_script_ll = list()

        for filename in flist:
            xhtml_src = self.load_files(filename, encoding, error_handling)
            fname_script_ll.append([filename, self.from_src(xhtml_src)])

        return fname_script_ll


    
class HtmlTagText(HtmlFullText):
    
    def __init__(self, *args, **kwrgs):
        super(HtmlTagText, self).__init__(*args, **kwrgs)
        
    def _attrib(self, xhtml_str):
        return self.tags(xhtml_str)



class HtmlScriptText(HtmlFullText):
    
    def __init__(self, *args, **kwrgs):
        super(HtmlScriptText, self).__init__(*args, **kwrgs)
    
    def _attrib(self, xhtml_str):
        return self.scripts(xhtml_str)



class HtmlStyleText(HtmlFullText):
    
    def __init__(self, *args, **kwrgs):
        super(HtmlStyleText, self).__init__(*args, **kwrgs)
    
    def _attrib(self, xhtml_str):
        return self.styles(xhtml_str)
    
