#! C:/Python27/python.exe
#
class SDreader(object):
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

    #Returns a block of text corresponding to 1 record in the SD File
    def next(self):
        lines = []
        linebuffer = self.f.readline()
        while (linebuffer and not ('$$$$' in linebuffer)):
            lines.append(linebuffer)
            linebuffer = self.f.readline()
        lines.append(linebuffer)
        return(''.join(lines))
            
        
testfile = "E:/Documents/Computational/ChemInformatics/ChelatingFragments.sdf"
#S = SDreader("banana stand")
S = SDreader(testfile)
print('~'*80)
S0 = S.next()
print(S0)
print('~'*80)
S1 = S.next()
print(S1)
