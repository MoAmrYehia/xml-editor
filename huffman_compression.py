# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 15:28:50 2021

@author: dinaa
"""
import sys

# Changing python's default recursion depth so it won't cause us any errors while reading the files
sys.setrecursionlimit(100000)

class node(object):
    """Huffman tree nodes implementation.
    A Huffman tree is basically a min heap/binary search tree.
    value: is the code assigned to the character
    right,left, parent: are the right,left,parent of the node."""
    def __init__(self,value = None, left = None, right = None, parent = None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

class Compression():
    """Class that implements Huffman's Algorithm for compressing files."""
    def createTree(self,nodes_list):
        """Method that builds the huffman tree."""
        # First thing to do is sort the nodes in an ascending order
        nodes_list.sort(key=lambda n: n.value)
        length = len(nodes_list)   
        if (length == 1):  # This means the tree only has 1 node
            return nodes_list[0]    

        parent_node = node(nodes_list[0].value+nodes_list[1].value,nodes_list[0],nodes_list[1]) 
        nodes_list[0].parent = nodes_list[1].parent 
        nodes_list[1].parent = parent_node
        # We delete the two nodes with the smallest frequency and use their sum to create a new parent node
        nodes_list.pop(0)
        nodes_list.pop(0)
        nodes_list.insert(0,parent_node)   
        return (self.createTree(nodes_list)) # Recursively call itself until the tree is formed

    @staticmethod    
    def compress(self,file_path):
        """Interface method for the user to compress files."""
        self.compressFile(file_path)
        
    @staticmethod    
    def extract(self,file_path):
        """Interface function for the user to extract files."""
        self.extractFile(file_path)

    
    def encodeNode(self,node):            
        """Method that encodes the leaf nodes."""
        if (node.parent) == None:
            return b''
        if (node.parent.left) == node:
            return self.encodeNode(node.parent)+b'0'
        else:
            return self.encodeNode(node.parent)+b'1'
        
    def compressFile(self, input_file):
        """Method that encodes the input files using variable length prefix codes.
        The output is the encoded zip file."""

        with open(input_file,'rb') as file:
            file.seek(0, 2)        
            length = file.tell()
            file.seek(0)
            bytes_list = [0]*length  # List where we'll store the read bytes
    
            ind = 0
            while (ind<length):
                bytes_list[ind] = file.read(1) # Reading one char at a time
                ind = ind + 1

        count = {}  # Dict to count the number of occurrences of each character
        nodes_dict = {}  # dictionary that contains the nodes created out of the file characters
        nodes = []      # List of nodes used to build the Huffman tree 
        bytes_dict = {} # dictionary containing the encoded characters

        for i in bytes_list:
            if i not in count.keys():
                count[i] = 0
            count[i] = count[i] + 1
    
        for j in count.keys():
            nodes_dict[j] = node(count[j])  
    
        for x in nodes_dict.keys():
            nodes.append(nodes_dict[x])
    
        root = self.createTree(nodes)  

        for x in nodes_dict.keys():
            bytes_dict[x]=self.encodeNode(nodes_dict[x]) # Encoding the nodes
    
        path = input_file.split('.') # Input file path
        file_name = input_file.split('/')[-1] # Extracting the file's name from the given path

        with open(path[0]+'.zip','wb') as object: # Creating the .zip file
            object.write((file_name+'\n').encode(encoding='UTF-8'))
            n = len(count.keys())
            object.write(int.to_bytes(n ,2 ,byteorder = 'big'))

            #First calculate the number of bytes occupied by the maximum frequency
            max_freq_count =0
            for j in count.keys():
                if max_freq_count<count[j]:
                    max_freq_count = count[j]
            w = 1
            if max_freq_count>255:
                w = 2
                if max_freq_count>65535:
                    w = 3
                    if max_freq_count>16777215:
                        w = 4
            
            object.write(int.to_bytes(w,1,byteorder='big'))
    
            for j in count.keys():
                object.write(j)
                object.write(int.to_bytes(count[j], w, byteorder = 'big'))
    
            code = b''   # prefix code used for encoding the characters
            for j in bytes_list:
                code += bytes_dict[j]
                output = 0
                while len(code)>=8:
                    for j in range(8):
                        output = output << 1
                        if code[j] == 49:    
                            #ASCII code of  1 is 49
                            output = output | 1
                    object.write(int.to_bytes(output,1,byteorder = 'big'))
                    output = 0
                    code = code[8:]

            #Processing any data that is less than one byte
            object.write(int.to_bytes(len(code), 1, byteorder = 'big')) 
            output = 0
            for i in range(len(code)):
                output = output << 1
                if code[i] == 49:
                    output = output | 1
            object.write(int.to_bytes(output,1,byteorder='big'))
            

        

        
#Compression().compressFile("data-sample.xml")
#Compression().compressFile("example_1.json")
