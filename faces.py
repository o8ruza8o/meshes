import operator

# careful: objs are 1 based
n = 60                          # number of loops
m = 7                           # points per loop
filename = 'try.obj'

def addFaces(n, m, filename):
    
    faces = []
    for i in range(m):       # goes through all m vertices around a loop
        for j in range(n):      # goes through all n loops
            f1 = [i +j*m, ((i + 1)%m + j*m)%(n*m), (i + j*m + m)%(n*m)]
            faces.append(f1)
            
            f2 = [((i + 1)%m + j*m)%(n*m), ((i+1)%m + j*m + m)%(n*m), (i + j*m + m)%(n*m)]
            faces.append(f2)
            # inserts mods and takes care of zeros
            
    # print faces to file 
    with open(filename, 'a') as thefile:
        thefile.write("# {} faces\n".format(len(faces)))
        for f in faces:
            f = map(operator.add, f, [1, 1, 1])
            thefile.write("f {0[0]} {0[1]} {0[2]}\n} ".format(f))
            
    print len(faces), " faces writen"

