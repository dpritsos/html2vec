""" """

import os
from filehandlers import basefilehandlers as bfs

bfh = bfs.BasePathFileHandler()

   
#genres = [ "blog", "eshop", "faq", "frontpage", "listing", "php", "spage"] 
#base_filepath = "/home/dimitrios/Synergy-Crawler/Santini_corpus_html2txt/"
#htmls_path = "/html/"
#text_path = "/txt_Htmlremover_app/"

genres = [ "" ] 
htmls_path = "html/"
base_filepath = "/home/dimitrios/Synergy-Crawler/Golden_Standared_from_Santinis_corpus/"
text_path = "html2text_debian_text/"

for g in genres:
    file_lst = bfh.file_list_frmpaths(base_filepath, g + htmls_path)
    file_lst = [ fname.split('/')[-1] for fname in file_lst ]
    for html_f in file_lst:
        print base_filepath + g + htmls_path + html_f 
        os.spawnlp(os.P_WAIT, 'html2text',\
                   'html2text',\
                   #"-style", "compact",\ #It is default option
                   #"-utf8",\ #It is applied because of eclipse utf8 environment  
                   '-nometa',\
                   '-o', base_filepath + g + text_path + html_f + '.txt',\
                   base_filepath + g + htmls_path + html_f )





