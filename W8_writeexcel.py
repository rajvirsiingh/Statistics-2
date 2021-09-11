import xlwt
from xlwt import Workbook

# Workbook is created
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')

sheet1.write(1, 0, 'Punjab')
sheet1.write(2, 0, 'Haryana')
sheet1.write(3, 0, 'J&K')
sheet1.write(4, 0, 'Uttrakhand')
sheet1.write(5, 0, 'Uttar Pradesh')
sheet1.write(0, 1, 'Bihar')
sheet1.write(0, 2, 'Sikkim')
sheet1.write(0, 3, 'Rajasthan')
sheet1.write(0, 4, 'Gujrat')
sheet1.write(0, 5, 'Maharashtra')

wb.save('example.xls')
