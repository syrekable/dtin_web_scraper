from bs4 import BeautifulSoup as bs
import requests
import argparse
from typing import Union

'''Utilities for processing URL as a command-line argument'''
parser = argparse.ArgumentParser("Prints out the 'See also' sections of Wikipedia articles recursively.")
parser.add_argument('URL', help="an URL to a Wikipedia article")
args = parser.parse_args()

r = requests.get(args.URL)
soup = bs(r.text, 'lxml')

MAIN_URL = "en.wikipedia.org"

def get_see_also_section(article: bs) -> Union[list, None]:
    '''returns either a list of URLs to articles mentioned in 'See Also' section or None'''
    see_also_heading = article.find(id="See_also")
    urls = []
    if see_also_heading is not None:
        for element in see_also_heading.next_elements:
            if element.name is not None and element.name == 'ul':
                urls = from_tags_to_links(element)
                return urls

def from_tags_to_links(tags) -> [str, ...]:
    '''returns sanitized version of input list, i.e. containing only URLs to articles'''
    return [tag.get('href') for tag in tags.find_all('a')]
