#!/bin/zsh
# -*- coding: utf8 -*-

# Created by Neil Francis Hipona on 14/1/2016.
# Copyright © 2015 NFerocious. All rights reserved.


# Parses Tides Raw Data


import csv
import os
import shutil

from datetime import datetime
from dateutil.parser import parse

# Helper
from TidesModifierScriptFunc import generatePathForDirName
from TidesModifierScriptFunc import startParsingInDirectory
from TidesModifierScriptFunc import createOutputDirectory


# Set delimiter
delimiter = ","

# Define working directories
cDir = os.getcwd()

# Define Folder names
rawDataFolderName = "Tides Data"
outputDirectoryName = ""

print "Start parsing... : " + str(datetime.now())

# Prepare for parsing ... 
print "\nParse file? [Y] or any key to exit."
parseCompletionKey = raw_input("  Command: ")

while (parseCompletionKey == "Y" or parseCompletionKey == "y" or parseCompletionKey == "N" or parseCompletionKey == "n"):

	# Get output directory name
	if parseCompletionKey == "N" or parseCompletionKey == "n" or not outputDirectoryName:
		# Reset output directory
		outputDirectoryName = ""
		
		while (not outputDirectoryName):
			outputDirectoryName = raw_input("Enter output folder name: ")
		
		createOutputDirectory(cDir, outputDirectoryName)

	# Perform parsing ...
	startParsingInDirectory(cDir, rawDataFolderName, outputDirectoryName)
	
	print "\nParse another file? [Y] Start with new directory [N] or any key to exit."
	parseCompletionKey = raw_input("  Command: ")


print "\nExit."


