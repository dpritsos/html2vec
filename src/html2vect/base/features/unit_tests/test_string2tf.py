#
#    Unit Test html2vect.base.features.  
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

import unittest
import html2vect.dict.cngrams as cngrams
from html2vect.string.attrib_text import HtmlFullText 
import pickle

class Test_BaseString2NgramList__3grams(unittest.TestCase):
    
    def setUp(self):
        self.bs2tl = cngrams.BaseString2NgramList(n=3)
        self.txt_sample = "This is a unit test for html2tfd.charngrams.BaseString2TF class for html2vectors package/module"
        self.expected_terms_lst = ['Thi', 'his', 'is ', 's i', ' is', 'is ', 's a', ' a ', 'a u', ' un', 'uni', 'nit', 'it ', 't t',\
                                   ' te', 'tes', 'est', 'st ', 't f', ' fo', 'for', 'or ', 'r h', ' ht', 'htm', 'tml', 'ml2', 'l2t',\
                                   '2tf', 'tfd', 'fd.', 'd.c', '.ch', 'cha', 'har', 'arn', 'rng', 'ngr', 'gra', 'ram', 'ams', 'ms.',\
                                   's.B', '.Ba', 'Bas', 'ase', 'seS', 'eSt', 'Str', 'tri', 'rin', 'ing', 'ng2', 'g2T', '2TF', 'TF ',\
                                   'F c', ' cl', 'cla', 'las', 'ass', 'ss ', 's f', ' fo', 'for', 'or ', 'r h', ' ht', 'htm', 'tml',\
                                   'ml2', 'l2v', '2ve', 'vec', 'ect', 'cto', 'tor', 'ors', 'rs ', 's p', ' pa', 'pac', 'ack', 'cka',\
                                   'kag', 'age', 'ge/', 'e/m', '/mo', 'mod', 'odu', 'dul', 'ule']
    
    def test_terms_lst(self):
        terms_l = self.bs2tl.terms_lst( self.txt_sample )
        self.assertEqual(terms_l, self.expected_terms_lst)


class Test_BaseString2TFTP__3grams(unittest.TestCase):
    
    def setUp(self):
        self.bs2tf = cngrams.BaseString2TFTP(n=3)
        self.txt_sample = "This is a unit test for html2tfd.charngrams.BaseString2TF class for html2vectors package/module"
        self.expected_ngrams_freq = {'s i': 1, 't t': 1, 'ase': 1, 's a': 1, 'htm': 2, 'ram': 1, 'rs ': 1, 'TF ': 1, 's f': 1,\
                                     '.ch': 1, 't f': 1, ' un': 1, '2tf': 1, 'l2t': 1, 'l2v': 1, 's p': 1, 'eSt': 1, 'tes': 1,\
                                     'ge/': 1, 'ams': 1, 'or ': 2, 'cha': 1, 'est': 1, 'st ': 1, 'Str': 1, 'for': 2, 'tor': 1,\
                                     ' is': 1, 'ing': 1, 'cla': 1, 'e/m': 1, 'fd.': 1, 'ml2': 2, 'pac': 1, 'arn': 1, 'ngr': 1,\
                                     'r h': 2, '2TF': 1, 'har': 1, 'is ': 2, 'tml': 2, 'F c': 1, 'ass': 1, 'tri': 1, 'g2T': 1,\
                                     'his': 1, 'kag': 1, 'Bas': 1, '2ve': 1, 'tfd': 1, 'gra': 1, 'rng': 1, 'ors': 1, 'it ': 1,\
                                     'odu': 1, 'mod': 1, ' pa': 1, 'ect': 1, 'ule': 1, 'Thi': 1, 's.B': 1, ' te': 1, '.Ba': 1,\
                                     'nit': 1, 'las': 1, ' a ': 1, 'rin': 1, 'seS': 1, 'cka': 1, ' cl': 1, 'd.c': 1, 'dul': 1,\
                                     'ack': 1, 'age': 1, ' ht': 2, 'ms.': 1, '/mo': 1, 'ng2': 1, 'ss ': 1, 'uni': 1, 'cto': 1,\
                                     'vec': 1, ' fo': 2, 'a u': 1}
        self.expected_ngrams_pos = {'s i': [3], 't t': [13], 'ase': [45], 's a': [6], 'htm': [24, 68], 'ram': [39], 'rs ': [78],\
                                    'TF ': [55], 's f': [62], '.ch': [32], 't f': [18], ' un': [9], '2tf': [28], 'l2t': [27],\
                                    'l2v': [71], 's p': [79], 'eSt': [47], 'tes': [15], 'ge/': [86], 'ams': [40], 'or ': [21, 65],\
                                    'cha': [33], 'est': [16], 'st ': [17], 'Str': [48], 'for': [20, 64], 'tor': [76], ' is': [4],\
                                    'ing': [51], 'cla': [58], 'e/m': [87], 'fd.': [30], 'ml2': [26, 70], 'pac': [81], 'arn': [35],\
                                    'ngr': [37], 'r h': [22, 66], '2TF': [54], 'har': [34], 'is ': [2, 5], 'tml': [25, 69], 'F c': [56],\
                                    'ass': [60], 'tri': [49], 'g2T': [53], 'his': [1], 'kag': [84], 'Bas': [44], '2ve': [72], 'tfd': [29],\
                                    'gra': [38], 'rng': [36], 'ors': [77], 'it ': [12], 'odu': [90], 'mod': [89], ' pa': [80], 'ect': [74],\
                                    'ule': [92], 'Thi': [0], 's.B': [42], ' te': [14], '.Ba': [43], 'nit': [11], 'las': [59], ' a ': [7],\
                                    'rin': [50], 'seS': [46], 'cka': [83], ' cl': [57], 'd.c': [31], 'dul': [91], 'ack': [82], 'age': [85],\
                                    ' ht': [23, 67], 'ms.': [41], '/mo': [88], 'ng2': [52], 'ss ': [61], 'uni': [10], 'cto': [75], 'vec': [73],\
                                    ' fo': [19, 63], 'a u': [8]}
                           
    def test_basestring2tf_nf_dict(self):
        ngrams_freq = self.bs2tf.nf_dict( self.txt_sample )
        self.assertEqual(ngrams_freq, self.expected_ngrams_freq)
        
    def test_basestring2tf_npos_dict(self):
        ngrams_pos = self.bs2tf.npos_dict( self.txt_sample )
        self.assertEqual(ngrams_pos, self.expected_ngrams_pos)