"""https://www.hackerrank.com/challenges/html-parser-part-1/problem."""
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        if attrs:
            for i in attrs:
                print('-> {} > {}'.format(i[0], i[1]))

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        if attrs:
            for i in attrs:
                print('-> {} > {}'.format(i[0], i[1]))


def process_html(s):
    """Process input html text."""
    parser = MyHTMLParser()
    parser.feed(s)


if __name__ == '__main__':
    n = int(input())
    s = ''
    for _ in range(n):
        s += input() + '\n'
    process_html(s)
