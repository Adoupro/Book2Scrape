"""_summary_

Returns:
    _type_: _description_
"""

import pandas as pd


class LoadProcedure(object):
    """_summary_

    Args:
        object (_type_): _description_
    """

    def book_loading(self, book_information: dict, path) -> None:
        """_summary_

        Args:
            book_information (dict): _description_

        Returns:
            None
        """
        columns = {
            "UPC": "universal_ product_code",
            "Product Type": "",
            "Price (excl. tax)": "price_excluding_tax",
            "Price (incl. tax)": "price_including_tax",
            "Tax": "",
            "Availability": "number_available",
            "url": "product_page_url",
            "category": "category",
            "rating": "review_rating",
            "title": "title",
            "image": "image_url",
            "description": "product_description"
        }
        
        del book_information['Product Type']
        del book_information['Tax']
        del book_information['Number of reviews']

        dataframe: pd.DataFrame = pd.DataFrame(book_information)
        dataframe = dataframe.rename(columns=columns)
        dataframe.to_csv(path, index=False, sep=';')
