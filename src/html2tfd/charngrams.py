""" """

import re
from htmlattrib.regex import HtmlText


class BaseString2TF(object):
    
    def __init__(self, n):
        reg_ng_size = r'.{' + str(n) + '}'
        self.ngrams = re.compile( reg_ng_size, re.UNICODE )
    
    def nf_dict(self, text):
        if not text:
            return None
        #Find and Count NGrams
        ngrms_l = self.ngrams.findall(text)
        NgF_d = dict()
        for ng in ngrms_l:
            if ng in NgF_d: #if the dictionary of terms has the 'terms' as a key 
                NgF_d[ ng ] += 1
            else: 
                NgF_d[ ng ] = 1 
        return NgF_d
    

class Html2TF(BaseString2TF, HtmlText):
    
    def __init__(self, n=3):
        HtmlText.__init__(self)
        BaseString2TF.__init(self, n)
    
    def _attrib(self, xhtml_str):
        return self.nf_dict( self.text( xhtml_str ) )
    