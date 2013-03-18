# -*- coding: utf-8  -*-

"""
Main configuration
"""

"""
    * FILE_DIR        : location for input and output files (ended with slash /)
    * INDEX_URL       : list of URLs for source index pages of news
    * NEWS_NUM        : number of news to capture at one time
    * ID_PATTERN      : pattern for matching news ID
    * Q_PATTERN       : quasi-pattern URL string for substituting news ID
    * API_URL         : URL of MediaWiki API (URI of path to api.php)
    * BOT_NAME        : name of the bot account you want to display on wiki page comment
    * SEM_DATE_PATTERN: system-generated date pattern in the news page (e.g. 2013-11-01)
    * SYS_DATE_PATTERN: semantic generated date pattern in the news page (e.g. March 1, 2013)
    * INVALID_PATTERN : nullify news that match any patterns listed
    * SUB_FILTER      : replacement patterns
    * EXCEPTION_LIST  : exceptions for semantic parse matching which generates wiki links
    * TEMPLATES       : dictionary mapping target template page at MediaWiki sites

"""
FILE_DIR     = "/home/anshichao/newscapture/local/"
INDEX_URL    = [
                "http://news.ustb.edu.cn/html/Article_Class2_1_1.html", 
                "http://news.ustb.edu.cn/html/Article_Class2_1_2.html",
               ]

NEWS_NUM    = 4
ID_PATTERN  = r"Article_Show\.asp\?ArticleID=(\d+)"
Q_PATTERN   = "http://news.ustb.edu.cn/html/article/Article_show%s.html"
API_URL     = "http://wiki.ibeike.com/api.php" 
BOT_NAME    = "Mitsuki Kojima"

SEM_DATE_PATTERN = u'(\d{4})年(\d+)月(\d+)日'        # Semantic date pattern 
SYS_DATE_PATTERN = r'(\d{4})-(\d+)-(\d+)'           # System date pattern


INVALID_PATTERN = [
                   u"^.+：",        # Derivative news prefix (e.g. 光明日报：)
                   u"^.+:",
                   u"【视频】",      # Those with [Video] tags
                   r"\S+\s+\S+",    # Those with whitespace(s) in the middle
                   r"\S+&nbsp;\S+", # Those with HTML whitespace in the middle
				   r";",
                   ] 

SUB_FILTER = {
              u"\S+\u2014\u2014(\S+)" : r"\1", # \u2014 and \u2015 are common Chinese dashes 
              u"\S+\u2015\u2015(\S+)" : r"\1",
              u"我校"       : u"北京科技大学",
              u"我国"       : u"中国",
              }

EXCEPTION_LIST = [
                  u"北京科技大学", 
                  u"北京科技大",
                  u"勤",
                  u"党委",
                  ]

TEMPLATES = {
                 'news_ref'  :  u"Template:NewsAuto",
                 'news_unref':  u"Template:NewsAutoUntagged",
                 }
