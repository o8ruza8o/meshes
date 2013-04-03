# consider cgkit.objmtl.OBJReader
import operator

def loadOBJvertices(filename):
	vertices = []
	for line in open(filename, "r"):
		vals = line.strip().split()
                if len(vals) > 0:
                    if vals[0] == "v":
                        v = map(float, vals[1:4])
                        vertices.append(v)
	return vertices


def loadOBJverticesANDfaces(filename):
	vertices = []
        faces = []
	for line in open(filename, "r"):
		vals = line.strip().split()
                if len(vals) > 0:
                    if vals[0] == "v":
                        v = map(float, vals[1:4])
                        vertices.append(v)
                    if vals[0] == "f":
                        face = line[2:].strip().split()
                        f = map(int, face)
                        f = map(operator.add, f, [-1, -1, -1])
                        faces.append(f)
	return vertices, faces


def loadOBJ(filename):
	vertices = []
	normals = []
        faces = []
	for line in open(filename, "r"):
		vals = line.strip().split()
                if len(vals) > 0:
                    if vals[0] == "v":
                        v = map(float, vals[1:4])
                        vertices.append(v)
                    if vals[0] == "vn":
                        n = map(float, vals[1:4])
                        normals.append(n)
                    if vals[0] == "f":
                        face = line[2:].strip().split()
                        f = map(int, face)
                        f = map(operator.add, f, [-1, -1, -1])
                        
                        # fix this part once there are normals
                        # for i in range(0, len(face)) :
                        #     face[i] = face[i].split('/')
                        #     # OBJ indexies are 1 based not 0 based hence the -1
                        #     # convert indexies to integer
                        #     for j in range(0, len(face[i])) : f[i][j] = int(face[i][j]) - 1
                        faces.append(f)
	return vertices, normals, faces



def loadOBJtextures(filename):
	vertices = []
	normals = []
        faces = []
	for line in open(filename, "r"):
		vals = line.strip().split()
                if len(vals) > 0:
                    if vals[0] == "v":
                        v = map(float, vals[1:4])
                        vertices.append(v)
                    if vals[0] == "vn":
                        n = map(float, vals[1:4])
                        normals.append(n)
                    if vals[0] == "f":
                        face = line[2:].strip().split()
                        f = map(int, face)
                        f = map(operator.add, f, [-1, -1, -1])
                        
                        # fix this part once there are normals and textures
                        faces.append(f)
	return vertices, normals, faces
