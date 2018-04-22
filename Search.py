import urllib
from bs4 import BeautifulSoup

unwanted_spc = ['.', ',', ':', '/', '<', '>', '=', '\n']
unwanted = ['(', ')', '{', '}', '[', ']', "'", '"', '“', '„', ';', '?', '!', '|']


class FreqSearch:
    def __init__(self):
        self.data = []

    def process(self, url, count=10):
        web = self._parse_web_content(url)
        web = self._freq(web)
        web = self._readable(web)
        self.data = web[:count]

    def _parse_web_content(self, url):
        response = urllib.request.urlretrieve(url)
        f = open(response[0])
        html_file = BeautifulSoup(f, "html.parser")
        f.close()
        urllib.request.urlcleanup()
        for script in html_file(['script', 'style']):
            script.extract()
        html_file = html_file.get_text()
        return html_file

    def _freq(self, text_str):
        frq = {}
        for word in [w for w in text_str.split() if len(w) > 1]:
            if not frq.get(word):
                frq[word] = 1
            else:
                frq[word] += 1
        return frq

    def _readable(self, word_dict):
        return [(key, word_dict[key]) for key in sorted(word_dict, key=word_dict.get, reverse=True)]

    def get_data(self):
        return self.data
