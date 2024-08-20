"""_summary_

Returns:
    _type_: _description_
"""

import re
from bs4 import BeautifulSoup


class TransformProcedure(object):
    """TransformProcedure class for processing book data.

    Args:
        object (type): Parent class.
    """

    def book_transform(self, book: dict) -> dict:
        """Transforms book data into a structured dictionary.

        Args:
            book (dict): A dictionary containing book information.

        Returns:
            dict: A structured dictionary with book information.
        """

        information_dict: dict = {}

        # Get main informations
        information_dict['url'] = book['url']
        information_dict['category'] = book['category']

        # Get information table
        information: BeautifulSoup = book['soup'].find("table", {"class": "table table-striped"})
        keys: list = [row.find('th').text for row in information.find_all('tr')]
        values: list = [row.find('td').text for row in information.find_all('tr')]

        table: dict = dict(zip(keys, values))
        information_dict = table | information_dict

        information: BeautifulSoup = book['soup'].find("div", {"class": "col-sm-6 product_main"})

        # Get rating
        rating: str = information.find('p', {"class": re.compile(r'^star')})['class'][-1]
        information_dict['rating'] = rating

        # Get image and title
        information: BeautifulSoup = book['soup'].find("img")
        information_dict['title'] = information['alt']
        information_dict['image'] = information['src']

        # Get description
        information: BeautifulSoup = book['soup'].find('p', {'class': None})
        if information is not None:
            information_dict['description'] = information.text
        else:
            information_dict['description'] = ""

        # Delete useless informations
        del information_dict['Product Type']
        del information_dict['Tax']
        del information_dict['Number of reviews']

        return information_dict
