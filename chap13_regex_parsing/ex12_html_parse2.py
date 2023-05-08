"""https://www.hackerrank.com/domains/python/py-regex/2."""
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print('>>> Multi-line Comment')
            print(data)
        else:
            print('>>> Single-line Comment')
            print(data)

    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)


def main():
    html = ''
    parser = MyHTMLParser()
    for i in range(int(input())):
        html += input().rstrip() + '\n'
    parser.feed(html)
    parser.close()


if __name__ == '__main__':
    main()
