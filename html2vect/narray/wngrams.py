#
#    Module: Words-TF - from html row text/files to scipy.sparse.csr_matrix Words-TF
#
#    Author: Dimitiros Pritsos
#
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking
#

""" html2vect.sparse.wngrams: submodule of `html2vect` module defines the classes: Html2TF() """

from .cngrams import Html2TF as CHtml2TF
from ..base.termstypes.wngrams import String2WNGramsList


class Html2TF(CHtml2TF):

    # Define the TermsType to be produced from this class.
    s2ngl = String2WNGramsList()

    def __init__(self, *args, **kwrgs):

        # Initialise BaseHtml2TF Class.
        super(Html2TF, self).__init__(*args, **kwrgs)


# To Be Written
class Html2TPL(object):

    def __init__(self):
        pass
