#
#    Module: cngrams - Character NGrams
#
#    Author: Dimitrios Pritsos
#
#    License: GPL Style
#
#    Last update: Please refer to the GIT tracking
#

""" html2vect.base.termstypes.posgrams: submodule of `html2vect` module defines
    the class String2POSGramsList """

# #########################################################################################
# ##### NOTE: This is a quick-and-dirty solution for accelarating my experiments...  ######
# ##### ...since NLTK new stanford-Tagger wraper is using the "stream like" tagger...######
# ##### ...server, implamented in Java, I can do that directly and not by using nltk.######
# #########################################################################################

from .wngrams import String2TokenList
from nltk.tag.stanford import StanforPOSTagger


class String2WNGramsList(String2TokenList):

    def __init__(self, tagger_cls='english-bidirectional-distsim.tagger'):

        super(String2WNGramsList, self).__init__(*args, **kwrgs)

        self.tagger_cls = tagger_cls

    @property
    def N(self):
        return self.n

    @N.setter
    def N(self, value):
        self.tagger_cls = value

    def terms_lst(self, text):

        # Getting the Analysed list of tokens.
        analyzed_terms_lst = self.token_lst(text, self.terms_size_reject)

        # Getting the Stanford tagger instance.
        spt = StanforPOSTagger(self.tagger_cls)

        # Tagging the Analyzed terms list and getting the tags list as terms.
        pos_tags = [pos for t, pos in spt.tag(analyzed_terms_lst)]

        return pos_tags
