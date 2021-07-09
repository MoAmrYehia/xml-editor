import re

def collect_tags(filename):
    #Parses the xml file and collects tags
    tags = []
    with open(filename) as f:
        for line in f:
            if line.find('<!') != -1: #A comment line
                continue
            if line.find('<?') != -1: #A Declaration line
                continue
            
            while line.find('<') != -1:
                if line[line.find('<') + 1] != '/':
                    open_tag = line[line.find('<'): line.find('>') + 1]
                    if '=' in open_tag:
                        open_tag = open_tag[: open_tag.find(' ')] + '>'
                    tags.append(open_tag)
                    line = re.sub(line[line.find('<'): line.find('>') + 1], ' ', line)
                         
                if line.find('</') != -1:
                    close_tag = line[line.find('</'): line.find('>') + 1]
                    tags.append(close_tag)
                    line = re.sub(line[line.find('</'): line.find('>') + 1], '', line)
                
    while "" in tags:
        tags.remove("")   

    return tags

def hasErrors(tags):
    #Checks if there are errors, returns the error tag
    queue = []
    for tag in tags:
        if '/' not in tag: #An open tag
            queue.append(tag)
        elif '/' in tag:
            if len(queue) > 0 and tag == '</' + queue[-1][1:]:
                queue.pop()
            else:
                return True, queue[-1]
    if len(queue) == 0:            
        return False
    return True, queue[-1]

# tags = collect_tags('file.xml')
# print(hasErrors(tags))
