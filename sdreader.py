#! C:/Python27/python.exe
#
class SDreader(object):
    def __init__(self,filename):
        self.file = filename
        try:
            f = open(filename)
        except IOError as e:
            print("ERROR! Could not open the file {0}".format(filename))
            self.file = None
        else:
            f.close()
            
        
