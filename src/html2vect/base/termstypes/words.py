#
#    Module: words - Natural Language Dictionary Words as Terms Types      
# 
#    Author: Dimitrios Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2vect.base.termstypes.words: submodule of `html2vect` module defines the class String2WordList """ 

import re

class String2WordList(object):
    
    def __init__(self):
            
        #Whitespace characters [<space>\t\n\r\f\v] matching, for splitting the raw text to terms
        self.white_spliter = re.compile(r'[\s]+', re.UNICODE)
        
        #Find URL String. Probably anchor text
        self.url_str = re.compile(r'(((ftp://|FTP://|http://|HTTP://|https://|HTTPS://)?(www|[^\s()<>.?]+))?([.]?[^\s()<>.?]+)+?(?=.org|.edu|.tv|.com|.gr|.gov|.uk)(.org|.edu|.tv|.com|.gr|.gov|.uk){1}([/]\S+)*[/]?)', re.UNICODE|re.IGNORECASE)
        
        #Comma decomposer
        self.comma_decomp = re.compile(r'[^,]+(?=,)|(?<=,)[^,]+|[,]+', re.UNICODE|re.IGNORECASE)
        
        #Find dot or sequence of dots
        self.dot_str = re.compile(r'[.]+', re.UNICODE)
        self.dot_decomp = re.compile(r'[^.]+(?=\.)|(?<=\.)[^.]+|[.]+', re.UNICODE)
        
        #Symbol term decomposer 
        self.fredsb_clean = re.compile(r'^[\W]|[^\w%]$', re.UNICODE) #front-end-symbol-cleaning => fredsb_clean
        
        #Find proper number
        self.proper_num = re.compile(r'(^[0-9]+$)|(^[0-9]+[,][0-9]+$)|(^[0-9]+[.][0-9]+$)|(^[0-9]{1,3}(?:[.][0-9]{3})+[,][0-9]+$)|(^[0-9]{1,3}(?:[,][0-9]{3})+[.][0-9]+$)', re.UNICODE)
        
        
    def terms_lst(self, text):
        
        #In case not text is given it returns None. The outer code layer should handle this if caused due to error. 
        if not text:
            return None
        
        #The list of Word terms will result after the terms list will be passed from some feature extractors 
        analysed_terms_l = list()
        #list of idxs to be removed from the main terms_l after the feature extractors
        fnd_idx_l = list()
        
        #Initially split the text to terms separated by white-spaces [ \t\n\r\f\v] 
        terms_l = self.white_spliter.split(text)
        
        #Any term has more than 512 characters is rejected
        terms_l = self.__term_len_limit(terms_l, 512)
        
        #Extract the Numbers form the terms_l
        num_trm_l, fidx_l = self.__extract_proper_numbers(terms_l)
        analysed_terms_l.extend(num_trm_l)
        fnd_idx_l.extend(fidx_l)
        
        #Remove the already analysed terms after finding the proper numbers
        terms_l = [trm for trm in terms_l if terms_l.index(trm) not in fnd_idx_l]        
        #Clean-up the index list because items already removed
        fnd_idx_l = []
        
        #Extract the terms to sub-terms of any symbol but comma (,) and comma sub-term(s)
        comma_trm_l, fidx_l  = self.__extract_comma_n_trms(terms_l)
        analysed_terms_l.extend(comma_trm_l)
        fnd_idx_l.extend(fidx_l)
        
        #Extract term to words upon dot (.) and dot needs special treatment because we have the case of . or ... and so on
        dot_trm_l, fidx_l  = self.__extract_dot_n_trms(terms_l)
        analysed_terms_l.extend(dot_trm_l)
        fnd_idx_l.extend(fidx_l)
        
        #Remove the already analysed terms after finding dots and commas
        terms_l = [trm for trm in terms_l if terms_l.index(trm) not in fnd_idx_l]
        #Clean-up the index list because items already removed
        fnd_idx_l = []
              
        #Extract the non-alphanumeric symbols ONLY from the Beginning and the End of the terms
        ##except dot (.) and percentage % at the end for the term)
        symb_trm_l, fidx_l  = self.__extract_propr_trms_n_symbs(terms_l)
        analysed_terms_l.extend(symb_trm_l)
        fnd_idx_l.extend(fidx_l)      
        
        #Remove the already analysed terms and put the return a tuple list including the indices of remaining terms list
        terms_l = [(j, trm) for j, trm in enumerate(terms_l) if terms_l.index(trm) not in fnd_idx_l]
        
        #Merge the main terms list with the list of analysed terms
        analysed_terms_l.extend(terms_l)
        
        #Short tuple list by indices i.e. using the fist element of the tuple
        analysed_terms_l.sort()
        
        #Discard indices and keep only the terms list
        analysed_terms_l = [trm[1] for trm in analysed_terms_l]
        
        return analysed_terms_l      
        
        
    def __term_len_limit(self, term_l, limit):
        
        norm_term_l = list()
        
        for term in term_l:
            if len(term) <= limit:
                norm_term_l.append(term)
        return norm_term_l 
        
        
    def __extract_proper_numbers(self, terms_l):
        
        #The proper_numbers list and the list of indices where the proper_number-terms found in the original list    
        num_terms_l = list()
        fnd_idx_l = list()
           
        #Extracting the following Number Formats: 
        #    1)xxxxxx 2)xxxx,xxxx 3)xxxx.xxxx 4)333.333.333...333,xxxxxx 5)333,333,333,333,,,333.xxxxxx
        for i, term in enumerate(terms_l):
            num_terms = self.proper_num.findall(term) # It returns a list of the proper numbers extracted from a raw term
            if num_terms:
                num_terms_l.extend([(j+i, trm) for j, trm in enumerate(num_terms[0]) if trm != ""])
                fnd_idx_l.append(i)
        
        return num_terms_l, fnd_idx_l
    
    
    def __extract_comma_n_trms(self, terms_l):
        
        #The comma list and the list of indices where the comma-terms found in the original list    
        comma_terms_l = list()
        fnd_idx_l = list()
    
        for i, term in enumerate(terms_l):
            #Decompose the terms that in their char set include comma symbol to a list of comma separated terms and the comma(s) 
            decomp_terms = self.comma_decomp.findall(term)
            comma_terms_l.extend([(j+i, trm) for j, trm in enumerate(decomp_terms) if trm != ""])
            if decomp_terms:
                fnd_idx_l.append(i)
        
        return comma_terms_l, fnd_idx_l
    
    
    def __extract_dot_n_trms(self, terms_l):
        
        #The dot list and the list of indices where the dot-terms found in the original list    
        dot_terms_l = list()
        fnd_idx_l = list()

        for i, term in enumerate(terms_l):       
            #Decompose to a dots & terms list and analyse farther for some cases 
            decomp_term = self.dot_decomp.findall(term)
            dtrm_len = len(decomp_term)
            
            if dtrm_len > 1 and dtrm_len <= 3:
                #Here we have the cases of ...CCC or .CC or CC.... or CCC. or CC.CCC or CCCC....CCCC so keep each sub-term
                dot_terms_l.extend([(j+i, trm) for j, trm in enumerate(decomp_term) if trm != ""])
                fnd_idx_l.append(i)
                
            elif dtrm_len > 3: #i.e. Greater than 3
                #Remove the first and the last dot sub-string and let the rest of the term as it was (but the prefix and suffix of dot(s))
                sub_term_l = list()
                
                #Extract dot-sequence prefix if any 
                if self.dot_str.findall(decomp_term[0]):
                    sub_term_l.append( decomp_term.pop(0) )
                    
                #Extract dot-sequence suffix if any
                l_end = len(decomp_term) - 1
                if self.dot_str.findall(decomp_term[l_end]):
                    sub_term_l.append( decomp_term.pop(l_end) )
                    
                #Save the sub-terms of the Decomposed term from the terms list 
                dot_terms_l.append( (i,"".join(decomp_term)) )
                dot_terms_l.extend([(j+i+1, trm) for j, trm in enumerate(sub_term_l) if trm != ""])
                fnd_idx_l.append(i)
                
            else:
                #in case of one element in the list check if it is a dot-sequence
                if self.dot_str.findall(term):     
                    dot_terms_l.extend([(j+i, trm) for j, trm in enumerate(sub_term_l) if trm != ""])
                    fnd_idx_l.append(i)
                     
        return dot_terms_l, fnd_idx_l
        
        
    def __extract_propr_trms_n_symbs(self, terms_l):
        
        #The proper terms and symbols list and the list of indices where the proper-terms&symbols found in the original list    
        symb_terms_l = list()
        fnd_idx_l = list()
        
        for i, term in enumerate(terms_l):
            #Get the symbols
            symb_term_l = self.fredsb_clean.findall(term)
            
            if symb_term_l:
                #Keep the symbols found 
                symb_terms_l.extend([(j+i+1, trm) for j, trm in enumerate(symb_term_l) if trm != ""])
                clean_trm = self.fredsb_clean.sub('', term)
                
                #Keep the terms free of symbols found
                symb_terms_l.append((i+j,clean_trm))
                
                #Keep index symbols found
                fnd_idx_l.append(i)
        
        return symb_terms_l, fnd_idx_l
    
