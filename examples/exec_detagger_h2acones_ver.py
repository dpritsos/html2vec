""" """

import os
from filehandlers import basefilehandlers as bfs

bfile_hdlr = bfs.BasePathFileHandler()

   
#genres = [ "blog", "eshop", "faq", "frontpage", "listing", "php", "spage"] 
#base_filepath = "/home/dimitrios/Synergy-Crawler/Santini_corpus_html2txt/"
genres = [ "blog_pgs", "news_pgs", "product_pgs", "forum_pgs", "wiki_pgs" ] 
#base_filepath = "/home/dimitrios/Synergy-Crawler/Crawled_corpus_3000/"
base_filepath = "/home/dimitrios/Synergy-Crawler/Crawled_corpus_500/"
#base_filepath = "/home/dimitrios/Synergy-Crawler/Manually_Selected_Crawled_corpus_75/"
#htmls_path = "/html_500/"
htmls_path = "/html/"
#genres = [ "" ] 
#htmls_path = "/html/"
#base_filepath = "/home/dimitrios/Synergy-Crawler/Golden_Standared_from_Santinis_corpus/"

#base_filepath_w = "z:\\home\\dimitrios\\Synergy-Crawler\\Santini_corpus_html2txt\\"
#base_filepath_w = "z:\\home\\dimitrios\\Synergy-Crawler\\Crawled_corpus_3000\\"
#htmls_path_w = "\\html_500\\"
#base_filepath_w = "z:\\home\\dimitrios\\Synergy-Crawler\\Manually_Selected_Crawled_corpus_75\\"
base_filepath_w = "z:\\home\\dimitrios\\Synergy-Crawler\\Crawled_corpus_500\\"
htmls_path_w = "\\html\\"
#base_filepath_w = "z:\\home\\dimitrios\\Synergy-Crawler\\Golden_Standared_from_Santinis_corpus\\"
#htmls_path_w = "\\html\\"
#text_path_w = "\\htmldetagger_console_500_ver_text\\"
text_path_w = "\\htmldetagger_console_ver_text\\"

for g in genres:
    file_lst = bfile_hdlr.file_list_frmpaths(base_filepath, g + htmls_path)
    file_lst = [ fname.split('/')[-1] for fname in file_lst ]
    for html_f in file_lst:
        os.spawnlp(os.P_WAIT, '/usr/bin/wine', '/usr/bin/wine',\
                   '/home/dimitrios/.wine/drive_c/Program Files/JafSoft/Detagger/h2acons.exe',\
                   base_filepath_w + g + htmls_path_w + html_f,\
                   '/out=' + base_filepath_w + g + text_path_w + html_f.replace('.html', ".html.txt" ) )





