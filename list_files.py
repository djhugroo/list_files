import os
import xlwt

print(os.getcwd())

directory = ("C:\\Users\\dhire\\Downloads\\CERN eLibrary")

os.chdir(directory)

print(os.getcwd())

file_name_list = []
file_ext_list = []
file_size_list =[]

for root, dirs, files in os.walk(directory):
    for file in files:
        [filename,extension] = file.rsplit('.',1)
        file_name_list.append(filename)
        file_ext_list.append(extension)
        file_size_list.append((os.stat(file).st_size)/(1024*1024) )

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('file_list')

worksheet.write(0,0,'File Name')
worksheet.write(0,1,'File Type')
worksheet.write(0,2,'File Size')

for number, name in enumerate(file_name_list):
    worksheet.write(number+1,0,name)
    worksheet.write(number+1,1,file_ext_list[number])
    worksheet.write(number+1,2,file_size_list[number])

worksheet.col(0).width = 20000 # In pixels

os.chdir("C:\\Users\\dhire\\Downloads")

workbook.save('File List.xls')