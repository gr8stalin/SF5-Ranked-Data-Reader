import openpyxl


def read_ranked_data_workbook():
    ranked_data_workbook = openpyxl.load_workbook("/home/gr8stalin/Documents/jiveGrind.xlsx")
    sheets = [x for x in ranked_data_workbook.sheetnames if "New" not in x]
    print(sheets)


if __name__ == '__main__':
    read_ranked_data_workbook()
