import os
from xlrd import open_workbook
proDir = os.path.split(os.path.realpath(__file__))[0]
def get_xls(xls_name, sheet_name):
    """
    get interface data from xls file
    :return:
    """
    cls = []
    # get xls file's path
    xlsPath = os.path.join(proDir, "testFile", 'case', xls_name)
    # open xls file
    file = open_workbook(xlsPath)
    # get sheet by name
    sheet = file.sheet_by_name(sheet_name)
    # get one sheet's rows
    nrows = sheet.nrows
    for i in range(nrows):
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
    return cls
# with open(r'C:\Users\Administrator\Desktop\文件\新建文本文档.txt',encoding='utf-8') as f:
#     print(f.read())
#     # f.write('alskdjflsakdjflksadjf')
#
