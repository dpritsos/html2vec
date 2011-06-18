""" """

import re
from htmlattrib.regex import HtmlText
import tfdhandler


class BaseWordExtractionRegexTools(object):
    
    def __init__(self):    
        #Whitespace characters [<space>\t\n\r\f\v] matching, for splitting the raw text to terms
        self.white_spliter = re.compile(r'[\s]+', re.UNICODE)
        #Find URL String. Probably anchor text
        self.url_str = re.compile(r'(((ftp://|FTP://|http://|HTTP://|https://|HTTPS://)?(www|[^\s()<>.?]+))?([.]?[^\s()<>.?]+)+?(?=.org|.edu|.tv|.com|.gr|.gov|.uk)(.org|.edu|.tv|.com|.gr|.gov|.uk){1}([/]\S+)*[/]?)', re.UNICODE|re.IGNORECASE)
        #Comma decomposer
        self.comma_decomp = re.compile(r'[^,]+|[,]+', re.UNICODE|re.IGNORECASE)
        self.comma_str = re.compile(r'[,]+', re.UNICODE|re.IGNORECASE)
        #Find dot or sequence of dots
        self.dot_str = re.compile(r'[.]+', re.UNICODE)
        self.dot_decomp = re.compile(r'[^.]+|[.]+', re.UNICODE)
        #Symbol term decomposer 
        self.fredsb_clean = re.compile(r'^[^\w]+|[^\w%]+$', re.UNICODE) #front-end-symbol-cleaning => fredsb_clean
        #Find proper number
        self.proper_num = re.compile(r'(^[0-9]+$)|(^[0-9]+[,][0-9]+$)|(^[0-9]+[.][0-9]+$)|(^[0-9]{1,3}(?:[.][0-9]{3})+[,][0-9]+$)|(^[0-9]{1,3}(?:[,][0-9]{3})+[.][0-9]+$)', re.UNICODE)
        
    def get_proper_numbers(self, terms_l):
        tf_d = dict()
        num_free_tl = list()
        for term in terms_l:
            num_term_l = self.proper_num.findall(term)
            if num_term_l: #if a number found the the term should be the number so we keep it as it is
                #for i in range(len(num_term_l[0])):
                #    use this for-loop in case you want to know the exact form of the number.
                #    Each from has a position with the following order 1)xxxxxx 2)xxxx,xxxx 3)xxxx.xxxx 4)333.333.333...333,xxxxxx 5)333,333,333,333,,,333.xxxxxx
                if term in tf_d: #if the dictionary of terms has the 'terms' as a key 
                    tf_d[term] += 1
                else:    
                    tf_d[term] = 1
            else:
                #Keep only Non-Number terms or Non-proper-numbers
                num_free_tl.append(term)
        return tf_d, num_free_tl
    
    def get_comma_n_trms(self, terms_l):
        tf_d = dict()
        comma_free_tl = list()
        for term in terms_l:
            #Decompose the terms that in their char set include comma symbol to a list of comma separated terms and the comma(s) 
            decomp_term_l = self.comma_decomp.findall(term)
            if len(decomp_term_l) > 1:
                for subterm in decomp_term_l:
                    if self.comma_str.findall(subterm):
                        if subterm in tf_d: #if the dictionary of terms has the 'terms' as a key 
                            tf_d[subterm] += 1
                        else:    
                            tf_d[subterm] = 1
                    else: #if the substring is not a comma string then forward for farther analysis 
                        comma_free_tl.append(subterm)
            else:
                #Keep only the terms that are already free of commas because the other have been already decomposed and counted
                comma_free_tl.append(term)
        #use the comma_free terms list as the terms list to continue processing
        return tf_d, comma_free_tl
    
    def get_dot_n_trms(self, terms_l):
        tf_d = dict()
        dot_free_tl = list()
        for term in terms_l:
            decomp_term = self.dot_decomp.findall(term)
            dec_trm_len = len(decomp_term)
            if dec_trm_len > 1 and dec_trm_len <= 3: 
                #Here we have the cases of ...CCC or .CC or CC.... or CCC. or CC.CCC or CCCC....CCCC so keep each sub-term
                for sub_term in decomp_term:
                    if self.dot_str.findall(sub_term):
                        if sub_term in tf_d: 
                            tf_d[sub_term] += 1
                        else:
                            tf_d[sub_term] = 1
                    else: #give the new terms for farther analysis
                        dot_free_tl.append(sub_term)
            elif dec_trm_len > 3: #i.e. Greater thatn 3
                #Remove the first and the last dot sub-string and let the rest of the term as it was (but the prefix and suffix of dot(s))
                sub_term_l = list()
                #Extract dot-sequence prefix if any 
                if self.dot_str.findall(decomp_term[0]):
                    sub_term_l.append( decomp_term.pop(0) )
                #Extract dot-sequence suffix if any
                l_end = len(decomp_term) - 1
                if self.dot_str.findall(decomp_term[l_end]):
                    sub_term_l.append( decomp_term.pop(l_end) )
                #Count dot-sequence terms 
                for sub_term in sub_term_l:                  
                    if sub_term in tf_d: 
                        tf_d[sub_term] += 1
                    else:
                        tf_d[sub_term] = 1
                #Re-compose the term without suffix/prefix dot-sequence and give it for further analysis 
                dot_free_tl.append( "".join(decomp_term) )
            else:
                if self.dot_str.findall(term): #in case of one element in the list check if it is a dot-sequence
                    if term in tf_d: 
                        tf_d[term] += 1
                    else:
                        tf_d[term] = 1
                else: #keep already the dot-free terms    
                    dot_free_tl.append(term) 
        return tf_d, dot_free_tl
        
    def get_propr_trms_n_symbs(self, terms_l):
        tf_d = dict()
        clean_term_tl = list()
        for term in terms_l:
            #Get the 
            symb_term_l = self.fredsb_clean.findall(term)
            if symb_term_l:
                #Keep and count the symbols found 
                for symb in symb_term_l:
                    if symb in tf_d: #if the dictionary of terms has the 'terms' as a key 
                        tf_d[symb] += 1
                    else: 
                        tf_d[symb] = 1
                clean_trm = self.fredsb_clean.sub('', term)
                if clean_trm in tf_d: #if the dictionary of terms has the 'terms' as a key 
                    tf_d[clean_trm] += 1
                elif clean_trm: #if not empty string (Just in case)
                    tf_d[clean_trm] = 1
            else:
                #Keep only the terms that are already free of commas because the other have been already decomposed and counted
                clean_term_tl.append(term)
        #use the comma_free terms list as the terms list to continue processing
        return tf_d, clean_term_tl
    
    def term_len_limit(self, term_l, limit):
        norm_term_l = list()
        for term in term_l:
            if len(term) <= limit:
                norm_term_l.append(term)
        return norm_term_l


