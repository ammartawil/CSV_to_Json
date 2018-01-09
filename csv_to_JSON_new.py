# -*- coding: utf-8 -*-
# reads a file "enemy arrays data" containing the levels data
# and outputs a file "out_new.txt" containing the JSON array.

import csv

def ConvertCSVToJSON():
    Array1=[]
    Array2=[]
    Array3=[]
    Array4=[]
    AirArray=[]
    with open('enemy arrays data.csv', 'r') as in_file:
        in_file.readline()
        in_file.readline()
        fin = csv.reader(in_file)

        for level in range(0 , 10):
            Array1.append([])
            Array2.append([])
            Array3.append([])
            Array4.append([])
            AirArray.append([])
            for wave in range(0 , 10):
                Array1[level].append([])
                Array2[level].append([])
                Array3[level].append([])
                Array4[level].append([])
                AirArray[level].append([])
                for enemy in range(0 , 10):
                    row = next(fin)
                    # throw a way the first 3 elements
                    row.pop(0)
                    row.pop(0)
                    row.pop(0)
                    Array1[level][wave].append("\"{};{}\"".format(row.pop(0),row.pop(0)))
                    Array2[level][wave].append("\"{};{}\"".format(row.pop(0),row.pop(0)))
                    Array3[level][wave].append("\"{};{}\"".format(row.pop(0),row.pop(0)))
                    Array4[level][wave].append("\"{};{}\"".format(row.pop(0),row.pop(0)))
                    AirArray[level][wave].append("\"{};{}\"".format(row.pop(0),row.pop(0)))
                row = next(fin)
                Array1[level][wave].append(int(row[3]))
                Array2[level][wave].append(int(row[5]))
                Array3[level][wave].append(int(row[7]))
                Array4[level][wave].append(int(row[9]))
                AirArray[level][wave].append(int(row[11]))

    with open('out_new.txt', 'w') as out_file:
		out_file.write('{}{}{}'.format('"{""c2array"":true,""size"":[10,10,11],""data"":', str(Array1).replace("'",'"'), '}\n\n'))
		out_file.write('{}{}{}'.format('"{""c2array"":true,""size"":[10,10,11],""data"":', str(Array2).replace("'",'"'), '}\n\n'))
		out_file.write('{}{}{}'.format('"{""c2array"":true,""size"":[10,10,11],""data"":', str(Array3).replace("'",'"'), '}\n\n'))
		out_file.write('{}{}{}'.format('"{""c2array"":true,""size"":[10,10,11],""data"":', str(Array4).replace("'",'"'), '}\n\n'))
		out_file.write('{}{}{}'.format('"{""c2array"":true,""size"":[10,10,11],""data"":', str(AirArray).replace("'",'"'), '}\n\n'))

   
if __name__ == '__main__':
    ConvertCSVToJSON()
