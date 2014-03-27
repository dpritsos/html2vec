#
#    Unit Test for html2vect.base.termstypes.cngrams
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

import sys
sys.path.append('../../../../')

import unittest
from html2vect.base.termstypes.cngrams import String2CNGramsList


class Test_String2CNGramsList__3grams(unittest.TestCase):
    
    def setUp(self):
        self.str2cng = String2CNGramsList(n=3)
        self.txt_sample = "This is a unit test for html2tfd.charngrams.BaseString2TF class for html2vectors package/module"
        self.expected_terms_lst = ['Thi', 'his', 'is ', 's i', ' is', 'is ', 's a', ' a ', 'a u', ' un', 'uni', 'nit', 'it ', 't t',\
                                   ' te', 'tes', 'est', 'st ', 't f', ' fo', 'for', 'or ', 'r h', ' ht', 'htm', 'tml', 'ml2', 'l2t',\
                                   '2tf', 'tfd', 'fd.', 'd.c', '.ch', 'cha', 'har', 'arn', 'rng', 'ngr', 'gra', 'ram', 'ams', 'ms.',\
                                   's.B', '.Ba', 'Bas', 'ase', 'seS', 'eSt', 'Str', 'tri', 'rin', 'ing', 'ng2', 'g2T', '2TF', 'TF ',\
                                   'F c', ' cl', 'cla', 'las', 'ass', 'ss ', 's f', ' fo', 'for', 'or ', 'r h', ' ht', 'htm', 'tml',\
                                   'ml2', 'l2v', '2ve', 'vec', 'ect', 'cto', 'tor', 'ors', 'rs ', 's p', ' pa', 'pac', 'ack', 'cka',\
                                   'kag', 'age', 'ge/', 'e/m', '/mo', 'mod', 'odu', 'dul', 'ule']
    
    
    def test_terms_lst(self):
        terms_l = self.str2cng.terms_lst( self.txt_sample )
        self.assertEqual(terms_l, self.expected_terms_lst)
        

suite = unittest.TestSuite()
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_String2CNGramsList__3grams) )
unittest.TextTestRunner(verbosity=2).run(suite)        
    