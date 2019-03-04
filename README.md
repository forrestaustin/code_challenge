# Simpli.fi Dynamic Language Code Challenge - Forrest

## Overview
This python package is the solution to coding challenge outlined in Challenge_README.md

This application takes raw text data containing information about a user and creates dictionaries that can be queried by either user or words found from their urls.

The three main functions are accomplished using the processdata, qusers, and qwords modules found in the scripts directory. These modules also utilize functions from parsetools and dictools.

The data folder contains raw text data for processing as well as binary dictionary files (.pickle)


#Installation
Create and activate virtual environment:
```
$ python3 -m virtualenv env             # mac / Linux
$ py -m pip install --user virtualenv   # windows

$ source env/bin/activate               #mac / Linux
$ .\env\Scripts\activate                #windows#

$ python -m pip install requirements.txt    #necessary packages such as pytest
```


#Usage

```
$ cd into project root directory
$ python -m scripts.processdata                     # creates dictionaries using default parsed_data.txt
$ python -m scripts.processdata different_data.txt  # creates dictionaries using different_data.txt
$ python -m scripts.qwords Miami # returns list of user tuples that have urls containing "Miami" 
$ python -m scripts.qwusers "(192.168.1.1, uastring)" # returns list of words found for user (must use "")

```

##Tests

```
$ python -m pytest [-v]     #v is option paramter for more details
```