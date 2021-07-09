#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 10:11:12 2021

@author: ehab
"""
import xml.dom.minidom
import re

xml_filename="/home/ehab/Downloads/data/data-sample.xml"

dom = xml.dom.minidom.parse(xml_filename)
ugly=dom.toprettyxml(indent='  ')

text_re=re.compile('>\n\s+([^<>\s].*?)\n\s+</',re.DOTALL)
prettyxml= text_re.sub('>\g<1></',ugly)

print (prettyxml)



from xml.etree import ElementTree

def indent(elem, level=0):
    i = "\n" + level*"  "
    j = "\n" + (level-1)*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = j
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = j
    return elem        

root = ElementTree.parse(xml_filename).getroot()
indent(root)
ElementTree.dump(root)