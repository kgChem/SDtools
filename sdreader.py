#! C:/Python27/python.exe
#
import re
class SDreader(object):
    """
    SDreader objects have methods that read and parses SD files to text
    """
    def __init__(self,filename):
        try:
            self.f = open(filename,"rb")
        except IOError as e:
            print("ERROR! Could not open the file {0}".format(filename))
            self.filename = filename
            self.f = None
        else:
            self.filename = filename
            self.pos = 0
            self.nRecords = 0
            self.fields = []
            self.records = []

    def __iter__(self):
        return(self)

    def __str__(self):
        if self.f:
            return("An SDreader object linked to the file {0}".format(self.filename))
        else:
            return("This is an invalid SDreader object linked to the file".format(self.filename))

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

    # Iterate over the file reading all records to extract the text
    def readRecords(self):
        if self.isValid:
            for record in self:
                self._addRecord(record)
                self.pos = self.pos + 1
        else:
            print('Cannot read records for an invalid SDreader object')

    def _addRecord(self,record):
        self.records.append(record)
        self.nRecords = self.nRecords + 1  

    def isValid(self):
        if self.f == None:
            return(False)
        else: 
            return(True) #Will elaborate more sophisticated error checking later!
        
    # Read all field codes in the file and update the .fields with the update method
    def readFields(self):
        pat=re.compile("<.*>")
        with open(self.filename,"r") as f:
            for line in f:
                hit= pat.search(line)
                if hit and (not hit.group(0) in self.fields):
                    self.fields.append(hit.group(0))

    # Tells the number of records if already known. If not known, loops through the file
    # and counts number of records
    def numRecords(self):
        if self.nRecords == 0:
            self.readRecords()
        return(self.nRecords)
    
    # Returns the n-th record in the file. If all file has been parsed, then it just
    # takes the value from .record[n]. If the file has not been parsed it steps through
    # the file until that record number is reached. Uses numRecords to check that the
    # value of n is a valid index
    def nthRecord(self,n):
        pass

    # Searches through the .records[] to match a record containing some text string
    def searchRecord(self,queryString):
        pass

    # Determines if a record is in the .records[] field
    def _in(self,record):
        pass

    # Converts the SD file to tabular data
    # Should eventually include converting the SD structure to
    # a smiles string

    def outputSDF(self,filename):
        try:
            f = open(filename,'wb')
            for record in self.records:
                f.write(record)
        except IOError as e:
            print('Error opening file {}:{}'.format(filename,e))
        finally:
            f.close()
#not working yet
    def updateField(self,recIndex,fieldname,newValue):
        if (recIndex < 0 or recIndex > self.nRecords):
            print('Error: recordIndex {} outside range 0-{}'.format(recIndex,self.nRecords))
            raise ValueError
        tag=re.search(fieldname,self.records[recIndex])
        if tag:
            oldData = re.search('.*>',(self.records[recIndex])[tag.end(0)+1:],re.DOTALL)
            newData = "\r\n"+newValue+"\r\n>"
            self.records[recIndex]=re.sub(oldData.group(0),newData,self.records[recIndex],count=1)
        else:
            oldData = "$$$$\r\n"
            newData = "> "+fieldname + "\r\n" + newValue + "\r\n\r\n" + OldData
            self.records[recIndex]=re.sub(oldData,newData,self.records[recIndex],count=1)

                                          
            

    

# Testing readRecords
source = "E:/Documents/Projects/Vertex/Shipment97 NSNCF180_updated 042915.sdf"
#sink = "E:/Documents/Projects/Vertex/Shipment97 NSNCF180_updated 042915-KLG.sdf"
S = SDreader(source)
print('found {0} records in {1}'.format(S.numRecords(),source))
#S.outputSDF(sink)
print('found these fields in the SDfile')
S.readFields()
print(S.fields)
