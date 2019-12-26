from openpyxl import Workbook


class Read_data:
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['考号',
                        '姓名',
                        '性别',
                        '高考成绩'])

    def process_item(self, itemx):
        linex = [itemx['id'],
                 itemx['name'],
                 itemx['sex'],
                 itemx['grade']]
        self.ws.append(linex)
        return itemx

    def __del__(self):
        self.wb.save('data.xlsx')


if __name__ == '__main__':
    process = Read_data()
    filename = 'f1.txt'

    with open(filename, 'r') as data:
        lines = data.readlines()
        for line in lines:
            item = {'id': line.split()[0],
                    'name': line.split()[1],
                    'sex': line.split()[2],
                    'grade': line.split()[3]}
            process.process_item(item)

    del process
    pass
