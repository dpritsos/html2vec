#
#    Unit Test for html2vect.base.vectortypes.string2tf
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
#

import unittest
from html2vect.base.vectortypes.string2tf import BaseString2TF
from html2vect.base.termstypes.cngrams import String2CNGramsList
from html2vect.base.termstypes.words import String2WordList
import numpy as np


class Test_Html2LBN(unittest.TestCase):
    
    def setUp(self):
        
        self.bs2tf_3grams = BaseString2TF( termstype=String2CNGramsList(n=3) )
        self.bs2tf_words = BaseString2TF( termstype=String2WordList() )
        
        self.txt_sample = "This is a unit test for html2tfd.charngrams.BaseString2TF class for html2vectors package/module"
        
        self.expected_3grams_freq = {'s i': 1, 't t': 1, 'ase': 1, 's a': 1, 'htm': 2, 'ram': 1, 'rs ': 1, 'TF ': 1, 's f': 1,\
                                     '.ch': 1, 't f': 1, ' un': 1, '2tf': 1, 'l2t': 1, 'l2v': 1, 's p': 1, 'eSt': 1, 'tes': 1,\
                                     'ge/': 1, 'ams': 1, 'or ': 2, 'cha': 1, 'est': 1, 'st ': 1, 'Str': 1, 'for': 2, 'tor': 1,\
                                     ' is': 1, 'ing': 1, 'cla': 1, 'e/m': 1, 'fd.': 1, 'ml2': 2, 'pac': 1, 'arn': 1, 'ngr': 1,\
                                     'r h': 2, '2TF': 1, 'har': 1, 'is ': 2, 'tml': 2, 'F c': 1, 'ass': 1, 'tri': 1, 'g2T': 1,\
                                     'his': 1, 'kag': 1, 'Bas': 1, '2ve': 1, 'tfd': 1, 'gra': 1, 'rng': 1, 'ors': 1, 'it ': 1,\
                                     'odu': 1, 'mod': 1, ' pa': 1, 'ect': 1, 'ule': 1, 'Thi': 1, 's.B': 1, ' te': 1, '.Ba': 1,\
                                     'nit': 1, 'las': 1, ' a ': 1, 'rin': 1, 'seS': 1, 'cka': 1, ' cl': 1, 'd.c': 1, 'dul': 1,\
                                     'ack': 1, 'age': 1, ' ht': 2, 'ms.': 1, '/mo': 1, 'ng2': 1, 'ss ': 1, 'uni': 1, 'cto': 1,\
                                     'vec': 1, ' fo': 2, 'a u': 1}
        
        self.expected_words_freq = {'a': 1, 'for': 2, 'This': 1, 'is': 1, 'html2vectors': 1, 'test': 1, 'package/module': 1,\
                                    'html2tfd.charngrams.BaseString2TF': 1, 'class': 1, 'unit': 1}
        
        
        self.expected_3grams_freq_arr = np.array( [(' a ', 1.0), (' cl', 1.0), (' fo', 2.0), (' ht', 2.0), (' is', 1.0),\
                                                   (' pa', 1.0), (' te', 1.0), (' un', 1.0), ('.Ba', 1.0), ('.ch', 1.0),\
                                                   ('/mo', 1.0), ('2TF', 1.0), ('2tf', 1.0), ('2ve', 1.0), ('Bas', 1.0),\
                                                   ('F c', 1.0), ('Str', 1.0), ('TF ', 1.0), ('Thi', 1.0), ('a u', 1.0),\
                                                   ('ack', 1.0), ('age', 1.0), ('ams', 1.0), ('arn', 1.0), ('ase', 1.0),\
                                                   ('ass', 1.0), ('cha', 1.0), ('cka', 1.0), ('cla', 1.0), ('cto', 1.0),\
                                                   ('d.c', 1.0), ('dul', 1.0), ('e/m', 1.0), ('eSt', 1.0), ('ect', 1.0),\
                                                   ('est', 1.0), ('fd.', 1.0), ('for', 2.0), ('g2T', 1.0), ('ge/', 1.0),\
                                                   ('gra', 1.0), ('har', 1.0), ('his', 1.0), ('htm', 2.0), ('ing', 1.0),\
                                                   ('is ', 2.0), ('it ', 1.0), ('kag', 1.0), ('l2t', 1.0), ('l2v', 1.0),\
                                                   ('las', 1.0), ('ml2', 2.0), ('mod', 1.0), ('ms.', 1.0), ('ng2', 1.0),\
                                                   ('ngr', 1.0), ('nit', 1.0), ('odu', 1.0), ('or ', 2.0), ('ors', 1.0),\
                                                   ('pac', 1.0), ('r h', 2.0), ('ram', 1.0), ('rin', 1.0), ('rng', 1.0),\
                                                   ('rs ', 1.0), ('s a', 1.0), ('s f', 1.0), ('s i', 1.0), ('s p', 1.0),\
                                                   ('s.B', 1.0), ('seS', 1.0), ('ss ', 1.0), ('st ', 1.0), ('t f', 1.0),\
                                                   ('t t', 1.0), ('tes', 1.0), ('tfd', 1.0), ('tml', 2.0), ('tor', 1.0),\
                                                   ('tri', 1.0), ('ule', 1.0), ('uni', 1), ('vec', 1)],\
                                                   dtype=np.dtype([('terms', 'S128'), ('freq', 'float32')]))
        
        self.expected_words_freq_arr = np.array( [('This', 1.0), ('a', 1.0), ('class', 1.0), ('for', 2.0),\
                                                  ('html2tfd.charngrams.BaseString2TF', 1.0), ('html2vectors', 1.0),\
                                                  ('is', 1.0), ('package/module', 1.0), ('test', 1.0), ('unit', 1.0)],\
                                                  dtype=np.dtype([('terms', 'S128'), ('freq', 'float32')]))                                          
                           
                           
    def test_tf_dict_3grams(self):
        ngrams_freq_dict = self.bs2tf_3grams.tf_dict( self.txt_sample )
        self.assertEqual(ngrams_freq_dict, self.expected_3grams_freq)    
    
    
    def test_tf_array_3grams(self):
        ngrams_freq_arr = self.bs2tf_3grams.tf_narray( self.txt_sample ) 
        for val, exp_val in zip(ngrams_freq_arr, self.expected_3grams_freq_arr):
            self.assertEqual(val, exp_val)
        
            
    def test_tf_dict_words(self):
        word_freq_dict = self.bs2tf_words.tf_dict( self.txt_sample )
        self.assertEqual(word_freq_dict, self.expected_words_freq)    
    
    
    def test_tf_array_words(self):
        word_freq_arr = self.bs2tf_words.tf_narray( self.txt_sample )
        for val, exp_val in zip(word_freq_arr, self.expected_words_freq_arr):
            self.assertEqual(val, exp_val)
        
        
suite = unittest.TestSuite()
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_BaseString2TF) )
unittest.TextTestRunner(verbosity=2).run(suite)        
