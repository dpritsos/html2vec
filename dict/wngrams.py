#
#    Module: Words - from html row text/files to native python character Words TF dictionaries
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2vect.dict.wngrams: submodule of `html2vect` module defines the classes: HtmlTF(), HtmlTPL()"""

from cngrams import Html2TF as CHtml2TF
from ..base.termstypes.wngrams import String2WNGramsList



class Html2TF(CHtml2TF):
    
    #Define the TermsType to be produced from this class 
    s2ngl = String2WNGramsList()
    
    
    def __init__(self, *args, **kwrgs):
            
        #Initialise BaseHtml2TF Class   
        super(Html2TF, self).__init__(*args, **kwrgs)
              
        

#Deleted from the previous version now is need to be re-written    
class Html2TPL(object):
    
    def __init__(self):
        pass