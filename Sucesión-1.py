f1 = 1
f2 = 1
sucesion = [f1, f2]
for n in range(2, 80):
    fn = sucesion[n-2]+sucesion[n-1]
    sucesion.append(fn)
print(sucesion)