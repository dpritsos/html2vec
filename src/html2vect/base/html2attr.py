#
#    Module: Html2Terms - Contains all the Common Methods for all Html2TF Classes
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2vect.base.html2attr: submodule of `html2vect` module defines the classes: Html2Terms() """

from ..base.features.html2attrib import BaseHTML2Attributes



class Html2Attr(object):
    
    
    def __init__(self, attrib, lowercase, valid_html):
        
        #HTML to attributes Class
        self.h2attr = BaseHTML2Attributes( valid_html )
        
        if attrib == "text":
            self._attrib = self.h2attr.text
        elif attrib == "tags":
            self._attrib = self.s2tf.tags
                        
        if lowercase:
            self._attrib = self._lower( self._attrib )
    
    
    def _lower(self, methd):
        
        def lowerCase(*args, **kwrgs):
            return methd(*args, **kwrgs).lower()
        
        return lowerCase
    
    