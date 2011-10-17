""" EXAMPLE FILE FOR PYTABLES HANDLING """

import tables as pyt
import numpy as np

class Particle(pyt.IsDescription):
    identity = pyt.StringCol(itemsize=22, dflt=" ", pos=0) # character String
    idnumber = pyt.Int16Col(dflt=1, pos = 1) # short integer
    speed = pyt.Float32Col(dflt=1, pos = 1) # single-precision
    
# Open a file in "w"rite mode
fileh = pyt.openFile("/home/dimitrios/objecttree.h5", mode="w")

# Get the HDF5 root group
root = fileh.root

# Create the groups:
group1 = fileh.createGroup(root, "group1")
group2 = fileh.createGroup(root, "group2")

# Now, create an array in root group
array1 = fileh.createArray(root, "array1", ["string", "array"], "Stringarray")

# Create 2 new tables in group1
table1 = fileh.createTable(group1, "table1", Particle)
table2 = fileh.createTable("/group2", "table2", Particle)

# Create the last table in group2
array2 = fileh.createArray("/group1", "array2", [1,2,3,4])

# Now, fill the tables:
for table in (table1, table2):
    # Get the record object associated with the table:
    row = table.row
    # Fill the table with 10 records
    for i in xrange(10):
        # First, assign the values to the Particle record
        row['identity'] = 'This is particle: %2d' % (i)
        row['idnumber'] = i
        row['speed'] = i * 2.
        # This injects the Record values
        row.append()

# Flush the table buffers
table.flush()

#Adding staff to PyTables tree
speed = [ x['speed'] for x in table.iterrows() if x['idnumber'] > 3 and 6 <= x['speed'] < 16 ]
print speed
identity = [ x['identity'] for x in table if x['idnumber'] >3 and 6 <= x['speed'] < 16 ]
print identity
gcolumns = fileh.createGroup(fileh.root, "columns", "speed and identity data")
fileh.createArray(gcolumns, 'speed', np.array(speed), 'Speed columns selection')
fileh.createArray(gcolumns, 'identity', identity, 'Identity columns selection')

#Browsing staff from PyTables tree
print "h5file nodes iteration"
for node in fileh:
    print node
print "Walking Groups iteration"
for group in fileh.walkGroups():
    print group
print "List Nodes -- (h5file.listNodes())"
for group in fileh.walkGroups():
    print fileh.listNodes(group, classname="Array")
print "Iterate list nodes"
for group in fileh.walkGroups():
    for array in fileh.listNodes(group, classname="Array"):
        print array
print "iterNodes() function"
for group in fileh.walkGroups():
    for array in fileh.iterNodes(group, classname="Array"):
        print array
print "h5file.walkNodes() function"
for array in fileh.walkNodes("/", classname="Array"):
    print array

    
# Finally, close the file (this also will flush all the remaining buffers!)
fileh.close()