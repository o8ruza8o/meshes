from loadOBJ import loadOBJverticesANDfaces
from writeOBJ import writeOBJ
from math import sqrt
import operator

filename = 'four.obj'
filenameWnormals = 'fourn.obj'


def Normalize(normals):
    normalSum = [0, 0, 0]
    normSquared = 0
    for n in normals:
        normSquared += sum(map(operator.mul, n, n))
        normalSum = map(operator.add, normalSum, n)

    norm = sqrt(normSquared)
    normalised = []
    for c in normalSum: normalised.append(c/norm)

    return normalised


def cross(a, b):
    return [a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]]


def FaceNormal(a, b, c):
    side1 = map(operator.add, b, map(operator.neg, a))
    side2 = map(operator.add, c, map(operator.neg, a))

    return cross(side1, side2)


def normals(v, f):
    # should vertices be touples to start with?
    fn = []                         # calculate normals per face
    vn = []                         # then calculate normals per vertex
    vertexdic = {}                  # a dic with vertices as keys

    # initialize all normals in vertex dic
    for vertex in v:
        vertexdic[tuple(vertex)] = []

    # calculate each face normal and add it to the 3 vertices in vertexdic
    for face in f:
        # subtracting onse as objs are 1based
        a = v[face[0]-1]
        b = v[face[1]-1]
        c = v[face[2]-1]
        facenormal = FaceNormal(a, b, c)
        fn.append(facenormal)
        vertexdic[tuple(a)].append(facenormal)
        vertexdic[tuple(b)].append(facenormal)
        vertexdic[tuple(c)].append(facenormal)

    # normalize the vertices to average over faces
    for vertex in v:
        vn.append(Normalize(vertexdic[tuple(vertex)]))
    print len(vn), " normals constructed"

    return vn



v, f = loadOBJverticesANDfaces(filename)
vn = normals(v, f)
writeOBJ(v, vn, f, filenameWnormals)
