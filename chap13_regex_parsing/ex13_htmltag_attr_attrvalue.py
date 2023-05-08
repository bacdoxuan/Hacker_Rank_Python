"""https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem."""
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for i in attrs:
                print('-> {} > {}'.format(i[0], i[1]))

    def handle_startendtag(self, tag, attrs):
        print(tag)
        if attrs:
            for i in attrs:
                print('-> {} > {}'.format(i[0], i[1]))


def main():
    html = ''
    parser = MyHTMLParser()
    for i in range(int(input())):
        html += input().rstrip() + '\n'
    parser.feed(html)
    parser.close()


if __name__ == '__main__':
    main()
