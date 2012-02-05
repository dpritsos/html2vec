"""

"""
import re
import os
import codecs
import xml.etree 
import unicodedata
import sys
from basicfiletools import BaseFileTools

class BaseHTMLFileTools(BaseFileTools):

    def __load_html_file(self, filename, encoding='utf-8', error_handling='strict'):
        """ __load_tf_dict(): do not use this function prefer the VHTools.load_tf_dict(). 
            This function is getting a filename and a lower case force option and returns a 
            Term-Frequency dictionary loaded from the file given as argument. """
        try:
            fenc = codecs.open( filename, 'rb',  encoding, error_handling) 
        except Exception as e:
            print("BaseHTMLFileTools.load_dict() FILE %s ERROR: %s" % (filename, e))
            return None
        try:
            xhtml_str = fenc.read()
        except Exception as e:
            print("BaseHTMLFileTools.load_dict() FILE %s ERROR: %s" % (filename, e))
            return None
        finally:
            fenc.close()    
        return xhtml_str  
    
    def load_html_files(self, filename_l, encoding='utf-8', error_handling='strict'):
        """ load_tf_dict(): is getting a filename or a (filename list) and lower case force option
            as arguments. It returns a Term-Frequency Dictionary which is a merged dictionary of all
            TF dictionaries given a argument """
        if isinstance(filename_l, str):
            return self.__load_html_file(filename_l, encoding, error_handling)
        elif isinstance(filename_l, list):
            file_lst = list()
            for filename in filename_l:
                file_lst.append( self.__load_html_file(filename, encoding, error_handling) )
            return file_lst
        else:
            raise Exception("A String or a list of Strings was Expected as input")
    
    def load_html_frmpaths(self, basepath, filepath_l, encoding='utf8', error_handling='strict'):
        """ __exec_on_files_frmpaths(): is executing a function given as the first argument to all the
            files found in the file-paths list given third and second argument. Optionally a fore lower
            case argument can be given. """
        fname_lst = BaseHTMLFileTools.file_list_frmpaths(basepath, filepath_l)
        return  fname_lst, self.load_html_files(fname_lst, encoding, error_handling)


class BaseHTML2TFRegexTools(object):
    
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
        
    def get_proper_numbers(self, terms_l, xhtml_TF):
        num_free_tl = list()
        for term in terms_l:
            num_term_l = self.proper_num.findall(term)
            if num_term_l: #if a number found the the term should be the number so we keep it as it is
                #for i in range(len(num_term_l[0])):
                #    use this for-loop in case you want to know the exact form of the number.
                #    Each from has a position with the following order 1)xxxxxx 2)xxxx,xxxx 3)xxxx.xxxx 4)333.333.333...333,xxxxxx 5)333,333,333,333,,,333.xxxxxx
                if term in xhtml_TF: #if the dictionary of terms has the 'terms' as a key 
                    xhtml_TF[term] += 1
                else:    
                    xhtml_TF[term] = 1
            else:
                #Keep only Non-Number terms or Non-proper-numbers
                num_free_tl.append(term)
        return num_free_tl
    
    def get_comma_n_trms(self, terms_l, xhtml_TF):
        comma_free_tl = list()
        for term in terms_l:
            #Decompose the terms that in their char set include comma symbol to a list of comma separated terms and the comma(s) 
            decomp_term_l = self.comma_decomp.findall(term)
            if len(decomp_term_l) > 1:
                for subterm in decomp_term_l:
                    if self.comma_str.findall(subterm):
                        if subterm in xhtml_TF: #if the dictionary of terms has the 'terms' as a key 
                            xhtml_TF[subterm] += 1
                        else:    
                            xhtml_TF[subterm] = 1
                    else: #if the substring is not a comma string then forward for farther analysis 
                        comma_free_tl.append(subterm)
            else:
                #Keep only the terms that are already free of commas because the other have been already decomposed and counted
                comma_free_tl.append(term)
        #use the comma_free terms list as the terms list to continue processing
        return comma_free_tl
    
    def get_dot_n_trms(self, terms_l, xhtml_TF):
        dot_free_tl = list()
        for term in terms_l:
            decomp_term = self.dot_decomp.findall(term)
            dec_trm_len = len(decomp_term)
            if dec_trm_len > 1 and dec_trm_len <= 3: 
                #Here we have the cases of ...CCC or .CC or CC.... or CCC. or CC.CCC or CCCC....CCCC so keep each sub-term
                for sub_term in decomp_term:
                    if self.dot_str.findall(sub_term):
                        if sub_term in xhtml_TF: 
                            xhtml_TF[sub_term] += 1
                        else:
                            xhtml_TF[sub_term] = 1
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
                    if sub_term in xhtml_TF: 
                        xhtml_TF[sub_term] += 1
                    else:
                        xhtml_TF[sub_term] = 1
                #Re-compose the term without suffix/prefix dot-sequence and give it for further analysis 
                dot_free_tl.append( "".join(decomp_term) )
            else:
                if self.dot_str.findall(term): #in case of one element in the list check if it is a dot-sequence
                    if term in xhtml_TF: 
                        xhtml_TF[term] += 1
                    else:
                        xhtml_TF[term] = 1
                else: #keep already the dot-free terms    
                    dot_free_tl.append(term) 
        return  dot_free_tl
        
    def get_propr_trms_n_symbs(self, terms_l, xhtml_TF):
        clean_term_tl = list()
        for term in terms_l:
            #Get the 
            symb_term_l = self.fredsb_clean.findall(term)
            if symb_term_l:
                #Keep and count the symbols found 
                for symb in symb_term_l:
                    if symb in xhtml_TF: #if the dictionary of terms has the 'terms' as a key 
                        xhtml_TF[symb] += 1
                    else: 
                        xhtml_TF[symb] = 1
                clean_trm = self.fredsb_clean.sub('', term)
                if clean_trm in xhtml_TF: #if the dictionary of terms has the 'terms' as a key 
                    xhtml_TF[clean_trm] += 1
                elif clean_trm: #if not empty string (Just in case)
                    xhtml_TF[clean_trm] = 1
            else:
                #Keep only the terms that are already free of commas because the other have been already decomposed and counted
                clean_term_tl.append(term)
        #use the comma_free terms list as the terms list to continue processing
        return clean_term_tl
    
    def term_len_limit(self, term_l, limit):
        norm_term_l = list()
        for term in term_l:
            if len(term) <= limit:
                norm_term_l.append(term)
        return norm_term_l
    
    def keep_encoding(self, term_l, encoding='ascii'):
        pass
   
     
