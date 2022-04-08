#!/usr/bin/python

import sys
from math import ceil
from collections import OrderedDict
SIZE = (200, 200)  # (width, height)

def main(amount_mapping, border_colored=True, title=None):
    yield """<html>
        <head>
            <title>{0}</title>
            <style>img{{width:100%;  max-width:{1}px; height:100%;  max-height:{2}px;}}</style>
        </head>""".format(title if title else "", SIZE[0], SIZE[1])
    yield """<body style="font-family:arial; font-size:80px">"""

    yield "\n".join(generate_table(amount_mapping, border_colored))

    yield """\n\t</body></html>"""

def generate_table(amount_mapping, border_colored=True):
    cells = generate_cards(amount_mapping, border_colored)
    total = sum(amount_mapping.values())
    columns = 6
    rows = ceil((total/columns)+1)

    yield "\n\t\t<table>"
    for rowno in range(rows):
        yield "\t\t\t<tr>"

        for i in range(columns):
            #print rowno, i
            try:
                cell = next(cells)
                yield "\t\t\t\t<td>"
                yield cell
                yield "\t\t\t\t</td>"
            except StopIteration:
                break
        #import pdb; pdb.set_trace()
        yield "\t\t\t</tr>"
    yield "\t\t</table>"

def generate_cards(amount_mapping, border_colored=True):
    for imagepath, amount in amount_mapping.items():
        imagecode = """<img src="{0}" height="{2}" width="{1}"/>""".format(imagepath, SIZE[0], SIZE[1])
        for i in range(amount):
            height,width = SIZE
            border_width = 1 if border_colored else 1
            height -= 2*border_width
            width -= 2*border_width
        
            yield """<div style='
                border: solid {3}px;
                text-align: center; 
                width: {1}px; 
                height: {2}px; 
                line-height: {2}px;
                margin: 5px; 
                vertical-align:bottom; 
                padding: 10px;
                font-size: 70px'>
            {0}</div>""".format(imagecode, height, width, border_width)

if __name__ == "__main__":
    filename = sys.argv[1]

    amounts = sys.argv[2:]

    amount_mapping = OrderedDict()
    for amountstr in amounts:
        parts = amountstr.split(":")
        amount_mapping[parts[0]] =int(parts[1])

    with open(filename, "w+") as f:
        for html in main(amount_mapping, border_colored=True):
            f.write(html)
