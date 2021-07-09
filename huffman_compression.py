# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 15:28:50 2021

@author: dinaa
"""

class node(object):
    """Huffman tree nodes implementation."""
    def __init__(self,value = None, left = None, right = None, parent = None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

class Compression():
    """Class that implements Huffman's Algorithm for compressing files."""
    def createTree(self,nodes_list):
        nodes_list.sort(key=lambda x: x.value)   # We need to sort the nodes in ascending order first
        if len(nodes_list)==1:
            return nodes_list[0]       
        parent_node = node(nodes_list[0].value+nodes_list[1].value,nodes_list[0],nodes_list[1]) 
        nodes_list[0].parent = nodes_list[1].parent = parent_node
        nodes_list.pop(0)
        nodes_list.pop(0)
        nodes_list.insert(0,parent_node)   # We delete the two smallest nodes and add the parent node
        return (self.createTree(nodes_list)) # Recursively call itself

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
        """Method that encodes the input files."""

        with open(input_file,'rb') as file:
            file.seek(0, 2)        
            size = file.tell()
            file.seek(0)
            bytes_list=[0]*size  # Storing read bytes
    
            i=0
            while i<size:
                # Read 1 symbol
                bytes_list[i]=file.read(1) 
                i = i + 1

        count = {}  # Dict to count the number of occurrences of each character
        for x in bytes_list:
            if x not in count.keys():
                count[x] = 0
            count[x] += 1
    
        node_dict={}  
        for j in count.keys():
            node_dict[j] = node(count[j])  
    
        nodes=[]      # List of nodes used to build the Huffman tree 
        for x in node_dict.keys():
            nodes.append(node_dict[x])
    
        root = self.createTree(nodes)  
    
        bytes_dict={}
        for x in node_dict.keys():
            bytes_dict[x]=self.encodeNode(node_dict[x]) # Encoding leaf nodes
    
        path = input_file.split('.')
        file_name = input_file.split('/')[-1]

        with open(path[0]+'.gz','wb') as object:
            object.write((file_name+'\n').encode(encoding='UTF-8'))
            n = len(count.keys())
            object.write(int.to_bytes(n ,2 ,byteorder = 'big'))

            #First calculate the number of bytes occupied by the maximum frequency
            max_freq_count =0
            for j in count.keys():
                if max_freq_count<count[j]:
                    max_freq_count = count[j]
            width=1
            if max_freq_count>255:
                width = 2
                if max_freq_count>65535:
                    width = 3
                    if max_freq_count>16777215:
                        width = 4
            
            object.write(int.to_bytes(width,1,byteorder='big'))
    
            for j in count.keys():
                object.write(j)
                object.write(int.to_bytes(count[j], width, byteorder = 'big'))
    
            code = b''   
            for j in bytes_list:
                code += bytes_dict[j]
                out=0
                while len(code)>=8:
                    for s in range(8):
                        out = out << 1
                        if code[s] == 49:    
                            #ASCII code of  1 is 49
                            out = out | 1
                    object.write(int.to_bytes(out,1,byteorder = 'big'))
                    out = 0
                    code = code[8:]

            #Processing any data that is less than one byte
            object.write(int.to_bytes(len(code), 1, byteorder = 'big')) 
            out = 0
            for i in range(len(code)):
                out = out << 1
                if code[i] == 49:
                    out = out | 1
            object.write(int.to_bytes(out,1,byteorder='big'))
            
    def extractFile(self,input_file):
        """Method that decodes/extracts .gz files."""
        with open(input_file,'rb') as in_file:
    
            in_file.seek(0,2)
            # Reading the length of the file
            length = in_file.tell() 
            in_file.seek(0)
            path = input_file.split('.')
            file_name = in_file.readline().decode(encoding="UTF-8").split('/')[-1].replace('\n','')
            file_name = file_name.split('.')[-1]        

            with open(path[0]+'.'+ file_name,'wb') as f_out:
                n=int.from_bytes(in_file.read(2), byteorder = 'big')     
                width=int.from_bytes(in_file.read(1), byteorder = 'big') 
                count = {}
                i = 0

                while i<n:
                    dict_key = in_file.read(1)
                    dict_value = int.from_bytes(in_file.read(width), byteorder = 'big')
                    count[dict_key]=dict_value
                    i = i + 1
    
                node_dict = {}  
                for j in count.keys():
                    node_dict[j] = node(count[j])  

                nodes = []  
                for x in node_dict.keys():
                    nodes.append(node_dict[x])

                # Building the huffman tree
                root = self.createTree(nodes)
                bytes_dict = {}
                for x in node_dict.keys():
                    bytes_dict[x] = self.encodeNode(node_dict[x])
    
                diff_dict={}
                for x in bytes_dict.keys():
                    diff_dict[bytes_dict[x]]=x

                # Traversing the tree until we find the leaf node
                out = b''
                i = in_file.tell()
                node_now = root
                output = b''
                while i < length-2:
                    i+=1
                    temp = int.from_bytes(in_file.read(1),byteorder = 'big')
                    for mm in range(8):       
                        if temp&1 == 1:
                            out=b'1'+out
                        else:
                            out=b'0'+out
                        temp=temp>>1
    
                    while out:      
                        if out[0]==49:
                            node_now = node_now.right
                            output = output + b'1'
                        if out[0] == 48:
                            node_now = node_now.left
                            output = output +b'0'
                        out = out[1:]
                        if (node_now.left == None) and (node_now.right==None):
                            f_out.write(diff_dict[output])
                            output = b''
                            node_now=root
    
                # Processing the final data that may be less than 8 bits
                final_length = int.from_bytes(in_file.read(1), byteorder='big')
                temp = int.from_bytes(in_file.read(1), byteorder='big')

                for mm in range(final_length):  
                    if temp & 1 == 1:
                        out = b'1' + out
                    else:
                        out = b'0' + out
                    temp = temp >> 1

                while out:  
                    if out[0] == 49:
                        node_now = node_now.right
                        output = output + b'1'
                    if out[0] == 48:
                        node_now = node_now.left
                        output = output + b'0'
                    out = out[1:]
                    if node_now.left == None and node_now.right == None:
                        f_out.write(diff_dict[output])
                        output = b''
                        node_now = root
        

        
#Compression().compressFile("example_1.json")
