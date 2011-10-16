
""" """

import htmlattrib.regex

h2t = htmlattrib.regex.HtmlText() 
   
#genres = [ "blog/html/", "eshop/html/", "faq/html/", "frontpage/html/", "listing/html/", "php/html/", "spage/html/"] 
#base_filepath = "/home/dimitrios/Synergy-Crawler/Santini_corpus_html2txt/"
#genres = [ "blog_pgs/html_500/", "news_pgs/html_500/", "product_pgs/html_500/", "forum_pgs/html_500/", "wiki_pgs/html_500/" ] 
#base_filepath = "/home/dimitrios/Synergy-Crawler/Crawled_corpus_3000/"
base_filepath = "/home/dimitrios/Synergy-Crawler/Crawled_corpus_500/"
genres = [ "blog_pgs/html/", "news_pgs/html/", "product_pgs/html/", "forum_pgs/html/", "wiki_pgs/html/" ] 
#base_filepath = "/home/dimitrios/Synergy-Crawler/Manually_Selected_Crawled_corpus_75/"



###base_filepath = "/home/dimitrios/Synergy-Crawler/Golden_Standared_from_Santinis_corpus/"
##genres = ["gold_standard_text/"]
##text_path = "/gold_standard_text_2/"



#genres = [ "html/" ] 
#base_filepath = "/home/dimitrios/Synergy-Crawler/Golden_Standared_from_Santinis_corpus/"
text_path = "/txt_html2vectors_mod/"



##text_path = "/txt_html2vectors_mod/"

for g in genres:
    fn_ftxt_l = h2t.from_paths(base_filepath, g, encoding='utf-8', error_handling='replace', low_mem=False)
    #fn_ftxt_l = [ [fn.replace('/gold_standared_text/', text_path), ftxt] for fn, ftxt in fn_ftxt_l ]
    fn_ftxt_l = [ [fn.replace('/html/', text_path), ftxt] for fn, ftxt in fn_ftxt_l ]
    fn_ftxt_l = [ [fn.replace('.html', '.html.txt'), ftxt] for fn, ftxt in fn_ftxt_l ]
    h2t.save_files(None, fn_ftxt_l, encoding='utf-8', error_handling='strict')
   
