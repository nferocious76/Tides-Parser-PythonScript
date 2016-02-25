#!/bin/zsh
# -*- coding: utf8 -*-

# Created by Neil Francis Hipona on 14/1/2016.
# Copyright © 2015 NFerocious. All rights reserved.


# Parses Tides Raw Data
# Function Collections


import csv
import os
import shutil

from datetime import datetime, timedelta
from dateutil.parser import parse


# Create output directory
def createOutputDirectory(cDir, folderName):
	# Create output directory
	directoryPath = generatePathForDirName(cDir, folderName)

	if os.path.exists(directoryPath):
		print "\n Output directory already exist at path: '" + directoryPath + "'"
	else:
		# Create output directory
		print "\nCreating output directory"
		os.mkdir(folderName)	


# Remove file at path 'filePath'
def removeFileAtPath(filePath):
	if os.path.exists(filePath):
		os.remove(filePath)
		print "\nRemoved file at '" + filePath + "'"


# Remove file at path 'filePath'
def removeDirectoryAtPath(dirPath):
	if os.path.exists(dirPath):
		shutil.rmtree(dirPath)
		print "\nRemoved file at '" + dirPath + "'"


# Create directory path for file
def generatePathForFileInDirectory(cDir, folder, fileName):
	newPath = cDir + "/" + folder + "/" + fileName
	return newPath


# Create directory path
def generatePathForDirName(cDir, folder):
	newPath = cDir + "/" + folder
	return newPath


# Check input if is number
def isNumber(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


# Get user input for hours modifier
def getHoursTimeValueModifier():
	hoursValue = raw_input("Enter hour(s) modifier: ")

	while (isNumber(hoursValue) == False):
		print "\nWrong input! Please input a number!"
		hoursValue = raw_input("\nEnter hour(s) modifier: ")

	return int(hoursValue)


# Get user input for minutes modifier
def getMinutesTimeValueModifier():
	minutesValue = raw_input("Enter minute(s) modifier: ")

	while (isNumber(minutesValue) == False):
		print "\nWrong input! Please input a number!"
		minutesValue = raw_input("\nEnter minute(s) modifier: ")

	return int(minutesValue)


# Get user input for tide level modifier
def getTideHeightValueModifier():
	heightValue = raw_input("Enter height modifier: ")

	while (isNumber(heightValue) == False):
		print "\nWrong input! Please input a number!"
		heightValue = raw_input("\nEnter height modifier: ")

	return float(heightValue)


# Parse file at path with input filename
def startParsingInDirectory(cDir, folder, outputFolder):
	print "\nGet raw file filename"

	# Open file to parse
	fileToParse = raw_input("Enter file name: ")
	fileToParsePath = generatePathForFileInDirectory(cDir, folder, fileToParse)

	# Validate file to parse
	while (os.path.exists(fileToParsePath) == False):
		print "\nFile with filename '" + fileToParse + "' does not exist at path: '" + fileToParsePath + "'"
		fileToParse = raw_input("\nEnter file name: ")
		fileToParsePath = generatePathForFileInDirectory(cDir, folder, fileToParse)

	outputFileName = fileToParse # "Modified-" + 

	print "\n"
	# Get time value modifier
	hoursValue = getHoursTimeValueModifier() # int
	minutesValue = getMinutesTimeValueModifier() # int
	heightValue = getTideHeightValueModifier() # float
	totalHoursValue = hoursValue + (float(minutesValue) / 60)

	print "\n Modifier --- " + str(hoursValue) + ":" + str(minutesValue) + ", " + str(heightValue)

	# Create time modifier
	timeModifier = timedelta(hours=totalHoursValue)
	print "\nTime Modifier: " + str(timeModifier)

	# Read raw data
	tidesRawData = open(fileToParsePath, "r")

	# Create reader
	plainText = csv.reader(tidesRawData)

	# Proceed on saving parsed data
	saveFileToDirectory(cDir, outputFolder, outputFileName, plainText, timeModifier, heightValue)


# Save function
def saveFileToDirectory(cDir, outputFolder, outputFileName, plainText, timeModifier, heightValue):

	# Generate output path
	fileOutputPath = generatePathForFileInDirectory(cDir, outputFolder, outputFileName)

	# Remove existing file at path
	removeFileAtPath(fileOutputPath)

	# Open text file
	textFile = open(fileOutputPath, "w+")

	# Parse through
	for inLineData in plainText:
		date = inLineData[0]
		time = inLineData[1]
		tideLevel = inLineData[2]

		# Combine date and time
		dateWithTime = date + " " + time
		dateObject = parse(dateWithTime)

		# Create new date with modifier
		newDateObject = dateObject + timeModifier

		# Define new values
		dateString = newDateObject.strftime('%d-%b-%Y')
		timeString = newDateObject.strftime('%H:%M')
		newTideLevel = float(tideLevel) + heightValue

		print "\n"
		print dateObject
		print newDateObject
		print "Date: " + date + " Time: " + time + " Level: " + tideLevel
		print "NewDate: " + dateString + " Time: " + timeString + " Level: " + str(newTideLevel)

		stringToWrite = dateString + "," + timeString + "," + str(newTideLevel)

		textFile.write(stringToWrite + "\n")

	# Close session
	textFile.close()
	print "\nDone parsing ..."











