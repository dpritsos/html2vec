#
#    Unit Test for html2vect.termstypes.words
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

import unittest
from html2vect.termstypes.words import String2WordList


class Test_String2WordList__words(unittest.TestCase):
    
    def setUp(self):
        self.str2cng = String2WordList()
        self.txt_sample = "This is a unit test for html2vect.termstype.words.String2WordList. package/module in cases of: proper numbers 2,000.00 proper symbol remove 10% and comma,,, ,comma dot. after .dot before"
        self.expected_terms_lst = ['2,000.00', 'comma', ',,,', ',', 'comma', '.', 'html2vect.termstype.words.String2WordList',\
                                   'dot', '.', '.', 'dot', ':', 'of', 'This', 'is', 'a', 'unit', 'test', 'for', 'package/module',\
                                   'in', 'cases', 'proper', 'numbers', 'proper', 'symbol', 'remove', '10%', 'and', 'after', 'before']   
    
    def test_terms_lst(self):
        terms_l = self.str2cng.terms_lst( self.txt_sample )
        self.assertEqual(terms_l, self.expected_terms_lst)


suite = unittest.TestSuite()
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_String2WordList__words) )
unittest.TextTestRunner(verbosity=2).run(suite)