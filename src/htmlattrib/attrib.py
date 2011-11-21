
from filehandlers.basefilehandlers import BaseFileHandler
import abc
from regex import BaseRegexHtmlAttributes
import tables as tb

class BaseHtmlAttrib(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def _attrib(self, xhtml_str): #Abstract method cannot be private (__methodname) method!
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
    
    def from_src2tbls(self, fileh, tablesGroup, xhtml_str, tbname="tbarray1"):
        terms_tb_arr = fileh.createTable(tablesGroup, tbname, self._attrib(xhtml_str), '')
        return terms_tb_arr
        
    def from_files2tbls(self, fileh, tablesGroup, xhtml_file_l, encoding='utf8', error_handling='strict'):
        for filename, html_str in zip(xhtml_file_l, self.load_files(xhtml_file_l, encoding, error_handling)):
            terms_tb_arr = fileh.createArray(tablesGroup, filename.split('/')[-1], self._attrib(html_str), '')
            terms_tb_arr._v_attrs.filepath = filename 
            terms_tb_arr._v_attrs.terms_num = len(terms_tb_arr.read())
        return tablesGroup  
        
    def from_paths2tbls(self, fileh, tablesGroup, basepath, filepath_l, encoding='utf8', error_handling='strict'):
        xhtml_file_l = self.file_list_frmpaths(basepath, filepath_l)
        tablesGroup = self.from_files2tbls(self, fileh, tablesGroup, xhtml_file_l, encoding, error_handling)
        return (tablesGroup, xhtml_file_l) 
    
             
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
    
    