#
#    Module: Base HTML 2(to) HTML Attributes   
# 
#    Author: Dimitiros Pritsos 
#    
#    License: BSD Style
#
#    Last update: Please refer to the GIT tracking 
# 

""" html2vect.base.features.html2attrib: submodule of `html2tf` module defines the class BaseHTML2Attributes """ 

import re
import unicodedata
import htmlentitydefs as hedfs


#The HTML tags list cosist of the full W3C tag list including HTML 5.0 and HTML 4.0.1 which they are depricated in HTML5 
html_tags_lst = ['<!--', '<!DOCTYPE', '<a', '<abbr', '<acronym', '<address', '<applet', '<area', '<article', '<aside', '<audio', '<b',\
                 '<base', '<basefont', '<bdi', '<bdo', '<big', '<blockquote', '<body', '<br', '<button', '<canvas', '<caption', '<center',\
                 '<cite', '<code', '<col', '<colgroup', '<command', '<datalist', '<dd', '<del', '<details', '<dfn', '<dir', '<div', '<dl',\
                 '<dt', '<em', '<embed', '<fieldset', '<figcaption', '<figure', '<font', '<footer', '<form', '<frame', '<frameset', '<head',\
                 '<header', '<hgroup', '<h1', '<h6', '<hr', '<html', '<i', '<iframe', '<img', '<input', '<ins', '<kbd', '<keygen', '<label',\
                 '<legend', '<li', '<link', '<map', '<mark', '<menu', '<meta', '<meter', '<nav', '<noframes', '<noscript', '<object', '<ol',\
                 '<optgroup', '<option', '<output', '<p', '<param', '<pre', '<progress', '<q', '<rp', '<rt', '<ruby', '<s', '<samp', '<script',\
                 '<section', '<select', '<small', '<source', '<span', '<strike', '<strong', '<style', '<sub', '<summary', '<sup', '<table', '<tbody',\
                 '<td', '<textarea', '<tfoot', '<th', '<thead', '<time', '<title', '<tr', '<track', '<tt', '<u', '<ul', '<var', '<video', '<wbr' ]
html_tags_lst.sort(reverse=True)


