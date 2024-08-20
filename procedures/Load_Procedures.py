"""_summary_

Returns:
    _type_: _description_
"""

from urllib.request import urlretrieve
import pandas as pd


class LoadProcedure(object):
    """_summary_

    Args:
        object (_type_): _description_
    """

    def book_loading(self, root_url: str, book_information: dict, path: str) -> None:
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

        dataframe: pd.DataFrame = pd.DataFrame.from_records(book_information)
        dataframe = dataframe.rename(columns=columns)
        dataframe['image_url'] = dataframe['image_url'].replace('\.\./\.\./', f"{root_url}", regex=True)
        dataframe['image_url'].apply(lambda x: urlretrieve(x, f'images/{x.split('/')[-1]}'))

        dataframe.to_csv(path, index=False, sep=';')
