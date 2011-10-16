
import re
import unicodedata
from filehandlers.basefilehandlers import BaseFileHandler
import htmlentitydefs as hedfs
import abc
import htmltagslist 

class BaseLXMLHtmlAttributes(object):
    
    def __init__(self):
        pass
    
    def tags(self, xhtml_str):
        pass
    
    def scripts(self, xhtml_str):
        pass
    
    def styles(self, xhtml_str):
        pass
    
    
    