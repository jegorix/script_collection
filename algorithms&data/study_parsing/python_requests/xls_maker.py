import xlsxwriter
from main import make_collection

def writer(collection):
    book = xlsxwriter.Workbook(r"/Users/macbook/PycharmProjects/scripts_edu/algorithms&data/study_parsing/python_requests/static/data.xlsx")
    page = book.add_worksheet("Product")

    row = 0
    column = 0

    page.set_column("A:A", 20)
    page.set_column("B:B", 20)
    page.set_column("C:C", 50)
    page.set_column("D:D", 50)

    for item in collection():
        page.write(row, column, item[0])
        page.write(row, column + 1, item[1])
        page.write(row, column + 2, item[2])
        page.write(row, column + 3, item[3])
        row += 1

    book.close()


if __name__ == "__main__":
    writer(make_collection)
