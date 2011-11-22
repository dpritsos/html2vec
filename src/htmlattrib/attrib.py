
from filehandlers.basefilehandlers import BaseFileHandler
import abc
from regex import BaseRegexHtmlAttributes
import numpy as np
from html2tf.tables import tbtools


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
            terms_tb_arr = fileh.createTable(tablesGroup, filename.split('/')[-1].split('.')[0], self._attrib(html_str), '')
            terms_tb_arr._v_attrs.filepath = filename 
            terms_tb_arr._v_attrs.terms_num = np.sum(terms_tb_arr.read()['freq'])
        return tablesGroup  
        
    def from_paths2tbls(self, fileh, tablesGroup, grn_wpg_tbl_name, basepath, filepath_l, encoding='utf8', error_handling='strict'):
        xhtml_file_l = self.file_list_frmpaths(basepath, filepath_l)
        tablesGroup = self.from_files2tbls(fileh, tablesGroup, xhtml_file_l, encoding, error_handling)
        GenrePageListTable = fileh.createTable(tablesGroup, grn_wpg_tbl_name, tbtools.default_GenreTable_Desc)
        for i, filename in enumerate(xhtml_file_l):
            GenrePageListTable.row['wpg_id' ] = i 
            GenrePageListTable.row['wpg_name' ] = filename 
            #GenrePageListTable.row['link_lst' ] = np.zeros(100)
            GenrePageListTable.row.append()
        GenrePageListTable.flush() 
        return (tablesGroup, GenrePageListTable) 
    
             
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
    
    