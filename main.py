import urllib.request
from bs4 import BeautifulSoup
from FreqSearch import FqVis

unwanted_spc = ['.', ',', ':', '/', '<', '>', '=', '\n']
unwanted = ['(', ')', '{', '}', '[', ']', "'", '"', '“', '„', ';', '?', '!', '|']


# def parse_file(filename):
#     file = open(filename, 'r')
#     text_str = file.read()
#     file.close()
#     return text_str


def parse_web_content(url):
    response = urllib.request.urlretrieve(url)
    f = open(response[0])
    html_file = BeautifulSoup(f, "html.parser")
    f.close()
    urllib.request.urlcleanup()
    for script in html_file(['script', 'style']):
        script.extract()
    html_file = html_file.get_text()
    return html_file


def remove_garbage(text_str):
    for ch in unwanted_spc:
        text_str = text_str.replace(ch, " ")
    for ch in unwanted:
        text_str = text_str.replace(ch, "")
    return text_str


def freq(text_str):
    frq = {}
    for word in [w for w in text_str.split() if len(w) > 1]:
        if not frq.get(word):
            frq[word] = 1
        else:
            frq[word] += 1
    return frq


def readable(word_dict):
    new = [(key, word_dict[key]) for key in sorted(word_dict, key=word_dict.get, reverse=True)]
    for pair in new:
        if not str(pair[0]).isdecimal():
            print(pair)
    return new


web = parse_web_content("https://www.github.com/")
web_words = freq(web)
web_words = readable(web_words)

# article = remove_garbage(parse_file("article.txt"))
# words = freq(article)
# words = readable(words)

Visual = FqVis()
Visual.insert_sorted_data(web_words, 10)
Visual.draw_data()

while True:
    Visual.run()
