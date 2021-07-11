#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 07:54:18 2021

@author: ehab
"""
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import tkinter as tk
from tkinter import filedialog
from formating import *




from PyQt5.uic import loadUi



class login(QMainWindow):
    def __init__(self):
        super(login, self).__init__()
        loadUi("ui/xml_main.ui",self)
        self.pushButton.clicked.connect(self.Browse)
        
        
        
    def Browse(self):
        root=tk.Tk()
        root.withdraw()
        
        file_path=filedialog.askopenfilename()
        if(file_path!=None):
            print(file_path) ##pass the file path to the open class
            widget.addWidget(functionpage(file_path))
            widget.setCurrentIndex(widget.currentIndex() + 1)
           
            
            
class functionpage(QMainWindow):
    def __init__(self,file_path):
        super(functionpage, self).__init__()
        loadUi("ui/editor.ui",self)
        self.file_path=file_path
        self.pushButton.clicked.connect(self.check_errors)
        self.pushButton_7.clicked.connect(self.fix_errors)
        self.pushButton_2.clicked.connect(self.prettify)
        self.pushButton_5.clicked.connect(self.minify)
        self.pushButton_3.clicked.connect(self.compress)
        self.pushButton_4.clicked.connect(self.convert_to_xml)
        self.pushButton_6.clicked.connect(self.convert_to_json)
        
        
    def check_errors(self):
        print(dfnkdf)
        
    def fix_errors(self):
        print(dkfjn)
        
    def prettify(self):
        pretty_list=Pretty.pretty_xml(self.file_path)
        for i in pretty_list:
            self.plainTextEdit.appendPlainText(str(i))
        
    def minify(self):
        minify_list=minifying.minifying_file(self.file_path)
        for i in minify_list:
            self.plainTextEdit.appendPlainText(str(i))
        
    def compress(self):
        print(kfjnsdk)
    def convert_to_xml(self):
        print(fdjn)
    def convert_to_json(self):
        print(fkjk)
        
       
        
        
        
        
        
        
        
        
        
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
widget.addWidget(login())
widget.show()
app.exec_()