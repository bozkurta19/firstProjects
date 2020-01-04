def pisagor_bulma():

    pisagor_listesi = list()

    for x in range(1,100):
        for y in range(x + 1,100):
            z = (x**2 + y**2) ** 0.5

            if z == int(z) and z <= 100:
                pisagor_listesi.append((x,y,int(z)))

    return pisagor_listesi

print("Pisagor Üçgenler : ")

for i in pisagor_bulma():
    print(i)