# WIKIPEDIA RECURSIVE SCAPER

## About
The script displays all the pages from 'See also' sections recursively. If you want to find the link between some nations and some *not cool* organisations, you shall use this.
Really, use it and *have some fun!*

## Requirements
* [Python3](https://www.python.org/)
* [venv](https://docs.python.org/3/library/venv.html): `pip3 install venv`

## Setup
1. Create a new virtual enviroment with `python3 -m venv /path/to/new/virtual/environment`
2. In the *venv* directory `git clone https://github.com/syrekable/dtin_web_scraper`
3. `pip install -r requirements.txt`

## Usage
* `python3 crawler.py 'https://en.wikipedia.org/wiki/path_to_the_article'`
* To kill the program, just `Ctrl+C` it.
* But really, it will die in most cases by itself.
