#
#     Module: Words N-Grams - Natural Language Dictionary Words as Terms Types
#
#     Author: Dimitrios Pritsos
#
#     License: BSD Style
#
#     Last update: Please refer to the GIT tracking
#

""" html2vect.base.termstypes.cngrams: submodule of `html2vect` module defines the class String2WNGramsList """

import re


class String2TokenList(object):

    def __init__(self):

        # Whitespace characters [<space>\t\n\r\f\v] matching, for splitting the raw text to terms
        self.white_spliter = re.compile(r'[\s]+', re.UNICODE)

        # Find URL String. Probably anchor text
        self.url_str = re.compile(
            r'(((ftp://|FTP://|http://|HTTP://|https://|HTTPS://)?(www|[^\s()<>.?]+))?([.]?[^\s()<>.?]+)+?(?=.org|.edu|.tv|.com|.gr|.gov|.uk)(.org|.edu|.tv|.com|.gr|.gov|.uk){1}([/]\S+)*[/]?)',
            re.UNICODE|re.IGNORECASE
        )

        #  Comma decomposer
        self.comma_decomp = re.compile(r'[^,]+(?=,)|(?<=,)[^,]+|[,]+', re.UNICODE|re.IGNORECASE)

        # Find dot or sequence of dots
        self.dot_str = re.compile(r'[.]+', re.UNICODE)
        self.dot_decomp = re.compile(r'[^.]+(?=\.)|(?<=\.)[^.]+|[.]+', re.UNICODE)

        # Symbol term decomposer
        self.fredsb_clean = re.compile(r'(^[\W])([\w]+?)|([\w]+?)([^\w%]$)', re.UNICODE)
        # front-end-symbol-cleaning => fredsb_clean

        # Find proper number
        self.proper_num = re.compile(
            r'(^[0-9]+$)|(^[0-9]+[,][0-9]+$)|(^[0-9]+[.][0-9]+$)|(^[0-9]{1,3}(?:[.][0-9]{3})+[,][0-9]+$)|(^[0-9]{1,3}(?:[,][0-9]{3})+[.][0-9]+$)',
            re.UNICODE
        )

    def token_lst(self, text, terms_size_reject=256):

        # In case not text is given it returns None. The outer code layer should handle this...
        # ...if caused due to error.
        if not text:
            return None

        # Initially split the text to terms separated by white-spaces [\t\n\r\f\v].
        token_l = self.white_spliter.split(text)

        # Any term has more than self.terms_size_reject (default 512 chars) characters is rejected.
        token_l = self.__term_len_limit(token_l, terms_size_reject)

        # Extract the Numbers form the token_l.
        token_l = self.__extract_proper_numbers(token_l)

        # Extract the terms to sub-terms of any symbol but comma (,) and comma sub-term(s).
        token_l = self.__extract_comma_n_trms(token_l)

        # Extract term to words upon dot (.) and dot needs special treatment because we have...
        # ...the case of . or ... and so on.
        token_l = self.__extract_dot_n_trms(token_l)

        # Extract the non-alphanumeric symbols ONLY from the Beginning and the End of the terms
        # # except dot (.) and percentage % at the end for the term)
        token_l = self.__extract_propr_trms_n_symbs(token_l)

        # Creating the analyzed terms list by puting the analyzed and non-analyzed terms in...
        # ...a single list.
        analyzed_token_lst = list()
        for trm in token_l:
            if isinstance(trm, list):
                analyzed_token_lst.extend(trm)
            else:
                analyzed_token_lst.append(trm)

        # Removing any empty string (if any).
        analyzed_token_lst = [trm for trm in analyzed_token_lst if trm != '']

        return analyzed_token_lst

    def __term_len_limit(self, term_l, limit):

        norm_term_l = list()

        for term in term_l:
            if len(term) <= limit:
                norm_term_l.append(term)

        return norm_term_l

    def __extract_proper_numbers(self, terms_l):

        # Extracting the following Number Formats:...
        # ...1)xxxxxx 2)xxxx,xxxx 3)xxxx.xxxx 4)333.333.333...333,xxxxxx ...
        # ... 5)333,333,333,333,,,333.xxxxxx
        for i, term in enumerate(terms_l):

            if isinstance(term, str):

                # It returns a list of the proper numbers extracted from a raw term
                num_terms = self.proper_num.findall(term)
                if num_terms:
                    terms_l[i] = [trm for trm in num_terms[0] if trm != '']

        return terms_l

    def __extract_comma_n_trms(self, terms_l):

        for i, term in enumerate(terms_l):

            if isinstance(term, str):

                # Decompose the terms that in their char set include comma symbol to a list...
                # ...of comma separated terms and the comma(s)
                decomp_terms = self.comma_decomp.findall(term)
                if decomp_terms:
                    terms_l[i] = [trm for trm in decomp_terms if trm != '']

        return terms_l

    def __extract_dot_n_trms(self, terms_l):

        for i, term in enumerate(terms_l):

            if isinstance(term, str):

                # Decompose to a dots & terms list and analyse farther for some cases.
                decomp_term = self.dot_decomp.findall(term)
                dtrm_len = len(decomp_term)

                if dtrm_len > 1 and dtrm_len <= 3:
                    # Here we have the cases of ...CCC or .CC or CC.... or CCC. or CC.CCC ...
                    # ... or CCCC....CCCC so keep each sub-term.
                    terms_l[i] = [trm for trm in decomp_term if trm != '']

                elif dtrm_len > 3:  # i.e. Greater than 3
                    # Remove the first and the last dot sub-string and let the rest of the term...
                    # ... as it was (but the prefix and suffix of dot(s)).
                    sub_term_l = list()

                    # Extract dot-sequence prefix if any.
                    if self.dot_str.findall(decomp_term[0]):
                        sub_term_l.append(decomp_term.pop(0))

                    # Extract dot-sequence suffix if any.
                    l_end = len(decomp_term) - 1
                    if self.dot_str.findall(decomp_term[l_end]):
                        sub_term_l.append(decomp_term.pop(l_end))

                    # Save the sub-terms of the Decomposed term from the terms list.
                    terms_l[i] = ["".join(decomp_term)]
                    terms_l[i].extend([trm for trm in sub_term_l if trm != ''])

                else:
                    # in case of one element in the list check if it is a dot-sequence
                    if self.dot_str.findall(term):
                        terms_l[i] = [trm for trm in decomp_term if trm != '']

        return terms_l

    def __extract_propr_trms_n_symbs(self, terms_l):

        for i, term in enumerate(terms_l):

            if isinstance(term, str):

                # Get the symbols
                symb_term_l = self.fredsb_clean.findall(term)

                if symb_term_l:
                    # Keep the preceding and ascending symbols separately to the rest of the term.
                    terms_l[i] = [trm for trm in symb_term_l[0] if trm != '']

        return terms_l


class String2WNGramsList(String2TokenList):

    def __init__(self, n=1, terms_size_reject=512):

        super(String2WNGramsList, self).__init__()

        # N-Grams size
        self.n = n

        # Term Size Reject
        self.terms_size_reject = terms_size_reject

    @property
    def N(self):
        return self.n

    @N.setter
    def N(self, value):
        self.n = value

    def terms_lst(self, text):

        # Getting the Analysed list of tokens.
        analyzed_terms_lst = self.token_lst(text, self.terms_size_reject)

        # Constructing the Words N-Grams List
        analyzed_terms_lst = [
            " ".join(analyzed_terms_lst[i: i+self.n])
            for i in range(len(analyzed_terms_lst) - self.n + 1)
        ]

        return analyzed_terms_lst
