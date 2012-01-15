""" Unit Test for regex.py """

import unittest
import regex


class Test_BaseRegexHtmlAttributes(unittest.TestCase):
    
    def setUp(self):
        self.htmlattrib = regex.BaseRegexHtmlAttributes(valid_html=True)
        self.htmlsample = "<html> \
                            <head> \
                            </head> \
                            <body>\
                            <p>This is a unit test for <b>BaseRegexHtmlAttributes</b> class<br/>for htmlattrib.regex module</p>\
                            </body>\
                           </html>"
        self.expected_text = "This is a unit test for BaseRegexHtmlAttributes class for htmlattrib.regex module "
                           
    def test_text(self):
        html_text = self.htmlattrib.text( self.htmlsample )
        self.assertEqual(html_text, self.expected_text)
        
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
suite.addTest( unittest.TestLoader().loadTestsFromTestCase(Test_BaseRegexHtmlAttributes) )
unittest.TextTestRunner(verbosity=2).run(suite)        
    
        