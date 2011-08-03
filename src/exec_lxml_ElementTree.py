
""" """
#import StringIO
import xml.etree.ElementTree 
import re
import lxml.html.clean 
import lxml.etree
from filehandlers import basefilehandlers as bfs

bpfh = bfs.BasePathFileHandler()
bfh = bfs.BaseFileHandler()


   
#genres = [ "blog/html/", "eshop/html/", "faq/html/", "frontpage/html/", "listing/html/", "php/html/", "spage/html/"] 
#base_filepath = "/home/dimitrios/Synergy-Crawler/Santini_corpus_html2txt/"
#genres = [ "blog_pgs/html/", "news_pgs/html/", "product_pgs/html/", "forum_pgs/html/", "wiki_pgs/html/" ]
genres = [ "blog_pgs/html_500/", "news_pgs/html_500/", "product_pgs/html_500/", "forum_pgs/html_500/", "wiki_pgs/html_500/" ] 
base_filepath = "/home/dimitrios/Synergy-Crawler/Crawled_corpus_3000/"
#genres = [ "html/" ] 
#base_filepath = "/home/dimitrios/Synergy-Crawler/Golden_Standared_from_Santinis_corpus/"
#text_path = "/lxml_elementtree_text/"
text_path = "/lxml_elementtree_text_500/"

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
    fn_ftxt_l = [ [fn.replace('/html_500/', text_path),\
                whitespace_chars.sub(' ', " ".join( find_text( lxml.etree.fromstring( cleaner.clean_html(ftxt.encode()), parser)) ))\
                   ] for fn, ftxt in fn_ftxt_l ]
    fn_ftxt_l = [ [fn.replace('.htm', '.html.txt'), ftxt.decode()] for fn, ftxt in fn_ftxt_l ]
    print fn_ftxt_l[0]
    bfh.save_files(None, fn_ftxt_l, encoding='utf-8', error_handling='strict')
        
        
    
   
