# -*- coding: utf-8 -*-
"""
Created on Sun Jul  11 15:28:50 2021
@author: dinaa
"""
import sys

# Changing python's default recursion depth so it won't cause us any errors while reading the files
sys.setrecursionlimit(100000000)

class node():
    """Huffman tree nodes implementation.
    A Huffman tree is basically a priority queue/binary search tree.
    value: is the code assigned to the character
    right,left, parent: are the right,left,parent of the node."""
    def __init__(self,value = None, left = None, right = None, parent = None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

class Compression():
    """Class that implements Huffman's Algorithm for compressing files."""
    def createTree(self, nodes):
        # First thing to do is sort the nodes in an ascending order
        nodes.sort(key=lambda x: x.value)

        # Recursion stopping condition
        if len(nodes)==1:
            return nodes[0]    

        # Merging leaf nodes into one node
        left = nodes[0]
        right = nodes[1]
        value = left.value + right.value
        new_node = node(value, left, right)

        # We delete the two nodes with the smallest frequency and use their sum to create a new parent node
        nodes[0].parent = nodes[1].parent = new_node
        nodes.pop(0)
        nodes.pop(0)
        nodes.insert(0, new_node)   
        return (self.createTree(nodes)) # Recursively call itself

    @staticmethod    
    def compress(self,file_path):
        """Interface method for the user to compress files."""
        self.compressFile(file_path)

    @staticmethod    
    def extract(self,file_path):
        """Interface function for the user to extract files."""
        self.extractFile(file_path)


    def encodeNode(self, node):            
        """Method that encodes the leaf nodes."""
        code = b''
        if (node.parent) == None:
            return code 
        elif (node.parent.left) == node:
            return self.encodeNode(node.parent)+b'0'
        else:
            return self.encodeNode(node.parent)+b'1'

    def createDicts(self, bytes_list):
        """Method that creates necessary dictionaries that will be used to do the encoding"""
        count = {}  # Dict to count the number of occurrences of each character
        nodes_dict = {}  # dictionary that contains the nodes created out of the file characters
        nodes = []      # List of nodes used to build the Huffman tree 
        for i in bytes_list:
            if i not in count.keys():
                count[i] = 0
            count[i] = count[i] + 1
    
        for j in count.keys():
            nodes_dict[j] = node(count[j])  
    
        for x in nodes_dict.keys():
            nodes.append(nodes_dict[x])
        return bytes_list, count, nodes_dict, nodes

    def maxFreq(self, count):
        max_freq_count = 0
        for j in count.keys():
            if max_freq_count<count[j]:
                max_freq_count = count[j]
        w = 1 # width
        one_byte = 255
        two_bytes = 257 * one_byte
        three_bytes = 65793 * one_byte

        if max_freq_count > one_byte:
            w = 2
        elif max_freq_count > two_bytes:
            w = 3
        elif max_freq_count > three_bytes:
            w = 4 
        return w, max_freq_count
        
    def compressFile(self, input_file):
        """Method that encodes the input files using variable length prefix codes.
        The output is the encoded zip file."""

        bytes_dict = {} # dictionary containing the encoded characters

        with open(input_file,'rb') as file:
            file.seek(0, 2)        
            length = file.tell()
            file.seek(0)
            bytes_list = [0]*length  # List where we'll store the read bytes
    
            ind = 0
            while (True):
                if(ind<length):
                    bytes_list[ind] = file.read(1) # Reading one char at a time
                    ind = ind + 1
                else:
                    break
        bytes_list, count, nodes_dict, nodes = self.createDicts(bytes_list)

        root = self.createTree(nodes)  

        for x in nodes_dict.keys():
            bytes_dict[x]=self.encodeNode(nodes_dict[x]) # Encoding the nodes
    
        path = input_file.split('.') # Input file path
        file_name = input_file.split('/')[-1] # Extracting the file's name from the given path

        with open(path[0]+'.bin','wb') as object: # Creating the .zip file
            try:
                object.write((file_name+'\n').encode(encoding='UTF-8'))
            except OverflowError as err:
                pass
            n = len(count.keys())
            object.write(int.to_bytes(n ,2 ,byteorder = 'big'))

            #First calculate the number of bytes occupied by the maximum frequency
            w, max_freq_count = self.maxFreq(count)

            object.write(int.to_bytes(w,1,byteorder='big'))
    
            for j in count.keys():
                object.write(j)
                try:
                    object.write(int.to_bytes(count[j], w, byteorder = 'big'))
                except OverflowError as err:
                    pass
    
            code = b''   # prefix code used for encoding the character

            for byte in bytes_list:
                code = code + bytes_dict[byte]
                output = 0
                while(True):
                        if len(code)>=8:
                            for byte in range(8):
                                output = output << 1
                                if code[byte] == 49:    
                                    #ASCII code of  1 is 49
                                    output = output | 1
                            object.write(int.to_bytes(output,1,byteorder = 'big'))
                            output = 0
                            code = code[8:]
                        else:
                            break

            #Processing any data that is less than one byte
            object.write(int.to_bytes(len(code), 1, byteorder = 'big')) 
            output = 0
            for i in range(len(code)):
                output = output << 1
                if code[i] == 49:
                    output = output | 1
            object.write(int.to_bytes(output,1,byteorder='big'))


#Compression().compressFile("sample2.json") 
#Compression().compressFile("sample-data.xml") 
#Compression().compressFile("data.xml") 