class BaseRegexTextExtraction(object):
    
    count = 0
    
    def __init__(self):
        self.proper_html = re.compile(r'<html[^>]*>[\S\s]+</html>', re.UNICODE|re.IGNORECASE)
        self.html_tags = re.compile(r'<[^>]+>')
        self.html_scripts = re.compile(r'<script[^>]*>[\S\s]*?</script>', re.UNICODE|re.IGNORECASE)
        self.html_style = re.compile(r'<style[^>]*>[\S\s]*?</style>', re.UNICODE|re.IGNORECASE)
        self.whitespace_chars = re.compile(r'[\s]+', re.UNICODE)   # {2,}')
        self.unknown_char_seq = re.compile(r'['+ unicodedata.lookup('REPLACEMENT CHARACTER') +']', re.UNICODE|re.IGNORECASE)   # {2,}')
    
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
        
    def extract_text(self, xhtml_str):
        properhtml = self.proper_html.findall(xhtml_str)
        if not properhtml:
            return None
        else:
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
               
        return text


class BaseXmlTextExtraction(object):
    
    def __init__(self):
        """ TO BE IMPLEMENTED """
        pass
        
    def extract_text(self, xhtml_str):
        """ TO BE IMPLEMENTED """
        pass


class HTML2NgFTools(BaseHTMLFileTools):
    
    def __init__(self, n=3):
        reg_ng_size = r'.{' + str(n) + '}'
        self.ngrams = re.compile( reg_ng_size, re.UNICODE )
    
    def nf_dict(self, xhtml_str):
        text = self.extract_text(xhtml_str)
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
    
    def nf_dict_l(self, xhtml_str_l):
        nf_d_list = list()
        for xhtml_str in xhtml_str_l:
            nf_d_list.append( self.nf_dict(xhtml_str) )
        return nf_d_list
        
    def nf_d_frmfiles(self, xhmtl_file_l, encoding='utf8', error_handling='strict'):
        html_str_l = self.load_html_files(xhmtl_file_l, encoding, error_handling)
        return self.nf_dict_l(html_str_l) 
        
    def nf_d_frmpaths(self, basepath, filepath_l, encoding='utf8', error_handling='strict', low_men=False):
        if low_men:
            flist = BaseHTMLFileTools.file_list_frmpaths(basepath, filepath_l)
            nf_d_list = list()
            wbpg_l = list()
            for filename in flist:
                xhtml_src = self.load_html_files(filename, encoding, error_handling)
                nf_d_list.append( self.nf_dict(xhtml_src) )
                wbpg_l.append(filename)
            return wbpg_l, nf_d_list
        else:
            wbpg_l, html_str_l = self.load_html_frmpaths(basepath, filepath_l, encoding, error_handling)  
            return wbpg_l, self.nf_dict_l(html_str_l)


