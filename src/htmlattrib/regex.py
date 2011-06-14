
import re
import unicodedata
from filehandlers.basefilehandlers import BaseFileHandler
import abc

class BaseRegexHtmlAttributes(object):
    
    def __init__(self):
        self.proper_html = re.compile(r'<html[^>]*>[\S\s]+</html>', re.UNICODE|re.IGNORECASE)
        self.html_tags = re.compile(r'<[^>]+>')
        self.html_scripts = re.compile(r'<script[^>]*>[\S\s]*?</script>', re.UNICODE|re.IGNORECASE)
        self.html_style = re.compile(r'<style[^>]*>[\S\s]*?</style>', re.UNICODE|re.IGNORECASE)
        self.whitespace_chars = re.compile(r'[\s]+', re.UNICODE)   # {2,}')
        self.unknown_char_seq = re.compile(r'['+ unicodedata.lookup('REPLACEMENT CHARACTER') +']+', re.UNICODE|re.IGNORECASE) #{2,}')
                                           #'['+ unicodedata.lookup('REPLACEMENT CHARACTER') +']+ <-- plus added 8-June-2011                       
    def encoding_norm(self, str):
        """ NOT WORKING AS EXPECTED TO BE FIXED """
        #Normalise unicode text data (Refer to unicodedata module) 
        try:
            encod_str = unicodedata.normalize('NFKC', str)
        except Exception as e:
            print("WHILE UTF-8 NORMALIZATION" % e)  
            encod_str = unicodedata.normalize('NFKC', str.decode('utf-8'))
            print ("STRING ASSUMED TO BE ENCODED-UTF8-BYTE-STRING and DECODED TO PROPER UTF-8")
        return encod_str
        
    def text(self, xhtml_str):
        properhtml = [xhtml_str] #self.proper_html.findall(xhtml_str)
        if not properhtml or properhtml:
            #return None
        #else:
            ph_str  = properhtml[0]
            #Clean-up Scripts
            nonscript_html_str = self.html_scripts.sub('', ph_str)
            #Clean-up Style tags
            nonstyle_html_str = self.html_style.sub('', nonscript_html_str)
            #Clean-up HTML tags
            text = self.html_tags.sub(' ', nonstyle_html_str)
            #Normalise Encoding
            ###norm_text = self.encoding_norm(text)
            #Replace whitespace chars with single space
            text = self.whitespace_chars.sub(' ', text)
            #Replace utf8 'REPLACEMENT CHARACTER' with empty string
            text = self.unknown_char_seq.sub('', text)
            #Remove whitespace from the beginning of text if any
            text = text.lstrip()
            #Remove newline character from the end of text if any
            text = text.rstrip(u'\n')
        return text
    
    def tags(self, xhtml_str):
        pass
    
    def scripts(self, xhtml_str):
        pass
    
    def styles(self, xhtml_str):
        pass
    
    
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
            flist = self.file_list_frmpaths(basepath, filepath_l)
            wpg_txt_ll = list()
            for filename in flist:
                xhtml_src = self.load_files(filename, encoding, error_handling)
                wpg_txt_ll.append( [filename, self._attrib(xhtml_src)]  )
            return wpg_txt_ll
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
    
    