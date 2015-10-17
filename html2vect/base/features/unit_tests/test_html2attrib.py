#
#    Unit Test for html2vect.base.features.html2attrib
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
#

import unittest
from html2vect.base.features.html2attrib import BaseHTML2Attributes


class Test_BaseHTML2Attributes(unittest.TestCase):
    
    def setUp(self):
        self.html2attrib = BaseHTML2Attributes(valid_html=False)
        self.html2attrib_valid = BaseHTML2Attributes(valid_html=True)
        self.htmlsample = "<html> \
                            <head> \
                            </head> \
                            <body>\
                            <p>This is a unit test for <b>BaseRegexHtmlAttributes</b> class<br/>for htmlattrib.regex module</p>\
                            </body>\
                           </html>\
                           <p> Not Valid"
        self.expected_text = "This is a unit test for BaseRegexHtmlAttributes class for htmlattrib.regex module Not Valid"
        self.expected_text_valid = "This is a unit test for BaseRegexHtmlAttributes class for htmlattrib.regex module "
    
    def test_text(self):
        html_text = self.html2attrib.text( self.htmlsample )
        self.assertEqual(html_text, self.expected_text)                       
    
    def test_text_valid(self):
        html_text = self.html2attrib_valid.text( self.htmlsample )
        self.assertEqual(html_text, self.expected_text_valid)
        
    #@unittest.skip("htmlattrib.regex.BaseRegexHtmlAttributes.tags() skip test") NOT WORKING IN python2.6    
    #def test_tags(self):
    #    self.fail("htmlattrib.regex.BaseRegexHtmlAttributes.tags() test shouldn't happen. Not yet tags() function implemented")
    
    #@unittest.skip("htmlattrib.regex.BaseRegexHtmlAttributes.scripts() skip test")    
    #def test_scripts(self):
    #    self.fail("htmlattrib.regex.BaseRegexHtmlAttributes.scripts() test shouldn't happen. Not yet scripts() function implemented")
        
    #@unittest.skip("htmlattrib.regex.BaseRegexHtmlAttributes.styles() skip test")    
    #def test_styles(self):
    #    self.fail("htmlattrib.regex.BaseRegexHtmlAttributes.styles() test shouldn't happen. Not yet styles() function implemented")

suite = unittest.TestSuite()
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_BaseHTML2Attributes) )
unittest.TextTestRunner(verbosity=2).run(suite)        
    
        