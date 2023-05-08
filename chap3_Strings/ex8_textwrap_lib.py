"""
textwrap.fill.
Signature: textwrap.fill(text, width=70, **kwargs)
Docstring:
Fill a single paragraph of text, returning a new string.

Reformat the single paragraph in 'text' to fit in lines of no more
than 'width' columns, and return a new string containing the entire
wrapped paragraph.  As with wrap(), tabs are expanded and other
whitespace characters converted to space.  See TextWrapper class for
available keyword args to customize wrapping behaviour.
File:      /usr/local/lib/python3.6/textwrap.py
Type:      function
"""
import textwrap


def wrap(string, max_width):
    """
    """
    return textwrap.fill(string, max_width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
