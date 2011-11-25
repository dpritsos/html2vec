""" """

from htmlattrib.attrib import HtmlText

class BaseString2NgramList(object):
    
    def __init__(self, n):
        self.n = n
        #self.ngrms_l = list()
    
    def terms_lst(self, text):
        if not text:
            return None
        ngrms_l =  list()
        for i in range( len(text) - self.n + 1 ): 
            ngrms_l.append( text[i : i+self.n]  )
        #ngrms_l.sort() #it is nice to be sorted and to conform with numpy.unique1d results   
        return ngrms_l
    
    
class BaseString2TFTP(BaseString2NgramList):
    
    def __init__(self, n):
        BaseString2NgramList.__init__(self, n)
    
    def nf_dict(self, text):
        if not text:
            return None
        #Create NGram List if has been not previously generated
        ngrms_l = self.terms_lst(text)
        #Count NGrams and Build the Ngram-Frequency (TF) dictionary 
        NgF_d = dict()
        for ng in ngrms_l:
            if ng in NgF_d: #if the dictionary of terms has the 'terms' as a key 
                NgF_d[ ng ] += 1
            else: 
                NgF_d[ ng ] = 1 
        return NgF_d  
    
    def npos_dict(self, text):
        if not text:
            return None
        #Create NGram List if has been not previously generated    
        ngrms_l = self.terms_lst(text)
        NgPos_d = dict()
        for i, ng in enumerate(ngrms_l):
            if ng in NgPos_d: #if the dictionary of terms has the 'terms' as a key 
                NgPos_d[ ng ].append(i)
            else: 
                NgPos_d[ ng ] = [ i ] 
        return NgPos_d
  

class Html2TF(BaseString2TFTP, HtmlText):
    
    def __init__(self, n=3, lowercase=False):
        HtmlText.__init__(self)
        BaseString2TFTP.__init__(self, n)
        if lowercase:
            self._attrib = self.__attrib_lowercase
        
    def _attrib(self, xhtml_str):
        return self.nf_dict( self.text( xhtml_str ) )
    
    def __attrib_lowercase(self, xhtml_str):
        return self.nf_dict( self.text( xhtml_str ).lower() )
    
    
class Html2TP(BaseString2TFTP, HtmlText):
    
    def __init__(self, n=3, lowercase=False):
        HtmlText.__init__(self)
        BaseString2TFTP.__init__(self, n)
        if lowercase:
            self._attrib = self.__attrib_lowercase
        
    def _attrib(self, xhtml_str):
        return self.npos_dict( self.text( xhtml_str ) )
    
    def __attrib_lowercase(self, xhtml_str):
        return self.npos_dict( self.text( xhtml_str ).lower() )
    