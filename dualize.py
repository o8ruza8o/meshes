import operator
from loadOBJ import loadOBJverticesANDfaces
from writeOBJ import writeOBJ
from normals import normals

def dualize(v, f):
    dualf = []
    dualv = []

    for face in f:
        s = [0, 0, 0]
        # note v is zero indexed...
        for i in face: s = map(operator.add, s, v[i-1])
        dualv.append([x/len(face) for x in s])

    return dualv, dualf


filename = 'tre.obj'
dualfilename = 'ert.obj'

v, f = loadOBJverticesANDfaces(filename)
dualv, dualf = dualize(v, f)
dualn = normals(dualv, dualf)
writeOBJ(dualv, dualn, dualf, dualfilename)
