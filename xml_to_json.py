import xmltodict, json


# Define XML file and JSON file names and path
xml_file_name = 'data.xml'
json_file_name = "data.json"


def save_xml(json_file_name, xml_object):
    
    json_file = open(json_file_name, "w")
    json_file.write(xml_object)
    json_file.close()
    
    return

def convert_xml_to_json(xml_file_name):
    with open(xml_file_name , 'r') as myfile:
        obj = xmltodict.parse(myfile.read())    
        
    return json.dumps(obj)


xml_object = convert_xml_to_json(xml_file_name)
save_xml(json_file_name, xml_object)



