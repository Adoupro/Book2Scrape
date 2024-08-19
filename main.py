"""_summary_
"""

from procedures.ExtractProcedures import ExtractProcedure
from procedures.TransformProcedures import TransformProcedure
from procedures.LoadProcedures import LoadProcedure


def main():
    """_summary_
    """

    category: str = "Historical Fiction"
    url: str = "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"

    extractor: ExtractProcedure = ExtractProcedure()
    book: dict = extractor.book_extraction(category, url)

    transformater: TransformProcedure = TransformProcedure()
    book: dict = transformater.book_transform(book)

    loader: LoadProcedure = LoadProcedure()
    loader.book_loading(book, path=f"{category}.csv")

main()