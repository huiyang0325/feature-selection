"""
Author : LinDing Group (ZHAO)
Application : file format conversion
Date : 20160902
Usage: Please refer to the README file
Function : Converts the CSV format file to SVM format file!
"""

def generate_svm_file(csv_file,svm_file):
    g = open(svm_file,'w')
    f = open(csv_file).readlines()[1:]

    for eachline in f:
        eachline = eachline.strip().split(',')
        label = eachline[0]
        values = eachline[1:]
        for i in range(len(values)):
            label += '\t%d:%s'%(i+1,values[i])

        g.write('%s\n'%(label))

    g.close()
            
       
import sys,os

csv_file = sys.argv[1]
svm_file = sys.argv[2]

if __name__ == '__main__':
    generate_svm_file(csv_file,svm_file)



