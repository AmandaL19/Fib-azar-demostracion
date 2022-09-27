import random
f1 = 1
f2 = 1
sucesion = [f1, f2]
for n in range(2, 1000):
    fn = sucesion[n-2]+sucesion[n-1]
    sucesion.append(fn)
Ronda = 0
Contador = 0
Resultado = 0
while Resultado == 0:
    Ronda = Ronda + 1 
    Apuesta = sucesion[Ronda-1]
    Resultado = random.randint(0, 1)
    if Resultado == 0 :
        Contador = Contador - Apuesta
        print("En la ronda número",(Ronda),"se han perdido",(Apuesta),"€")
    elif Resultado == 1 :
        Contador = Contador + (Apuesta*2)
        print("En la ronda número",(Ronda),"se han ganado",(Apuesta*2),"€")
print("Se ha conseguido en total",(Contador),"€") 