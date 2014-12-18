#
# this function parses and SD file and adds key values
# so that it is compatible with ISIS/BASE importing
#

import re

def assignID(filename):
    # Check that the file has the right extension 
    if filename[-4:].lower() != ".sdf":
        print('Error! Invalid file {}'.format(filename))
        raise TypeError
        return(None)
    # Define the strig that marks the end of the MOL portion
    pat = re.compile(r"M\s*END")
    # Loop through lines of the file
    i=1
    with open(filename,"rb") as f:
        with open (filename[:-4]+"_ISIS-BASE.sdf","wb") as o:
            for line in f:
                if pat.search(line):
                    line = (line + "\n\n> <ID>\n" + str(i)+ "\n\n")
                    i=i+1
                o.write(line)
    return(i)
                    
                
