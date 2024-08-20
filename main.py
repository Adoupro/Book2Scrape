"""_summary_
"""

import pandas as pd
from procedures.Extract_Procedures import ExtractProcedure
from procedures.Transform_Procedures import TransformProcedure
from procedures.Load_Procedures import LoadProcedure


def main():
    """_summary_
    """

    extractor: ExtractProcedure = ExtractProcedure()

    root_url: str = "https://books.toscrape.com/"
    categories: dict = extractor.categories_extraction(root_url)
    all_categories: dict = {}

    for category, url in categories.items():
        all_categories[category] = extractor.books_urls_extraction(url=f"{root_url}{url}")

    dataframe: pd.DataFrame = pd.DataFrame()

    for category, urls in all_categories.items():
        sub_dataframe: pd.DataFrame = pd.DataFrame({"url": urls})
        sub_dataframe['category'] = category
        dataframe = pd.concat([dataframe, sub_dataframe], axis=0)

    dataframe['url'] = dataframe['url'].replace('../../../', f"{root_url}catalogue/", regex=True)

    all_books: list = []
    transformater: TransformProcedure = TransformProcedure()

    loader: LoadProcedure = LoadProcedure()
    category: str = dataframe['category'].iloc[0]

    for i, row in dataframe.iterrows():
        book: dict = extractor.book_extraction(row.category, row.url)
        book: dict = transformater.book_transform(book)
        all_books.append(book)

        if row.category != category:
            loader.book_loading(root_url=root_url, book_information=all_books, path=f"data/{category}.csv")
            category = row.category
            all_books: list = []


main()
