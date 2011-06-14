
""" """

import htmattrib.regex

h2t = htmattrib.regex.HtmlText() 
   
genres = [ "blog/html/", "eshop/html/", "faq/html/", "frontpage/html/", "listing/html/", "php/html/", "spage/html/"] 
base_filepath = "/home/dimitrios/Synergy-Crawler/Santini_corpus_html2txt/"
text_path = "/txt_html2vectors_mod/"

for g in genres:
    fn_ftxt_l = h2t.from_paths(base_filepath, g, encoding='utf-8', error_handling='replace', low_mem=False)
    fn_ftxt_l = [ [fn.replace('/html/', text_path), ftxt] for fn, ftxt in fn_ftxt_l ]
    fn_ftxt_l = [ [fn.replace('.htm', '.htm.txt'), ftxt] for fn, ftxt in fn_ftxt_l ]
    h2t.save_files(None, fn_ftxt_l, encoding='utf-8', error_handling='strict')
   
