
from filehandlers.basefilehandlers import BaseFileHandler
import abc
from regex import BaseRegexHtmlAttributes

class BaseHtmlAttrib(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def _attrib(self, xhtml_str): #Abstractmethod cannot be private (__methodname) method!
        pass
    
    def from_src(self, xhtml_str):
        return self._attrib(xhtml_str)
        
    def from_files(self, xhtml_file_l, encoding='utf8', error_handling='strict'):
        text_l = [ self._attrib(html_str) for html_str in self.load_files(xhtml_file_l, encoding, error_handling) ]
        return text_l  
        
    def from_paths(self, basepath, filepath_l, encoding='utf8', error_handling='strict', low_mem=False):
        
        if low_mem:
            ###THIS IS THE FIRST PYTABLES INTERFACE
            flist = self.file_list_frmpaths(basepath, filepath_l)
            wpg_txt_ll = list()
            for filename in flist:
                xhtml_src = self.load_files(filename, encoding, error_handling)
                wpg_txt_ll.append( [filename, self._attrib(xhtml_src)]  )
            return wpg_txt_ll
            ###THIS IS THE FIRST PYTABLES INTERFACE
        else:  
            return [ [wbpg, self._attrib(html_src)] for wbpg, html_src in\
                        self.load_frmpaths(basepath, filepath_l, encoding, error_handling) ]
    
             
class HtmlText(BaseHtmlAttrib, BaseFileHandler, BaseRegexHtmlAttributes):
    
    def __init__(self):
        BaseFileHandler.__init__(self)
        BaseRegexHtmlAttributes.__init__(self)
    
    def _attrib(self, xhtml_str):
        return self.text(xhtml_str)

    
class HtmlTags(BaseHtmlAttrib, BaseFileHandler, BaseRegexHtmlAttributes):
    
    def __init__(self):
        BaseFileHandler.__init__(self)
        BaseRegexHtmlAttributes.__init__(self)
    
    def _attrib(self, xhtml_str):
        return self.tags(xhtml_str)


class HtmlScripts(BaseHtmlAttrib, BaseFileHandler, BaseRegexHtmlAttributes):
    
    def __init__(self):
        BaseFileHandler.__init__(self)
        BaseRegexHtmlAttributes.__init__(self)
    
    def _attrib(self, xhtml_str):
        return self.scripts(xhtml_str)


class HtmlStyles(BaseHtmlAttrib, BaseFileHandler, BaseRegexHtmlAttributes):
    
    def __init__(self):
        BaseFileHandler.__init__(self)
        BaseRegexHtmlAttributes.__init__(self)
    
    def _attrib(self, xhtml_str):
        return self.styles(xhtml_str)
    
    