class BaseString2TF(BaseWordExtractionRegexTools):
    
    def __init__(self):    
        BaseWordExtractionRegexTools.__init__(self)
        self.__tfd_hdlr = tfdhandler.TFdictHandler()
        
    def tf_dict(self, text):
        if not text:
            return None
        #Initially split the text to terms separated by white-spaces [ \t\n\r\f\v] 
        terms_l = self.white_spliter.split(text)
        #Any term has more than 512 characters is rejected
        terms_l = self.term_len_limit(terms_l, 512)
        #Create the Word Term Frequency Vectors (Dictionary) 
        tf_d = dict()
        #Count and remove the Numbers form the terms_l
        res_tfd, terms_l = self.get_proper_numbers(terms_l)
        tf_d = self.__tfd_hdlr.merge_tf_dicts(tf_d, res_tfd)
        #Decompose the terms to sub-terms of any symbol but comma (,) and comma sub-term(s)
        res_tfd, terms_l = self.get_comma_n_trms(terms_l)
        tf_d = self.__tfd_hdlr.merge_tf_dicts(tf_d, res_tfd)
        #Split term to words upon dot (.) and dot needs special treatment because we have the case of . or ... and so on
        res_tfd, terms_l = self.get_dot_n_trms(terms_l)
        tf_d = self.__tfd_hdlr.merge_tf_dicts(tf_d, res_tfd)
        #Count and clean-up the non-alphanumeric symbols ONLY from the Beginning and the End of the terms
        ##except dot (.) and percentage % at the end for the term)
        res_tfd, terms_l = self.get_propr_trms_n_symbs(terms_l)
        tf_d = self.__tfd_hdlr.merge_tf_dicts(tf_d, res_tfd) 
        for term in terms_l:            
            if self.white_spliter.findall(term):
                raise Exception("ERROR %s" % self.white_spliter.findall(term) )
            if term in tf_d: #if the dictionary of terms has the 'terms' as a key 
                tf_d[term] += 1
            elif term:
                tf_d[term] = 1                    
        return tf_d 

   
class Html2TF(BaseString2TF, HtmlText):
    
    def __init__(self, lowercase=False):
        HtmlText.__init__(self)
        BaseString2TF.__init__(self)
        if lowercase:
            self._attrib = self.__attrib_lowercase
        else:
            self._attrib = self.__attrib
        
    def __attrib(self, xhtml_str):
        return self.tf_dict( self.text( xhtml_str ) )
    
    def __attrib_lowercase(self, xhtml_str):
        return self.tf_dict( self.text( xhtml_str ).lower() )
    
    
    