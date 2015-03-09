#!/usr/bin/python

import sys
from collections import OrderedDict

def main(amount_mapping, border_colored=True, title=None):
    yield """<html>
        <head>
            <title>{0}</title>
        </head>""".format(title if title else "")
    yield """<body style="font-family:arial; font-size:80px">"""

    yield "\n".join(generate_table(amount_mapping, border_colored))

    yield """\n\t</body></html>"""

def generate_table(amount_mapping, border_colored=True):
    cells = generate_cards(amount_mapping, border_colored)
    #import ipdb; ipdb.set_trace()
    total = sum(amount_mapping.values())
    columns = 4
    rows = (total/columns)+1

    yield "\n\t\t<table>"
    for rowno in range(rows):
        yield "\t\t\t<tr>"

        for i in range(columns):
            #print rowno, i
            try:
                cell = cells.next()
                yield "\t\t\t\t<td>"
                yield cell
                yield "\t\t\t\t</td>"
            except StopIteration:
                break
        #import pdb; pdb.set_trace()
        yield "\t\t\t</tr>"
    yield "\t\t</table>"

def generate_cards(amount_mapping, border_colored=True):
    #import ipdb; ipdb.set_trace()
    for imagepath, amount in amount_mapping.iteritems():
        imagecode = """<img src="{0}"/>""".format(imagepath)
        for i in range(amount):
            height,width = 180,180
            border_width = 1 if border_colored else 1
            height -= 2*border_width
            width -= 2*border_width
        
            yield """<div style='
                border: solid {3}px;
                text-align: center; 
                width: {2}px; 
                height: {1}px; 
                line-height: {1}px;
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

    with file(filename, "w+") as f:
        for html in main(amount_mapping, border_colored=True):
            f.write(html)
