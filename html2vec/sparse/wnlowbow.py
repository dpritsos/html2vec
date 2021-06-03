#
#    Module: LowBOW (Local Weighted Bag of Words) - from html row text/files to scipy.sparse.csr_matrix LowBOW
#
#    Author: Dimitiros Pritsos
#
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking
#

""" html2vect.sparse.lowbow: submodule of `html2vect` module defines the classes: Html2LBN(), Html2LBW()"""

from .cnlowbow import CHtml2TLoW
from ..base.termstypes.words import String2WNGramsList

import scipy.sparse as ssp
import numpy as np
from scipy import stats
import string


class Html2TLoW(CHtml2TLoW):

    #Define the TermsType to be produced from this class
    s2ngl = String2WNGramsList()

    def __init__(self, *args, **kwrgs):

        #Initialise CHtml2TLoW Class
        super(Html2TLoW, self).__init__(*args, **kwrgs)
