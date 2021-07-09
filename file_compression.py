# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 11:59:30 2021

@author: dinaa
"""
import gzip
import shutil
class Compressor():
    """Class that compresses XML or JSON files into .gz format"""
    @staticmethod
    def compress_file(file_name):
        """Method that compress the file"""
        output_name = file_name + ".gz"
        with open(file_name, 'rb') as f_in, gzip.open(output_name, 'wb') as f_out:shutil.copyfileobj(f_in, f_out)
    
    @staticmethod       
    def read_compressed_file(file_name):
        """Method that shows the contents of the compressed file."""
        with gzip.open(file_name, 'rb') as f:
            for line in f:
                print(line.decode().strip())
                #return(line.decode().strip())
                

        
#Compressor().compress_file("example_1.json")
#Compressor.read_compressed_file("file.txt.gz")
        

