# XML Editor

<p align="center">
    <img src="https://raw.githubusercontent.com/MoAmrYehia/xml-editor/main/screenshots/logo_README.png">
</p>



This is a University project, where students could apply data structure concepts to a real-life project. At the end of this project, my team would be able to effectively implement different data structures from scratch, build an XML editor and convert XML to JSON. 

## Idea
XML (Extensible Markup Language) is one of the most famous formats for storing and sharing information among different devices. Some text editors such as Sublime Text are able to parse such files and do some basic operations. In this project, you will work on developing a GUI (Graphical User Interface) based program to parse and visualize an XML file.

## Main requirements

⋅⋅⋅Building a GUI in which the user can specify the location of an input XML file.

⋅⋅⋅Checking the XML consistency: The input XML may have inconsistencies like missing any of the closing and opening tags or not matching tags.The program should be able to detect and visually show any errors in consistency. Optimally, the program will also be able to automatically solve the errors.

⋅⋅⋅Formatting (Prettifying) the XML: the XML file should be well formatted by keeping the indentation for each level.

⋅⋅⋅Converting XML to JSON: JSON (Javascript Object Notation) is another format that is used to represent data. It’s helpful to convert the XML into JSON, especially when using javascript as there’s tons of libraries and tools that use json notation.

⋅⋅⋅Minifying the XML file: Since spaces and newlines (\n) are actually characters that can increase the size of an XML document. This feature should aim at decreasing the size of an XML file (compressing it) by deleting the whitespaces and indentations.

⋅⋅⋅Compressing the data in the XML/JSON file: You should come-up with a way to reduce the size of the file using a data compression technique. You can invent your own ad-hoc method for such compression. On the other hand, you can check how JSONH works and try to distill ideas from it. Finally, you can use a data compression technique such as bytepair encoding [byte pair encoding](https://en.wikipedia.org/wiki/Byte_pair_encoding).The smaller the output file is, the more efficient your algorithm is.
