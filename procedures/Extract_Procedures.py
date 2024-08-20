from urllib.request import urlopen
from bs4 import BeautifulSoup
import math


class ExtractProcedure(object):
    """
    A class for extracting information from URLs related to categories and books.

    Args:
        object (type): Base class for all classes in Python

    Methods:
        categories_extraction(url: str) -> dict: Extracts categories from a given URL and returns them as a dictionary.
        books_urls_extraction(url: str) -> dict: Extracts the URLs of books from a given category page URL.
        book_extraction(category: str, url: str) -> dict: Extracts book information from a given URL.

    Note:
        This class requires the 'urlopen' and 'BeautifulSoup' modules from urllib.request and bs4 respectively.
    """

    def categories_extraction(self, url: str) -> dict:
        """
        Extracts categories from a given URL and returns them as a dictionary.

        Args:
            url (str): The URL from which categories will be extracted.

        Returns:
            dict: A dictionary containing category names as keys and category URLs as values.
        """
        connection: bytes = urlopen(url).read()

        if connection is not None:
            soup = BeautifulSoup(connection, features="html.parser")
            categories = soup.find('div', {"class": "side_categories"})
            categories_list = [(category.text.strip(), category['href']) for category in categories.find_all("a")[1:]]
            return dict(categories_list)


    def books_urls_extraction(self, url: str) -> dict:
        """
        Extracts the URLs of books from a given category page URL.

        Args:
            url (str): The URL of the category page from which to extract book URLs.

        Returns:
            dict: A list of URLs of books found on the category page.
        """
        url = url.removesuffix('index.html')
        connection: bytes = urlopen(url).read()

        if connection is not None:
            soup = BeautifulSoup(connection, features="html.parser")

            nb_result = soup.find('form', {'class': 'form-horizontal'}).find('strong').text
            nb_result = int(nb_result)
            nb_result = math.ceil(nb_result / 20)

            urls: list = []

            for page in range(nb_result):
                page += 1

                if page > 1:
                    page = str(page)
                    page_url: str = f"{url}page-{page}.html"
                else:
                    page_url: str = url

                connection: bytes = urlopen(page_url).read()
                if connection is not None:
                    soup: BeautifulSoup = BeautifulSoup(connection, features="html.parser")
                    urls = urls + [book.find('a')['href'] for book in soup.find_all('article', {'class': 'product_pod'})]
         
        return urls


    def book_extraction(self, category: str, url: str) -> dict:
        """Extracts book information from a given URL.

        Args:
            category (str): The category of the book.
            url (str): The URL of the webpage containing book information.

        Returns:
            dict: A dictionary containing the extracted book information which includes URL, category, and BeautifulSoup object.
        """

        connection: bytes = urlopen(url).read()
        if connection is not None:
            return {'url': url, 'category': category, 'soup': BeautifulSoup(connection, "html.parser")}
