import operator

def writeOBJ(vertices, vertexnormals, faces, filename):
    # v x y z
    # vn x y z 
    # f v1//vn1 v2//vn2 v3//vn3
    # no textures yet! when ready write as 
    # f v1/vt1/vn1 v2/vt2/vn2 v3/vt3/vn3

    with open(filename, "w") as thefile:
        
        thefile.write("# {} vertices\n".format(len(vertices)))
        thefile.write("# {} faces\n".format(len(faces)))

        for v in vertices:
            thefile.write("v {0[0]} {0[1]} {0[2]}\n".format(v))
        for vn in vertexnormals:
            thefile.write("vn {0[0]} {0[1]} {0[2]}\n".format(vn))
        for f in faces:
            f = map(operator.add, f, [1, 1, 1])
            thefile.write("f {0[0]}//{0[0]} {0[1]}//{0[1]} {0[2]}//{0[2]}\n".format(f))