class BaseHTML2Attributes(object):
    
    def __init__(self, valid_html=False):
        
        #Option whether or not to return a valid HTML
        self.valid_html = valid_html
        
        #RegEx General for all HTML tags
        self.html_tags = re.compile(r'<[^>]+>')
                
        #RegEx using only for keeping only the proper HTML document, i.e. starts with <html> and ends with </html>        
        self.proper_html = re.compile(r'<html[^>]*>[\S\s]+</html>', re.UNICODE|re.IGNORECASE)
        
        #RegEx for HTML comemts
        self.html_comments = re.compile(r'<!--[\s\S]*?-->', re.UNICODE|re.IGNORECASE)
        
        #RegEx for HTML document type
        self.html_doctype_tag = re.compile(r'<!DOCTYPE[^>]*?>')
        
        #This meta tag content extraction regular expression is rejecting http-equiv content 
        #and can extract content inside or outside quotes while quotes are discarded 
        self.html_meta = re.compile(r'<meta(?![\s]*name="??http-equiv"??)[\s\S]*content="?([\S\s]*?)"?[\s]*/>', re.UNICODE|re.IGNORECASE)
               
        #RegEx for embedded Scripts in HTML
        self.html_scripts = re.compile(r'<script[^>]*>[\S\s]*?</script>', re.UNICODE|re.IGNORECASE)
        
        #RegEx for embedded Styles in HTML
        self.html_style = re.compile(r'<style[^>]*>[\S\s]*?</style>', re.UNICODE|re.IGNORECASE)
        
        #RegEx for white space characters, i.e., space, tab, carriage return, etc.
        self.whitespace_chars = re.compile(r'[\s]+', re.UNICODE)   # {2,}')
        
        #RegEx for NULL character
        self.NULL_chars = re.compile(r'[\x00]', re.UNICODE)   # {2,}')
        
        #RegEx for UTF-8 Replacement Character 
        self.unknown_char_seq = re.compile(r'['+ unicodedata.lookup('REPLACEMENT CHARACTER') +']+', re.UNICODE|re.IGNORECASE) #{2,}')
        
        #RegEx for HTML entities
        self.html_entities_name = re.compile(r'(&([\w]{2,8});)')
        
        #RegEx for HTML entities with omitted semicolon
        self.html_entname_nosemicolon = re.compile(r'(&([\w]{2,8}))')
        
        #RegEx for HTML entities with numerical form
        self.html_entities_number = re.compile(r'(&#([\d]+?);)')
        
        #RegEx for HTML entities with numerical form and omitted semicolon
        self.html_entnum_nosemicolon = re.compile(r'(&#([\d]+?))')
        
        #Build and Define a Regular Expression for matching incomplete HTML tags
        find_tgs = r'('
        condition_tgs = r'(?:'
        
        for tag in html_tags_lst:
            find_tgs += '<' +tag + r'|'
            condition_tgs += r'(?<=<' + tag + r')|'
            
        find_tgs = find_tgs.rstrip(r'|')
        condition_tgs = condition_tgs.rstrip(r'|')
        find_tgs += r')'
        condition_tgs += r')'  
        missclosed_tags_regex = find_tgs + condition_tgs + r'((?:[\s]+?[\S]+=[\S]+)*)'
        
        self.html_missclosed_tags = re.compile( missclosed_tags_regex )           


    def removehtmltags(self, text, repalce_char=' '):
        
        #Clean-up HTML tags
        text = self.html_tags.sub(repalce_char, text)
        
        #Clean-up miss-closed HTML tags
        missclosed_tags_lst = self.html_missclosed_tags.findall(text)
        if missclosed_tags_lst:
            for tag_str, attribs_str in missclosed_tags_lst:
                text =  text.replace((tag_str + attribs_str), '')
                
        return text
        
                    
    def encoding_norm(self, str):
        """ NOT WORKING AS EXPECTED - TO BE FIXED """
        
        #Normalise unicode text data (Refer to unicodedata module) 
        try:
            encod_str = unicodedata.normalize('NFKC', str)
        except Exception as e:
            print("WHILE UTF-8 NORMALIZATION" % e)  
            encod_str = unicodedata.normalize('NFKC', str.decode('utf-8'))
            print ("STRING ASSUMED TO BE ENCODED-UTF8-BYTE-STRING and DECODED TO PROPER UTF-8")
            
        return encod_str

    
    def htmlentities2utf8(self, str):
        
        for entity, etname in self.html_entities_name.findall(str):
            #Last argument in str.replace() is for maximum number of occurrences to be replaced
            try:
                str = str.replace(entity, unichr( hedfs.name2codepoint[ etname ] ), 1) 
            except Exception as e:
                pass
                #print("ERROR converting HTML entities to UTF-8 - There is no html entity: %s, %s" % (entity, e))
                
        for entity, etname in self.html_entities_number.findall(str):
            #Last argument in str.replace() is for maximum number of occurrences to be replaced
            try:
                str = str.replace(entity, unichr( int(etname) ), 1)
            except Exception as e:
                pass
                #print("ERROR converting HTML entities to UTF-8 - There is no html entity: %s, %s" % (entity, e))
        #Is trying to catch the error composed html entity characters and ref-numbers 
        
        for entity, etname in self.html_entname_nosemicolon.findall(str):
            try:
                str = str.replace(entity, unichr( hedfs.name2codepoint[ etname ] ), 1)
            except Exception as e:
                pass
                #print("ERROR converting HTML entities to UTF-8 - There is no html entity: %s, %s" % (entity, e)) 
                
        for entity, etname in self.html_entnum_nosemicolon.findall(str):
            try:
                str = str.replace(entity, unichr( int(etname) ), 1)
            except Exception as e:
                pass
                #print("ERROR converting HTML entities to UTF-8 - There is no html entity: %s, %s" % (entity, e))
                
        return str
    
                    
    def text(self, xhtml_str):
        
        if self.valid_html:
            properhtml = self.proper_html.findall(xhtml_str)
        else:
            properhtml = xhtml_str
            
        if not properhtml:
            return ""
        else:
            #Concatenate HTML parts in case there is an tag soup and we have a case of several <html></html> tag pairs
            if isinstance(properhtml, list) and properhtml > 1:
                text  = " ".join( properhtml )
            else:
                text  = properhtml
                
            #Clean-up comments
            text = self.html_comments.sub('', text)
            
            #Clean-up <!DOCTYPE> tag
            text = self.html_doctype_tag.sub('', text)
            
            #Get meta tags content
            meta_content_l = self.html_meta.findall(text)
            
            #Clean-up Scripts
            text = self.html_scripts.sub('', text)
            
            #Clean-up Style tags
            text = self.html_style.sub('', text)
            
            #Clean-up HTML tags
            text = self.removehtmltags(text, repalce_char=' ') 
            
            #Replace HTML Entity Number and Name with the proper utf8 character
            text = self.htmlentities2utf8(text)
            
            #Normalise Encoding
            ###norm_text = self.encoding_norm(text)
            #Replace NULL bytes - Yes! encoding and decoding conversion may cause this  
            text = self.NULL_chars.sub(' ',text)
            
            #Replace whitespace chars with single space
            text = self.whitespace_chars.sub(' ', text)
            
            #Replace utf8 'REPLACEMENT CHARACTER' with empty string
            text = self.unknown_char_seq.sub('', text)
            
            #Remove whitespace from the beginning of text if any
            text = text.lstrip()
            
            #Remove newline character from the end of text if any
            text = text.rstrip(u'\n')
            
            #Add meta tags text content to the rest of the html text
            #if meta_content_l[0]: ### MAYBE THIS SHOULD BE OPTIONAL FOR A INSTANCE OF THIS CLASS
            #    for  meta_content in meta_content_l:
            #        print meta_content
            #        0/0
            #        text = meta_content + " " + text 
        
        return text
    
    
    def tags(self, xhtml_str):
        
        if self.valid_html:
            properhtml = self.proper_html.findall(xhtml_str)
        else:
            properhtml = xhtml_str
            
        if not properhtml:
            return ""
        else:
            #Concatenate HTML parts in case there is an tag soup and we have a case of several <html></html> tag pairs
            if isinstance(properhtml, list) and properhtml > 1:
                text  = " ".join( properhtml )
            else:
                text  = properhtml
                       
            #Get only HTML tags
            text = " ".join( self.html_tags.findall(text) )
            
        return text 
    
    
    def scripts(self, xhtml_str):
        pass
    
    
    def get_styles(self, xhtml_str):
        pass
    
    