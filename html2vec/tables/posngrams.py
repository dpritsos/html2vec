#
#    Module: Words N-Grams - from html row text/files to PyTables EArrays Words N-Grams Earrays
#
#    Author: Dimitiros Pritsos
#
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking
#

""" html2vect.tables.posgrams: submodule of `html2vect` module defines the classes: Html2TF() """

from .cngrams import Html2TF as CHtml2TF
from ..base.termstypes.posngrams import String2POSNGramsList


class Html2TF(CHtml2TF):

    # Define the TermsType to be produced from this class
    s2ngl = String2POSNGramsList()

    def __init__(self, *args, **kwrgs):

        # Setting the requested Tagger Class will be used by the Stanford tagger.
        if len(args):

            # Setting the class property
            self.s2ngl.Tagger_cls = args[0]

            # Initialise BaseHtml2TF Class.
            super(Html2TF, self).__init__(*args[1::], **kwrgs)

        else:

            # Setting the class property.
            self.s2ngl.Tagger_cls = kwrgs['tagger_cls']

            # Removing the keyword form dictionary and passing the rest keword arguments to the...
            # ...parent class.
            kwrgs.pop('tagger_cls', None)

            # Initialise BaseHtml2TF Class.
            super(Html2TF, self).__init__(*args, **kwrgs)
