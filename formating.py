#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 10:11:12 2021

@author: ehab
"""

#xml_filename="/home/ehab/Downloads/data/tt.xml"
#xml2_filename="/home/ehab/Downloads/data/out.xml"
class Pretty():
    def pretty_xml(xml_filename):
        tags=[]
        indent=[]
        result=[]
        Str=""
        i=0
        with open(xml_filename,"r")as a_file:
            for line in a_file:
                stripped_line=line.strip()
                if stripped_line[0]=='<':
                    if stripped_line[1]=='/':
                        Str=stripped_line[2:stripped_line.index(">")]
                        result.append(indent[tags.index(Str)]*"  "+stripped_line)
                        
                        tags.remove(Str)
                    else:
                        if len(stripped_line)-stripped_line.index('>')==1:
                            tags.append(stripped_line[1:stripped_line.index(">")])
                            Str=stripped_line[1:stripped_line.index(">")]
                            indent.append(i)
                            i+=1
                            result.append(indent[tags.index(Str)]*"  "+stripped_line)
                            
                        elif len(stripped_line)-stripped_line.index('>')>1:
                            result.append((indent[tags.index(Str)]+1)*"  "+stripped_line)
                            
                else:
                    result.append((i)*"  "+stripped_line)
                   
                        
        return result
###############minifying####################
class minifying():
    def minifying_file(xml_filename):
        result=[]
        with open(xml_filename,"r")as a_file:
            for line in a_file:
                stripped_line=line.strip()
                result.append(stripped_line)
                
        return result


#pretty_xml(xml_filename)
#minifying_file(xml2_filename)
