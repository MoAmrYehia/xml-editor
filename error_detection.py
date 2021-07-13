class ErrorDetection():
    def collectTags(self, filename):
        #Parses the xml file and collects tags
        tags = []
        line_num = 0
        with open(filename) as f:
            for line in f:
                line_num = line_num + 1
                if line.find('<!') != -1: #A comment line
                    line = line[:line.find('<!')] + line[line.find('->') + 1:]
                if line.find('<?') != -1: #A Declaration line
                    continue
                if line.find('/>') != -1:
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

    def detectErrors(self, filename):
        #Checks if there are errors, returns the errors and lines each with a flag indicating error
        tags = self.collectTags(filename)
        queue = []
        lines_queue = []
        errors = []
        error_lines = []
        line_type = []
        error_line = -1
        ind = 0
        for tag in tags:
            error_line = tag[0]
            ind = ind + 1

            if '/' not in tag[1]:    # Opening tag
                queue.append(tag[1])
                lines_queue.append(tag[0])
            elif '/' in tag[1]:      # Closing tag
                # Collecting tag names
                ind_end = None
                tag_names = []
                for i in tags:
                    tag_names.append(i[1])
                    if i[1] == '<' + tag[1][2:] and tag_names.index(i[1]) > ind:
                        ind_end = tag_names.index(i[1])

                if len(queue) > 0 and tag[1] == '</' + queue[-1][1:]:
                    queue.pop()
                    lines_queue.pop()
                else:
                    # Tag mismatch - error type 1
                    if len(queue) > 0 and '</' + queue[-1][1:] not in tag_names[ind:ind_end] and '<' + tag[1][2:] not in queue:
                        errors.append([tag[1], error_line, 1])
                        error_lines.append(error_line)
                        line_type.append([error_line, 1])
                        queue.pop()
                        lines_queue.pop()
                    else:
                        # Tag opened with no closing - error type 2
                        if '</' + queue[-1][1:] not in tag_names[ind:ind_end]:
                            
                            errors.append([queue[-1], lines_queue[-1], 2])
                            error_lines.append(lines_queue[-1])
                            line_type.append([lines_queue[-1], 2])
                            queue.pop()
                            lines_queue.pop()
                            # Check if the top of queue is the matching tag
                            if '</' + queue[-1][1:] == tag[1]:
                                queue.pop()
                                lines_queue.pop()
                        # Tag closed with no opening - error type 3
                        elif '/' in tag_names[ind - 1]:
                            errors.append([tag[1], tag[0], 3])
                            error_lines.append(tag[0])
                            line_type.append([tag[0], 3])
        
        # Tags opened with no closing - error type 2          
        if len(queue) != 0:
            for element in queue:
                errors.append([element, error_line, 2])
                error_lines.append(error_line)
                line_type.append([error_line, 2])

        ind = 0
        lines = []
        type = 0
        with open(filename) as f:
            for curr_line in f:
                ind = ind + 1
                if ind in error_lines:
                    for i in line_type:
                        if i[0] == ind: 
                            type = i[1]
                            break
                    lines.append([curr_line, 1, type])
                else:
                    lines.append([curr_line, 0, 0])

        return errors, lines

    def correctErrors(self, filename):
        errors, lines = self.detectErrors(filename)
        line_num = 0
        lines = []
        lines_with_error = []
        # Collecting lines with error
        for error in errors:
            lines_with_error.append(error[1])

        with open(filename) as f:
            for curr_line in f:
                line_num = line_num + 1

                if line_num not in lines_with_error:
                    lines.append(curr_line)
                    continue
                else:
                    error_string = ''
                    error2_flag = 0   # To correctly order tags
                    for error in errors:
                        if error[1] == line_num:
                            if error[2] == 1:   # mismatch
                                lines.append('<' + error[0][2:] + curr_line[curr_line.index('>') + 1:])
                            elif error[2] == 2: # no close tag
                                error_string = '</' + error[0][1:] + '\n' + error_string 
                                error2_flag = 1
                            else:               # no open tag
                                lines.append('<' + error[0][2:] + curr_line)
                    if error2_flag:
                        lines.append(curr_line + error_string)
        return lines

tags = ErrorDetection().collectTags('/home/ehab/Downloads/data/tt.xml')
errors, error_lines = ErrorDetection().detectErrors('/home/ehab/Downloads/data/tt.xml')
correct_lines = ErrorDetection().correctErrors('/home/ehab/Downloads/data/tt.xml')
print(error_lines)