"""_summary_

Returns:
    _type_: _description_
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup


class ExtractProcedure(object):
    """_summary_

    Args:
        object (_type_): _description_
    """

    def book_extraction(self, category: str, url: str) -> dict:
        """_summary_

        Args:
            url (str): _description_

        Returns:
            dict: _description_
        """

        connection: bytes = urlopen(url).read()
        if connection is not None:
            return {'url': url, 'category': category, 'soup': BeautifulSoup(connection, "html.parser")}
