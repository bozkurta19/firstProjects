def findPythagorasTrianglesUnder(num):
    pythagoras_triangles_list = list()

    for x in range(1, num):

        # making y larger than x
        for y in range(x + 1, num):
            z = (x ** 2 + y ** 2) ** 0.5

            if z == int(z) and z < num:
                pythagoras_triangles_list.append((x, y, int(z)))

    return pythagoras_triangles_list


print("Pythagoras Triangles : ")

for i in findPythagorasTrianglesUnder(100):
    print(i)
