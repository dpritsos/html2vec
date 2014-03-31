


ret = [ '2TF', 'ase', 'htm', '/mo', 'TF ', '.ch', ' un', '2tf', 'l2t', 'l2v', 'eSt', 'ing', 'ge/', 'ams', 'or ', 'cha', 'est', 'Str', 'for',\
		 ' is', 'cla', 'e/m', 'fd.', 'ml2', 'pac', 'arn', 'ngr', 'gra', 'har', 'is ', 'F c', 'ass', 'g2T', 'his', 'kag', 'Bas', '2ve', 'ors',\
		 'it ', 'odu', 'mod', ' pa', 'ect', 'Thi', 'dul', ' te', '.Ba', 'nit', 'las', ' a ', 'cka', ' cl', 'd.c', 'ack', 'age', ' ht', 'ms.',\
		 'ng2', 'cto', ' fo', 'a u'\
      ]


exp = [
		
		' a ' , ' cl' , ' fo' , ' ht' , ' is', ' pa',\
            ' te', ' un',  '.Ba', '.ch', '/mo', '2TF',\
            '2tf', '2ve', 'Bas', 'F c', 'Str', 'TF ',\
            'Thi', 'a u', 'ack', 'age', 'ams', 'arn',\
            'ase', 'ass', 'cha', 'cka', 'cla', 'cto',\
            'd.c', 'dul', 'e/m', 'eSt', 'ect', 'est',\
            'fd.', 'for', 'g2T', 'ge/', 'gra', 'har',\
            'his', 'htm', 'ing', 'is ', 'it ', 'kag',\
            'l2t', 'l2v', 'las', 'ml2', 'mod', 'ms.',\
            'ng2', 'ngr', 'nit', 'odu', 'or ', 'ors',\
            'pac',\
      
            ]

terms_l = ['Thi', 'his', 'is ', 's i', ' is', 'is ', 's a', ' a ', 'a u', ' un', 'uni', 'nit', 'it ', 't t', ' te', 'tes', 'est', 'st ', 't f', ' fo', 'for', 'or ', 'r h', ' ht', 'htm', 'tml', 'ml2', 'l2t', '2tf', 'tfd', 'fd.', 'd.c', '.ch', 'cha', 'har', 'arn', 'rng', 'ngr', 'gra', 'ram', 'ams', 'ms.', 's.B', '.Ba', 'Bas', 'ase', 'seS', 'eSt', 'Str', 'tri', 'rin', 'ing', 'ng2', 'g2T', '2TF', 'TF ', 'F c', ' cl', 'cla', 'las', 'ass', 'ss ', 's f', ' fo', 'for', 'or ', 'r h', ' ht', 'htm', 'tml', 'ml2', 'l2v', '2ve', 'vec', 'ect', 'cto', 'tor', 'ors', 'rs ', 's p', ' pa', 'pac', 'ack', 'cka', 'kag', 'age', 'ge/', 'e/m', '/mo', 'mod', 'odu', 'dul', 'ule']

print len(ret), len(exp), len(terms_l)

print [ trm for trm in ret if trm not in exp ]
print [ trm for trm in ret if trm not in terms_l ]