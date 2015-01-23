#!/C:/Python27/python.exe
"""
Usage: ISISTag.py input.sdf output.sdf

Adds a unique key field to each record in an SD file so that
ISIS/Base is able to import it

"""
import sys

def isisTag(infile,outfile,tag = "ID",start=1):
    i = start
    with open(infile, "r") as f:
        with open(outfile,"w") as o:
            for line in f:
                if 'M  END' in line:
                    o.write(line)
                    newtext = ("\n>  <"+tag+">\n"+str(i)+"\n\n")
                    o.write(newtext)
                    i = i+1
                else:
                    o.write(line)
    print('Processed {} records'.format(i))
    return(0)

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

def main():
    # check file access
    try:
        if (len(sys.argv) < 3) or (sys.argv[1]==sys.argv[2]):
            raise(IOError('-!-Error: Improper arguments supplied'))
        else:
            filesOK = testfile(sys.argv[1],'r') and testfile(sys.argv[2],'w')
    except IOError as e2:
        print(e2)
        print(__doc__)
        sys.exit(2)
    except:
        print("-!-Another unknown error occured in main()")
    else:
        isisTag(sys.argv[1],sys.argv[2]) #add options later
        sys.exit(0)

if __name__ == "__main__":
    main()                  
