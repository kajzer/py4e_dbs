# Python scripts

Creating scripts to exercise python code.  
*Made on basis of py4e.com, Udacity, python notes for professionals, automate the borring stuff with python*

## Get data from my API and parse them
Link: **[get data from API](./get_data_from_api)**  
**Used:** JSON, Python, Heroku, [build by me Rails API](https://github.com/kajzer/school_api)  
Runs get request to my Rails API deployed on heroku and parses response and creates Student objects. All namespaced in a class.

## Counting emails
Link: **[counting_emails_db](./counting_emails_db)**  
**Used:** SQL, txt file parsing  
run db_connect.py - connect to db. Parse file for emails (press enter if no file, there is a fall back). The script will add domain names of emails to db.

## Many to many relational db
Link: **[many_to_many](./many_to_many)**  
**Used:** SQL, JSON  
script will parse json format and setup many to many db with courses and attendees with parsed data  

## Hangman Game
Link: **[Hangman Game](./hangman)**  
**Used:** random, requests, urllib, json, string  
Game of hangman with a random word taken from an API.

## Excel file handling
Link: **[excel automation](./excel_automation)**  
**Used:** openpyxl, pprint  
Script to automate *xlsx files. Requires OpenPyXL (pip3 install openpyxl)  
xlsx_repo.py - opening, getting sheets, traversing, etc.    
read_data_from_xlsx.py - read from the census spreadsheet file and calculate statistics for each county  

## Itunes tracks parser
Link: **[tracks](./tracks)**  
**Used:** SQL, XML  
application will read an iTunes export file in XML and produce a properly normalized database

## PDFs handling
Link: **[pdf_combine](./pdf_combine)**  
**Used:** PyPDF2, os, glob  
Combine pages without cover page from many *.pdf files into a single *.pdf  
Requires PyPDF2: sudo pip3 install PyPDF2

## Linked list
Link: **[linked_list](./linked_list)**  
linked list implementation in python

## Iterable
Link: **[iterable](./iterable)**  
build a Basic Python Iterator

## Fibonacci sequence generator
Link: **[Fibonacci generator](./fibonacci_generator)**   
generate first n numbers from Fibonacci series. Can be run as executable ./fibonacci_generator.py [#_of_numbers_in_sequance]. Uses sys.argv with try except block for validation and checking input errors. 

## Quiz generator
Link: **[quiz generator](./quiz_generator)**  
**Used:** file handling  
Generating different quizzes with multiple choice questions.

## Twilio API
Link: **[send_sms](./send_sms)**  
**Used:** Twilio API  
Sending sms with twilio API - for this to work script needs valid credentails

## Google maps from console
Link: **[map it](./mapit)**  
Opens google maps to specified location from command line arguments  
Usage example: ./mapit.py 870 Valencia St, San Francisco, CA94110
Need to install: pip install pyperclip

## Get weather from command line
Link: **[get weather](./get_weather)**  
**Used:** json, requests, sys, urllib  
Gets weather from openweathermap (only sample) for current location provided in command line arguments (needs API key - in this form always gets London)  
Usage: python3 get_weather.py London

## Check profanity in txt file
Link: **[profanity_checker](./profanity_checker)**  
**Used:** url encode  
Simple script to read from a txt file and hit url with contents to check if text contains curse words.

## Console logging
Link: **[logging_to_consoe](./logging_to_console)**   
Logging every step of factorial to console

## Copy passwords to clipboard
Link: **[passwords_copy](./passwords_copy)**  
Insecure password holder. Will copy to clipboard password for given account. Usage: ./pw.py [some_account]. To run as executable permissions are required: sudo chmod +x pw.py  

## Pomodoro and file rernaming
Link: **[pomodoro_rename_files](./pomodoro_rename_files)**  
  break_time.py - simple program to wait and open up a browser with provided link  
  rename_photos.py - script to rename files - remove numbers from the beggining of a file name
