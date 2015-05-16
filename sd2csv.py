#!/C:/Python27/python.exe
"""
=== Usage: sd2csv <input.sdf> <output.csv> [options]

    Options:
    
    -s      Specify the column seperator. Default is ";"
    -f      Specify fields to include. Default is all
    -na     specify the value to write for missing data. Default is NA
    -l      Just show headers. Do not write file

"""

import sys, pybel, argparse

def getAllFields(inputFile):
    #Collect all the field tags present in the file
    infile = pybel.readfile("sdf", inputFile)
    fields = []
    for mol in infile:
        for field in mol.data.keys():
            if not(field in fields):
                fields.append(field)
    return(fields)

def convertFile(inputFile,outputFile,fields,sep,NAval):
    #Converts the sdf file to a CSV file
    #fields is an ordered list of which fields to include as column heads
    count=0
    try:
        infile = pybel.readfile("sdf", inputFile)
        with open(outputFile,'w') as outF:
            #write smiles and header
            outF.write("SMILES"+sep+"Name"+sep)
            outF.write(sep.join(fields))
            outF.write('\n')
            for mol in infile:
                outF.write(writeRow(mol,fields,sep,NAval))
                outF.write('\n')
                count = count+1
        print('Processed {} records'.format(count))
        return(0)
    except IOError as e1:
        print("I/O error({0}: {1}".format(e1.errno,e1.strerror))
        return(1)
    except:
        print "Unexpected error:", sys.exc_info()[0]
    return(1)

def writeRow(mol,fields,sep,NAval):
    row=[]
    row.append(mol.write("smi").split()[0])
    row.append(mol.title)
    for field in fields:
        if field in mol.data.keys():
            data = mol.data[field]
            if sep in data: #doesn't seem to work
                data.replace(sep,'\s')
            if '\n' in data: #doesn't seem to work
                data.replace('\n','\s')
            row.append(data)
        else:
            row.append(NAval)
    return(sep.join(row))
    

def testfile(filename,mode):
    try:
        f = open(filename,mode)
        f.close()
    except IOError as e1:
        print("-!-Error accessing the file {0}\n{1}".format(filename,e1))
        sys.exit(2)
    except:
        print("-!-Unexpected error occured opening file {}".format(filename))
        sys.exit(2)
    else:
        return(True)

def printFields(fields,selectedFields):
    for field in fields:
        if field in selectedFields:
            print(field)
        else:
            print('Requested field {} not found in source file'.format(field))
    return(None)
    
def main():
    ## Parse the arguments passed in
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help ="input .sdf file to read from")
    parser.add_argument("output",help="output .csv file to write to")
    parser.add_argument("-s","--seperator",help="specify the colum seperator. Default is ;")
    parser.add_argument("-f","--fields",help="Specify fields to include. Default is all")
    parser.add_argument("-na","--na_value",help="specify the value to write for missing data. Default is NA")
    parser.add_argument("-l","--list",help="Just list headers. Do not write file"
                        action="store_true")
    args = parser.parse_args()
    #List only mode ignores outputting options
    if args.list:
        fileOK = testfile(args.input,'r')
        allFields = getAllFields(args.input)
        if args.fields:
            printFields(allFields,arg.fields)
        else:
            printFields(allFields,allFields)
    #Writing file, so check for other options
    else:
        fileOK = testfile(args.input,'r') and testfile(args.output.'w')
        if args.seperator:
            sep=args.seperator
        else:
            sep=';'
        if args.na_value:
            NAval = args.na_value
        else:
            NAval = "NA"
        if args.fields:
            fields = args.fields
        else:
            fields = getAllFields(args.input)
        convertFile(args.input,args.output,fields,sep,NAval)
    sys.exit(0)

if __name__ == "__main__":
    main() 

testing = "E:/Documents/My Data Sources/Selleck_FDA_Approved.sdf"
outfile = "E:/Documents/My Data Sources/Selleck_FDA_Approved.csv"
ok = testfile(testing,'r') and testfile(outfile,'w')
if ok:
    print('==> Testing getAllFields')
    fields = getAllFields(testing)
    print(fields)
    print('==> Testing writeRow with first 3 records in {}'.format(testing))
    infile = pybel.readfile("sdf", testing)
    print('MOLECULE1 \n\n')
    print(writeRow(infile.next(),fields,';'))
    print('MOLECULE2 \n\n')
    print(writeRow(infile.next(),fields,';'))
    print('MOLECULE3 \n\n')
    print(writeRow(infile.next(),fields,';'))
    print('~*'*40)
    print('==> Testing convertFile()')
    status = convertFile(testing,outfile,fields,';')
    if status == 0:
        print('convertFile exited cleanly')
    else:
        print('errors occured in convertFile')
else:
    print('error. Problem with the test files')
    
