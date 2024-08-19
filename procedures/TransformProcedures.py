"""_summary_

Returns:
    _type_: _description_
"""

import re
from bs4 import BeautifulSoup


class TransformProcedure(object):
    """_summary_

    Args:
        object (_type_): _description_
    """

    def book_transform(self, book: dict) -> dict:
        """_summary_

        Args:
            book (dict): _description_

        Returns:
            dict: _description_
        """
        
        information_dict = {}
        
        # Get main informations
        information_dict['url'] = [book['url']]
        information_dict['category'] = [book['category']]
        
        # Get information table
        information: BeautifulSoup = book['soup'].find("table", {"class": "table table-striped"})
        keys: list = [row.find('th').text for row in information.find_all('tr')]
        values: list = [[row.find('td').text] for row in information.find_all('tr')]

        table: dict = dict(zip(keys, values))
        information_dict = table | information_dict
        
        information: BeautifulSoup = book['soup'].find("div", {"class": "col-sm-6 product_main"})

        # Get rating
        rating: str = information.find('p', {"class": re.compile(r'^star')})['class'][-1]
        information_dict['rating'] = [rating]
        
        # Get image and title
        information: BeautifulSoup = book['soup'].find("img")
        information_dict['title'] = [information['alt']]
        information_dict['image'] = [information['src']]
        
        # Get description
        information: BeautifulSoup = book['soup'].find('p', {'class': None})
        information_dict['description'] = [information.text]
        
        return information_dict
