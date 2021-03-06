# Simpli.fi Dynamic Language Code Challenge Solution

## Overview
This python package contains a solution to coding challenge outlined in Challenge_README.md

The application takes raw text data containing information about a user and processes them into dictionaries that can be queried by users or words.

This is accomplished using the processdata, qusers, and qwords modules found in the scripts directory. These modules also utilize functions from parsetools and dictools.

## Requirements
**Required**

* python 3.x

**Recommended**

* pip - package manager
* venv - virtual environment
* pytest - test runner

----
## Usage

    cd <challenge directory>
    $ python -m venv <path to venv>        # optional
    $ python pip install requirements.txt  # install dependcy packages

    $ python -m scripts.processdata <path to data file>
    $ python -m scripts.qwords <example word>
    $ python -m scripts.qusers <ip adress> <user agent string>


#Installation
Create and activate virtual environment:
```
$ python3 -m virtualenv env             # mac / Linux
$ py -m pip install --user virtualenv   # windows

$ source env/bin/activate               #mac / Linux
$ .\env\Scripts\activate                #windows#

$ python -m pip install requirements.txt    #necessary packages such as pytest
```

##Tests

```
$ python -m pytest [-v]
```

----
## Package References
* [urllib](https://docs.python.org/3/library/urllib.html)
* [pytest](https://docs.pytest.org/en/latest/)
* [argparse](https://docs.python.org/3/library/argparse.html)
* [pickle](https://docs.python.org/3/library/pickle.html)
* [venv](https://docs.python.org/3/library/venv.html)
 