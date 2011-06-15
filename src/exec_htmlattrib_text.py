
""" """

import htmlattrib.regex
import codecs

h2t = htmlattrib.regex.HtmlText() 
   
csvs = [ #'santinis_blog_pgs_hml_cleaned.csv', 'santinis_eshop_pgs_hml_cleaned.csv',\ 
         'santinis_faq_pgs_hml_cleaned.csv']
         #'santinis_listing_pgs_hml_cleaned.csv']
         #'santinis_frontpage_pgs_hml_cleaned.csv']
         #'santinis_php_pgs_hml_cleaned.csv' ]
        
base_filepath = "/home/dimitrios/Synergy-Crawler/Santini_corpus_html2txt/"
text_path = "/txt_rapidminer_app/"


def load_csv(filename):
    csv_lines = list()
    csv_line = list()
    buffer = 1
    rec_c = 0
    recored = ''
    EOR = None
    with codecs.open( str(filename), 'rb', 'utf-8', 'strict') as fenc:
        while True:
            read_buff = fenc.read(buffer)
            #print read_buff
            if not read_buff:
                break
            if read_buff == "~" and EOR:
                EOR += read_buff
            elif read_buff == "~":
                EOR = read_buff
            elif read_buff == ":" and EOR == "~~":
                EOR += read_buff
            elif EOR:
                print EOR,read_buff
                EOR = None
            if EOR == "~~:~~":
                #print EOR, "DONE"
                #print recored[:-4]
                csv_line.append( recored[:-4] )
                rec_c += 1
                recored = ''
                EOR = None
            else:
                recored += read_buff
                #print recored
            if rec_c == 9:
                print len(csv_line[0])
                csv_lines.append( csv_line[0:3] )
                csv_line = list()
                rec_c = 0
    print "DONE"
    return csv_lines

for csv in csvs:
    csv_lines = load_csv( base_filepath + csv )
    for line_c in csv_lines:
        print line_c[2], line_c[1] 
    fn_ftxt_l = [ [base_filepath + line[1].strip() + text_path + line[2].strip() + ".txt", line[0]] for line in csv_lines ]
    #print fn_ftxt_l[1] 
    h2t.save_files(None, fn_ftxt_l[1:], encoding='utf-8', error_handling='strict')
   
