newscapture for MediaWiki
=========================
Sync news titles from an external news website to specific pages on your MediaWiki site.

Applicability
_____________
* MediaWiki site which is routinely maintained with `Pywikipediabot <http://www.mediawiki.org/wiki/Manual:Pywikipediabot>`_
* External news site which does not provide RSS feed, but has only index pages of news titles and links (URLs are ID-incremented)

Prerequisites
_____________
* `Pywikipediabot <http://www.mediawiki.org/wiki/Manual:Pywikipediabot>`_
* An authorized bot account on your MediaWiki to be associated with Pywikipediabot

Features
________
* Capture and dump news from the specified site into TXT files (can be imported to MediaWiki site using Pywikipediabot)
* Parse news contents and provide internal links of matched existing pages (through API) on your MediaWiki site
* Provide both unreferenced news and referenced news
* Set and prioritize multiple index pages of news
* Set arbitrary number of news to capture each time
* Configure filtering rules, substitute rules and internal links matching rules

Install
_______
1. Download the zip file or clone the code, and put it wherever you like

.. code-block:: bash
    
    $ git clone https://github.com/moleculea/newscapture.git

2. Create a directory wherever you like to hold output and input files (FILE_DIR in ``conf.py``)

.. code-block:: bash
	
	$ mkdir <FILE_DIR>

Usage
_____

1. Configuration: edit ``conf.py``; see docstring in this file for help info;
2. Script configuration (optional): edit sample ``sync.sh`` or write your own script; if you use the sample script, create an empty file named ``flag``:

.. code-block:: bash
	
	$ touch flag

It indicates whether there is NEW news each time you execute ``main.py``;

3. Test:

.. code-block:: bash

    $ python main.py

See if the following files are created in ``<FILE_DIR>``:

.. code-block:: bash

    news_append.txt
    news.id
    news_ref.txt
    news_unref.txt

* **news.id**: stores the ID of the last synced news (largest)

* **news_append.txt**: stores NEW news which differed from the last sync. This is useful for you to collect news to a single list page on your MediaWiki site. Use the following Pywikipedia command to upload (append) this file:

.. code-block:: bash

	$ python /path/to/pywikipedia/add_text.py -textfile:/path/to/<FILE_DIR>/news_append.txt \
	-page:<WIKI_PAGE> -bottom -always

* **news_ref.txt**: news with reference links. This file has the following format:

::
	
	AAAA<!-- automatically created content by Foobar-Bot 2013-03-16 14:00:02-->TTTTTemplate:NewsPageTTTT

	News contents ...

	BBBB

Use the following Pywikipedia command to upload this file to your MediaWiki site: 

.. code-block:: bash

	$ python /path/to/pywikipedia/pagefromfile.py -start:AAAA -end:BBBB \
	-titlestart:TTTT -titleend:TTTT -file:/path/to/news_ref.txt

* **news_unref.txt**: news with no reference links. The Pywikipedia command to upload this file is similar to that of ``news_ref.txt``

4. Deploy: use cron to periodically run your customized shell script. 

.. code-block:: bash

	$ crontab -e

Use the following sample schedule if you want to sync news every two hours

::

	0 */2 * * * /path/to/sync.sh >/dev/null 2>&1

Version
_______

0.1


Author
______

Email: moleculeaweb AT gmail DOT com



License
_______

BSD License
