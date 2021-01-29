#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@autor miguelms.es
"""
import sys
import os
import requests

directory = "D:\\2005"

def main():
    # first of all, get al files recursively
    all_files = []
    for filename in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, filename)):
            # decode special characters in spanish
            folder = os.path.join(directory, filename).decode("cp1252")
            temp_files = recursive_get_files(folder)
            print "Dir: {}, files {}".format(folder.encode("utf-8"), len(temp_files))
            all_files += temp_files
    
#    for item in all_files:
#        print item

def recursive_get_files(location):
    file_list = []
    if (os.path.isdir(location)):
        print "\t {}".format(location.encode("utf-8"))
        for item in os.listdir(location):
            if (os.path.isdir(os.path.join(location, item))):
                file_list += recursive_get_files(os.path.join(location, item)) # concat returned list with parent one
            else:
                addItem(file_list, os.path.join(location, item))
    else:
        addItem(file_list, location)
    return file_list

# function to filter the 
def addItem(file_list, item):
    allowed_files = [ "jpg", "png", "jpeg", "avi", "mp4", "mpeg", "mov" ""]
    if not item.endswith('.db') and not item.endswith(".zip") and not item.endswith(".pdf"):
        file_list.append(item)

main()