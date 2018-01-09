# -*- coding: utf-8 -*-
# reads a file "enemy arrays data" containing the levels data
# and outputs a file "out.txt" containing the JSON array.

def ConvertCSVToJSON():
    fin = open('enemy arrays data.csv', 'r')
    fout =open('out.txt', 'w')
    #flag=False  # set to true when we reach the word list in the file

#read and throw away the first 2 lines.
    fin.readline()
    fin.readline()

# Now read 10 levels that contain 10 waves each, that contain 10 possible enemies each.
# That needs to be done for four arrays.
    Array1=['\"{\"\"c2array\"\":true,\"\"size\"\":[10,10,11],\"\"data\"\":[']
    Array2=['\"{\"\"c2array\"\":true,\"\"size\"\":[10,10,11],\"\"data\"\":[']
    Array3=['\"{\"\"c2array\"\":true,\"\"size\"\":[10,10,11],\"\"data\"\":[']
    Array4=['\"{\"\"c2array\"\":true,\"\"size\"\":[10,10,11],\"\"data\"\":[']
    AirArray=['\"{\"\"c2array\"\":true,\"\"size\"\":[10,10,11],\"\"data\"\":[']

    for level in range(0 , 10):
        #print "level:"+str(level)
        Array1=Array1+['[']
        Array2=Array2+['[']
        Array3=Array3+['[']
        Array4=Array4+['[']
        AirArray=AirArray+['[']
        for wave in range(0 , 10):
            #print "wave:"+str(wave)
            Array1=Array1+['[']
            Array2=Array2+['[']
            Array3=Array3+['[']
            Array4=Array4+['[']
            AirArray=AirArray+['[']
            for enemy in range(0 , 10):
                line=fin.readline()
                temp=line.strip()
                items=temp.split(",")
                Array1=Array1+['\"\"'+items[3]+';'+items[4]+'\"\",']
                Array2=Array2+['\"\"'+items[5]+';'+items[6]+'\"\",']
                Array3=Array3+['\"\"'+items[7]+';'+items[8]+'\"\",']
                Array4=Array4+['\"\"'+items[9]+';'+items[10]+'\"\",']
                AirArray=AirArray+['\"\"'+items[11]+';'+items[12]+'\"\",']

            line=fin.readline()
            items=line.split(",")
            if wave<9:
                comma=','
            else:
                comma=''

            Array1=Array1+[items[3]+']'+comma]
            Array2=Array2+[items[5]+']'+comma]
            Array3=Array3+[items[7]+']'+comma]
            Array4=Array4+[items[9]+']'+comma]
            AirArray=AirArray+[items[11]+']'+comma]
        if level<9:
            comma=','
        else:
            comma=''

        Array1=Array1+[']'+comma]
        Array2=Array2+[']'+comma]
        Array3=Array3+[']'+comma]
        Array4=Array4+[']'+comma]
        AirArray=AirArray+[']'+comma]
    Array1=Array1+[']}\"']
    Array2=Array2+[']}\"']
    Array3=Array3+[']}\"']
    Array4=Array4+[']}\"']
    AirArray=AirArray+[']}\"']

    for i in Array1:
        fout.write(i)
    fout.write('\n\n')
    for i in Array2:
        fout.write(i)
    fout.write('\n\n')
    for i in Array3:
        fout.write(i)
    fout.write('\n\n')
    for i in Array4:
        fout.write(i)
    fout.write('\n\n')
    for i in AirArray:
        fout.write(i)
    fout.write('\n\n')
    fin.close()
    fout.close()


if __name__ == '__main__':
        ConvertCSVToJSON()
