#
#    Unit Test for html2vect.base.termstypes.words
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

import unittest
from html2vect.base.termstypes.words import String2WordList


class Test_String2WordList__words(unittest.TestCase):
    
    def setUp(self):
        self.str2cng = String2WordList()
        
        self.txt_sample = "This is a unit test for html2vect.termstype.words.String2WordList. package/module in\
                            cases of: proper numbers 2,000.00 proper symbol remove 10% and comma,,, ,comma\
                            dot. after .dot before and ..."
                            
        self.expected_terms_lst = ['This', 'is', 'a', 'unit', 'test', 'for', 'html2vect.termstype.words.String2WordList',\
                                   'package/module', '.', 'in', 'cases', 'of', ':', 'proper', 'numbers', 'proper', 'symbol',\
                                   'remove', '10%', 'and', '2,000.00', 'after', 'before', 'comma', ',', ',,,', 'and', 'comma', 'dot',\
                                   '.', '.', 'dot', '...'] 

    
    def test_terms_lst(self):
        terms_l = self.str2cng.terms_lst( self.txt_sample )
        self.assertEqual(terms_l, self.expected_terms_lst)


suite = unittest.TestSuite()
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_String2WordList__words) )
unittest.TextTestRunner(verbosity=2).run(suite)