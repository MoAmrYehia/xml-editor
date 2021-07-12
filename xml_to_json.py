"""
Created on Fri Jul  9 03:10:11 2021
@author: Mohamed Amr
"""

# Define XML file and JSON file names and path
xml_file_name = 'data.xml'
json_file_name = "data.json"


#Import related libraries
import json
import re

xml_file_name = 'data.xml'
json_file_name = "data.json"


def get_xml_dict(fileArg):

    res = re.findall("<(?P<var>\S*)(?P<attr>[^/>]*)(?:(?:>(?P<val>.*?)</(?P=var)>)|(?:/>))", fileArg)
    if len(res) >= 1:
        attreg="(?P<avr>\S+?)(?:(?:=(?P<quote>['\"])(?P<avl>.*?)(?P=quote))|(?:=(?P<avl1>.*?)(?:\s|$))|(?P<avl2>[\s]+)|$)"

        if len(res) > 1:
            return [{i[0]:[{"@attributes" : [{j[0]:(j[2] or j[3] or j[4])} for j in re.findall(attreg, i[1].strip())]},
                            {"$values":get_xml_dict(i[2])}]} for i in res]
        
        else:
            return {res[0]:[{"@attributes" : [{j[0]:(j[2] or j[3] or j[4])} for j in re.findall(attreg, res[1].strip())]},
                             {"$values":get_xml_dict(res[2])}]}
    else:
        return fileArg
    
    
def convert_xml_to_json(xml_file_name):
    with open(xml_file_name , 'r') as fil:    
        return json.dumps(get_xml_dict(fil.read()))

def save_json(json_file_name, xml_object):
    
    json_file = open(json_file_name, "w")
    json_file.write(xml_object)
    json_file.close()
    
    return
    
    



#xml_object = convert_xml_to_json(xml_file_name) To test the functions
#save_json(json_file_name, xml_object)    


