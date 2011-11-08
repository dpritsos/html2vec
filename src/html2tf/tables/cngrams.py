""" """

from htmlattrib.attrib import HtmlText
from html2tf.dictionaries.cngrams import BaseString2NgramList 


class BaseString2TFTP(BaseString2NgramList):
    
    def __init__(self, n):
        self.n = n
        self.ngrms_l = list()
    
    def terms_lst(self, text):
        if not text:
            return None
        for i in range( len(text) - self.n + 1 ): 
            self.ngrms_l.append( text[i : i+self.n]  )
        return self.ngrms_l
            
    def tf_array(self, text):
        if not text:
            return None
        #Find and Count NGrams
        if not self.ngrms_l:
            self.terms_lst(text)  
        NgF_d = dict()
        for ng in self.ngrms_l:
            if ng in NgF_d: #if the dictionary of terms has the 'terms' as a key 
                NgF_d[ ng ] += 1
            else: 
                NgF_d[ ng ] = 1 
        return NgF_d
    
    def npos_array(self, text):
        if not text:
            return None
        #Find and Count NGrams
        if not self.ngram_l:
            self.terms_lst(text)
    

class Html2TF(BaseString2TF, HtmlText):
    
    def __init__(self, n=3, lowercase=False):
        HtmlText.__init__(self)
        BaseString2TF.__init__(self, n)
        if lowercase:
            self._attrib = self.__attrib_lowercase
        
    def _attrib(self, xhtml_str):
        return self.nf_dict( self.text( xhtml_str ) )
    
    def __attrib_lowercase(self, xhtml_str):
        return self.nf_dict( self.text( xhtml_str ).lower() )
    