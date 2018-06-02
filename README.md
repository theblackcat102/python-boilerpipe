# python-boilerpipe


A python wrapper for [Boilerpipe](http://code.google.com/p/boilerpipe/), an excellent Java library for boilerplate removal and fulltext extraction from HTML pages.

## Configuration


Dependencies:

 * JPype1
 * chardet

The boilerpipe jar files will get fetched and included automatically when building the package.

## Installation

Checkout the code:

	git clone https://github.com/misja/python-boilerpipe.git
	cd python-boilerpipe


**virtualenv**

	virtualenv env
	source env/bin/activate
    pip install -r requirements.txt
	python setup.py install
	

**Fedora**

    sudo dnf install -y python2-jpype
    sudo python setup.py install


## Usage


Be sure to have set `JAVA_HOME` properly since `jpype` depends on this setting.

The constructor takes a keyword argment `extractor`, being one of the available boilerpipe extractor types:

 - DefaultExtractor
 - ArticleExtractor
 - ArticleSentencesExtractor
 - KeepEverythingExtractor
 - KeepEverythingWithMinKWordsExtractor
 - LargestContentExtractor
 - NumWordsRulesExtractor
 - CanolaExtractor

This version only accept html text and you have to crawl the html yourself
    from boilerpipe.extract import Extractor
    extractor = Extractor(html_text, extractor='ArticleExtractor')

Then, to extract relevant content:

    extracted_text = extractor.get_text()

    extracted_html = extractor.get_html()


For `KeepEverythingWithMinKWordsExtractor` we have to specify `kMin` parameter, which defaults to `1` for now:

	extractor = Extractor(extractor='KeepEverythingWithMinKWordsExtractor', url=your_url, kMin=20)


## Performance

Running test.py obtain the rough estimation of each extraction performance:

ArticleExtractor : 37.50 iteration per second = 27ms per extraction 
DefaultExtractor :  38.55 iteration per second = 26ms per extraction
ArticleSentencesExtractor :  40.68 iteration per second = 25ms per extraction
LargestContentExtractor : 35.37 iteration per second = 28ms per extraction

Benchmark was done on an i5-5250U, 4G RAM, Mac OS 10
