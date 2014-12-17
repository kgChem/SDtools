#! C:/Python27/python.exe
#
class SDreader(object):
    """
    SDreader objects have methods that read and parses SD files to text
    """
    def __init__(self,filename):
        try:
            self.f = open(filename,"rb")
        except IOError as e:
            print("ERROR! Could not open the file {0}".format(filename))
            self.f = None
        else:
            self.filename = filename
            self.pos = 0
            self.numRecords = 0
            self.fields = []
            self.records = []

    def __iter__(self):
        return(self)

    def __str__(self):
        if self.f:
            return("An SDreader object linked to the file {0}".format(self.filename))
        else:
            return("An invalid SDreader object with no file link!")

    #Returns a block of text corresponding to 1 record in the SD File
    def next(self):
        lines = []
        linebuffer = self.f.readline()
        if linebuffer == None or linebuffer == '':
            raise StopIteration
        else:
            while (linebuffer != "" and not ('$$$$' in linebuffer)): 
                lines.append(linebuffer)
                linebuffer = self.f.readline()
            lines.append(linebuffer)
            return(''.join(lines))

    # Read all records in a file using the .next() method to extract the text
    def readRecords(self):
        pass

    # Read all field codes in the file and update the .fields with the update method
    def readFields(self):
        pass

    # Tells the number of records if already known. If not known, loops through the file
    # and counts number of records
    def numRecords(self):
        pass

    # Returns the n-th record in the file. If all file has been parsed, then it just
    # takes the value from .record[n]. If the file has not been parsed it steps through
    # the file until that record number is reached. Uses numRecords to check that the
    # value of n is a valid index
    def nRecord(self,n):
        pass

    # Searches through the .records[] to match a record containing some text string
    def searchRecord(self,queryString):
        pass

    # Determines if a record is in the .records[] field
    def _in(self,record):
        pass
            
## Testing code below. Uncomment to test        
#testfile = "E:/Documents/Computational/ChemInformatics/ChelatingFragments.sdf"
#B = SDreader("banana stand")
#print(B)
#S = SDreader(testfile)
#print(S)
#print('~'*80)
#S0 = S.next()
#print(S0)
#print('~'*80)
#S1 = S.next()
#print(S1)
#for record in S:
#    print record