class RegexHTML2NgFTools(HTML2NgFTools, BaseRegexTextExtraction):
    
    def __init__(self, n=3):
        BaseRegexTextExtraction.__init__(self)
        HTML2NgFTools.__init__(self, n)


class XmlHTML2NgFTools(HTML2NgFTools, BaseXmlTextExtraction):
    
    def __init__(self, n=3):
        BaseXmlTextExtraction.__init__(self)
        HTML2NgFTools.__init__(self, n)


 
class HTML2TFTools(BaseHTML2TFRegexTools, BaseRegexTextExtraction, BaseHTMLFileTools):
    
    def __init__(self):
        BaseHTML2TFRegexTools.__init__(self)    
        BaseRegexTextExtraction.__init__(self)
        
    def tf_dict(self, xhtml_str):
        text = self.extract_text(xhtml_str)
        if not text:
            return None
        #Initially split the text to terms separated by white-spaces [ \t\n\r\f\v] 
        terms_l = self.white_spliter.split(text)
        #Any term has more than 512 characters is rejected
        terms_l = self.term_len_limit(terms_l, 512)
        #Create the Word Term Frequency Vectors (Dictionary) 
        tf_d = dict()
        #Count and remove the Numbers form the terms_l
        terms_l = self.get_proper_numbers(terms_l, tf_d)
        #Decompose the terms to sub-terms of any symbol but comma (,) and comma sub-term(s)
        terms_l = self.get_comma_n_trms(terms_l, tf_d)
        #Split term to words upon dot (.) and dot needs special treatment because we have the case of . or ... and so on
        terms_l = self.get_dot_n_trms(terms_l, tf_d)
        #Count and clean-up the non-alphanumeric symbols ONLY from the Beginning and the End of the terms
        ##except dot (.) and percentage % at the end for the term)
        terms_l = self.get_propr_trms_n_symbs(terms_l, tf_d) 
        for term in terms_l:            
            if self.white_spliter.findall(term):
                raise Exception("ERROR %s" % self.white_spliter.findall(term) )
            if term in tf_d: #if the dictionary of terms has the 'terms' as a key 
                tf_d[term] += 1
            elif term:
                tf_d[term] = 1                    
        return tf_d 
    
    def tf_dict_l(self, xhtml_str_l):
        tf_d_list = list()
        for xhtml_str in xhtml_str_l:
            tf_d_list.append( self.tf_dict(xhtml_str) )
        return tf_d_list

    def tf_d_frmfiles(self, xhmtl_file_l, encoding='utf8', error_handling='strict'):
        html_str_l = self.load_html_files(xhmtl_file_l, encoding, error_handling)
        return self.tf_dict_l(html_str_l) 
    
    def tf_d_frmpaths(self, basepath, filepath_l, encoding='utf8', error_handling='strict', low_men=False):
        if low_men:
            flist = BaseHTMLFileTools.file_list_frmpaths(basepath, filepath_l)
            tf_d_list = list()
            wbpg_l = list()
            for filename in flist:
                xhtml_src = self.load_html_files(filename, encoding, error_handling)
                tf_d_list.append( self.tf_dict(xhtml_src) )
                wbpg_l.append(filename)
            return wbpg_l, tf_d_list
        else:
            wbpg_l, html_str_l = self.load_html_frmpaths(basepath, filepath_l, encoding, error_handling)  
            return wbpg_l, self.tf_dict_l(html_str_l)


class RegexHTML2TFTools(HTML2TFTools, BaseRegexTextExtraction):
    
    def __init__(self):
        BaseRegexTextExtraction.__init__(self)
        HTML2TFTools.__init__(self)


class XmlHTML2TFTools(HTML2TFTools, BaseXmlTextExtraction):
    
    def __init__(self):
        BaseXmlTextExtraction.__init__(self)
        HTML2TFTools.__init__(self)


#Unit Test
if __name__ == "__main__":
    
    files_path = '/home/dimitrios/Documents/Synergy-Crawler/saved_pages/news/'
    
    html2nf = RegexHTML2NgFTools(3)
    html2tf = RegexHTML2TFTools()
    
    wpg_l, tf_d_l = html2nf.nf_d_frmpaths(None, files_path, error_handling='ignore', low_men=True)
    print wpg_l[0] 
    print tf_d_l[0], len(tf_d_l[0])
    
    del wpg_l
    del tf_d_l

    wpg_l, tf_d_l = html2tf.tf_d_frmpaths(None, files_path, error_handling='ignore', low_men=True)
    print wpg_l[0] 
    print tf_d_l[0], len(tf_d_l[0])

















