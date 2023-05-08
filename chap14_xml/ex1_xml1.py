"""https://www.hackerrank.com/challenges/xml-1-find-the-score/problem."""
import xml.etree.ElementTree as etree
import sys


def get_attr_number(node):
    attr_number = 0
    for element in node.iter():
        attr_number += len(element.attrib)
    return attr_number


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
