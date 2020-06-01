from bs4 import BeautifulSoup as bs
import requests
import argparse
import inspect

from typing import Union
from tree import Tree

'''Utilities for processing URL as a command-line argument'''
parser = argparse.ArgumentParser("Prints out the 'See also' sections of Wikipedia articles recursively.")
parser.add_argument('URL', help="an URL to a Wikipedia article")
args = parser.parse_args()

BASE_URL = "https://en.wikipedia.org"

def get_see_also_section(article: bs) -> Union[list, None]:
    '''returns either a list of URLs to articles mentioned in 'See Also' section or None'''
    see_also_heading = article.find(id="See_also") ## <div id="See_also">
    if see_also_heading is not None:
        for element in see_also_heading.next_elements:
            if element.name is not None and element.name == 'ul': ## looking for the first <ul> sibling
                return from_tags_to_links(element)


def from_tags_to_links(tags) -> [str, ...]:
    '''
        returns sanitized version of input list, i.e. containing only URLs to articles
        in the form "wiki/{Title_of_article}"
    '''
    return [tag.get('href') for tag in tags.find_all('a')]


def say_my_name(url: str) -> str: ##Heisenberg!
    return url.replace(BASE_URL, '')


def main(root: Union[Tree, None], url: str):
    ##make a request, get a website from it, get the 'See also' section,
    ##make a tree object with name being the url, and adjacent nodes being
    ##articles from 'See also' section. 
    

    ##TODO: eliminate the ocurring cycle; use the Trie.existing_nodes static attribute
    url = say_my_name(url)
    if url in Tree.existing_nodes:
        return None

    r = requests.get(BASE_URL+url)
    soup = bs(r.text, 'lxml')
    Tree.mark_visited(url)
    see_also = get_see_also_section(soup)

    if see_also is None: ##it dies somehow 
        return Tree(say_my_name(url), see_also)
 
    if root is None:
        root = Tree(say_my_name(args.URL), get_see_also_section(soup))

    print(url)
    for url in see_also:
        branch = main(root, url)
        if branch is None:
            continue
        root.add_node(branch)
    
    return root

if __name__ == "__main__":
    root = main(None, args.URL)
    root.print_nodes()
    
