#
#    Unit Test for html2vect.base.termstypes.words
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
from html2vect.base.termstypes.wngrams import String2WNGramsList


class Test_String2WNGramsList__words(unittest.TestCase):
    
    def setUp(self):
        self.str2wng = String2WNGramsList(n=1)
        
        self.txt_sample = "This is a unit test for html2vect.termstype.words.String2WNGramsList. package/module in\
                            cases of: proper numbers 2,000.00 proper symbol remove 10% and comma,,, ,comma\
                            dot. after .dot before and ..."
        
      
                            
        self.expected_terms_lst = ['This', 'is', 'a', 'unit', 'test', 'for', 'html2vect.termstype.words.String2WNGramsList',\
                                   'package/module', '.', 'in', 'cases', 'of', ':', 'proper', 'numbers', 'proper', 'symbol',\
                                   'remove', '10%', 'and', '2,000.00', 'after', 'before', 'comma', ',', ',,,', 'and', 'comma', 'dot',\
                                   '.', '.', 'dot', '...'] 
    
    def test_terms_lst(self):
        terms_l = self.str2wng.terms_lst( self.txt_sample )
        print terms_l
        self.assertEqual(terms_l, self.expected_terms_lst)


class Test_String2WNGramsList__wngrams(unittest.TestCase):
    
    def setUp(self):
        self.str2wng = String2WNGramsList(n=3)
        
        self.txt_sample = "This is a unit test for html2vect.termstype.words.String2WNGramsList. package/module in\
                            cases of: proper numbers 2,000.00 proper symbol remove 10% and comma,,, ,comma\
                            dot. after .dot before and ..."
                            
        self.expected_terms_lst = ['This is a', 'is a unit', 'a unit test', 'unit test for',\
                                   'test for html2vect.termstype.words.String2WNGramsList',\
                                   'for html2vect.termstype.words.String2WNGramsList package/module',\
                                   'html2vect.termstype.words.String2WNGramsList package/module .',\
                                   'package/module . in', '. in cases', 'in cases of', 'cases of :', 'of : proper',\
                                   ': proper numbers', 'proper numbers proper', 'numbers proper symbol',\
                                   'proper symbol remove', 'symbol remove 10%', 'remove 10% and', '10% and 2,000.00',\
                                   'and 2,000.00 after', '2,000.00 after before', 'after before comma', 'before comma ,',\
                                   'comma , ,,,', ', ,,, and', ',,, and comma', 'and comma dot', 'comma dot .', 'dot . .',\
                                   '. . dot', '. dot ...'] 

    
    def test_terms_lst(self):
        terms_l = self.str2wng.terms_lst( self.txt_sample )
        self.assertEqual(terms_l, self.expected_terms_lst)


suite = unittest.TestSuite()
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_String2WNGramsList__words) )
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_String2WNGramsList__wngrams) )
unittest.TextTestRunner(verbosity=2).run(suite)