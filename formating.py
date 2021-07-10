#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 10:11:12 2021

@author: ehab
"""
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
"""

#xml_filename="/home/ehab/Downloads/data/tt.xml"
#xml2_filename="/home/ehab/Downloads/data/out.xml"
def pretty_xml(xml_filename):
    tags=[]
    indent=[]
    Str=""
    i=0
    with open(xml_filename,"r")as a_file:
        for line in a_file:
            stripped_line=line.strip()
            if stripped_line[0]=='<':
                if stripped_line[1]=='/':
                    Str=stripped_line[2:stripped_line.index(">")]
                    print(indent[tags.index(Str)]*"  ",stripped_line)
                    tags.remove(Str)
                else:
                    if len(stripped_line)-stripped_line.index('>')==1:
                        tags.append(stripped_line[1:stripped_line.index(">")])
                        Str=stripped_line[1:stripped_line.index(">")]
                        indent.append(i)
                        i+=1
                        print(indent[tags.index(Str)]*"  ",stripped_line)
                    elif len(stripped_line)-stripped_line.index('>')>1:
                        print((indent[tags.index(Str)]+1)*"  ",stripped_line)
            else:
                print((i)*"  ",stripped_line)
                    
                    
###############minifying####################

def minifying_file(xml_filename):
    with open(xml_filename,"r")as a_file:
        for line in a_file:
            stripped_line=line.strip()
            print(stripped_line)


#pretty_xml(xml_filename)
#minifying_file(xml2_filename)
