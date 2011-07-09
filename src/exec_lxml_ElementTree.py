
""" """
#import StringIO
import xml.etree.ElementTree 
import re
import lxml.html.clean 
import lxml.etree
from filehandlers import basefilehandlers as bfs

bpfh = bfs.BasePathFileHandler()
bfh = bfs.BaseFileHandler()


   
#genres = [ "blog", "eshop", "faq", "frontpage", "listing", "php", "spage"] 
#base_filepath = "/home/dimitrios/Synergy-Crawler/Santini_corpus_html2txt/"
#htmls_path = "/html/"
#text_path = "/txt_Htmlremover_app/"

genres = [ "html/" ] 
htmls_path = ""
base_filepath = "/home/dimitrios/Synergy-Crawler/Golden_Standared_from_Santinis_corpus/"
text_path = "/lxml_elementtree_text/"

find_text = lxml.etree.XPath("//text()")
cleaner = lxml.html.clean.Cleaner(scripts=True,\
                                  javascript=True,\
                                  comments=True,\
                                  style=True,\
                                  links=True,\
                                  meta=True,\
                                  page_structure=True,\
                                  processing_instructions=True,\
                                  embedded=True,\
                                  frames=False,\
                                  forms=False,\
                                  annoying_tags=True,\
                                  remove_unknown_tags=True )
parser = lxml.etree.HTMLParser()
whitespace_chars = re.compile(r'[\s]+', re.UNICODE)

for g in genres:
    fn_ftxt_l = bfh.load_frmpaths(base_filepath, g, encoding='utf-8', error_handling='replace')
    fn_ftxt_l = [ [fn.replace('/html/', text_path),\
                whitespace_chars.sub(' ', " ".join( find_text( lxml.etree.fromstring( cleaner.clean_html(ftxt), parser)) ))\
                   ] for fn, ftxt in fn_ftxt_l ]
    fn_ftxt_l = [ [fn.replace('.html', '.html.txt'), ftxt] for fn, ftxt in fn_ftxt_l ]
    print fn_ftxt_l[0]
    bfh.save_files(None, fn_ftxt_l, encoding='utf-8', error_handling='strict')
        
        
    
   
