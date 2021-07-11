import re

def collect_tags(filename):
    #Parses the xml file and collects tags
    tags = []
    line_num = 0
    with open(filename) as f:
        for line in f:
            line_num = line_num + 1
            if line.find('<!') != -1: #A comment line
                continue
            if line.find('<?') != -1: #A Declaration line
                continue
            
            while line.find('<') != -1:
                ind_start = line.find('<')
                ind_end = line.find('>')
                if line[ind_start + 1] != '/':
                    open_tag = line[ind_start: ind_end + 1]
                    if '=' in open_tag:
                        open_tag = open_tag[: open_tag.find(' ')] + '>'
                    tags.append([line_num, open_tag])
                    line = line[:ind_start] + line[ind_end + 1:]
                         
                if line.find('</') != -1:
                    ind_start = line.find('</')
                    ind_end = line.find('>')
                    close_tag = line[ind_start: ind_end + 1]
                    tags.append([line_num, close_tag])
                    line = line[:ind_start] + line[ind_end + 1:]
                
    while "" in tags:
        tags.remove("")   

    return tags

def hasErrors(tags):
    #Checks if there are errors, returns the error tag
    queue = []
    error_line = -1
    errors = []
    ind = 0
    for tag in tags:
        error_line = tag[0]
        ind = ind + 1

        if '/' not in tag[1]:    #Opening tag
            queue.append(tag[1])

        elif '/' in tag[1]:      #Closing tag
            tag_names = []
            for i in tags:
                tag_names.append(i[1])
            if len(queue) > 0 and tag[1] == '</' + queue[-1][1:]:
                queue.pop()
            # Tag opened with no closing
            elif len(queue) > 0 and '</' + queue[-1][1:] not in tag_names[ind:]:
                errors.append([queue[-1], error_line])
                queue.pop()
            # Tag closed with no opening
            elif len(queue) == 0 or '<' + tag[1][2:] not in queue:
                errors.append([tag, tag[0]])
            # Tag mismatch
            else:
                errors.append([tag, error_line])
                
    if len(queue) == 0:            
        return False
    # errors.append([queue[-1], error_line])
    return errors

tags = collect_tags('file.xml')
# print(tags)
print(hasErrors(tags))
