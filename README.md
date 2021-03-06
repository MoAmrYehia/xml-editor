# XML Editor

<p align="center">
    <img src="https://github.com/MoAmrYehia/xml-editor/blob/main/screenshots/logo-removebg-preview.png">
</p>


This is a University project, where students could apply data structure concepts to a real-life project. At the end of this project, my team would be able to effectively implement different data structures from scratch, build an XML editor and convert XML to JSON. 

## Idea
XML (Extensible Markup Language) is one of the most famous formats for storing and sharing information among different devices. Some text editors such as Sublime Text are able to parse such files and do some basic operations. In this project, you will work on developing a GUI (Graphical User Interface) based program to parse and visualize an XML file.

## Main requirements

* Building a GUI in which the user can specify the location of an input XML file.

* Checking the XML consistency: The input XML may have inconsistencies like missing any of the closing and opening tags or not matching tags.The program should be able to detect and visually show any errors in consistency. Optimally, the program will also be able to automatically solve the errors.

* Formatting (Prettifying) the XML: the XML file should be well formatted by keeping the indentation for each level.

* Converting XML to JSON: JSON (Javascript Object Notation) is another format that is used to represent data. It’s helpful to convert the XML into JSON, especially when using javascript as there’s tons of libraries and tools that use json notation.

* Minifying the XML file: Since spaces and newlines (\n) are actually characters that can increase the size of an XML document. This feature should aim at decreasing the size of an XML file (compressing it) by deleting the whitespaces and indentations.

* Compressing the data in the XML/JSON file.

## How We Built It
The XML editor was built using PyQt5 to for the interactive GUI. PyQt5 allowed us to built a full user experience. For the backend we used python to enhance different functionality. 



## Current Contributors
<a href="https://github.com/MoAmrYehia/xml-editor/graphs/contributors">
    
  <img src="https://contributors-img.web.app/image?repo=MoAmrYehia/xml-editor" />
</a>
