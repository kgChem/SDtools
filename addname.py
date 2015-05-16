#! C:/Python27/python.exe
import re
import sys

class BadArgs(StandardError):
        pass

def readBlock(f):
        lines=[]
        linebuffer = f.readline()
        if linebuffer == None or linebuffer == '':
            return(None)
        else:
            while (linebuffer != "" and not ('$$$$' in linebuffer)): 
                lines.append(linebuffer)
                linebuffer = f.readline()
            lines.append(linebuffer)
            return(''.join(lines))

def readFile(filename):
    with open(filename,"rb") as f:
        records=[]
        record = readBlock(f)
        while record:
            records.append(record)
            record = readBlock(f)
    return(records)

def addNames(data):
    newdata = []
    for record in data:
        name = re.search(r'NSNV.*',record).group(0)
        newdata.append(name+'\n'+record[2:])
    return(newdata)

def writeSDF(data,filename):
    with open(filename,"wb") as f:
        for record in data:
            f.write(record)
    return('{} records written'.format(len(data)))

def main():
        if (len(sys.argv)<3):
                raise BadArgs()
                print('Got wrong number of args!')
                return(-1)
        else:
                sourcefile = sys.argv[1]
                outfile = sys.argv[2]
        try:
                f_in = open(sourcefile,'r')
                f_in.close()
                f_out = open(outfile,'w')
                f_out.close()
        except Exception as e:
                print(e)
                return(-1)
        data = readFile(sourcefile)
        print('read {} records from {}'.format(len(data),sourcefile))
        data2 = addNames(data)
        writeSDF(data2,outfile)
        return(0)

if __name__=="__main__":
        status = main()
