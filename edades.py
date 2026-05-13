#Autores: Wilfrido David Castillo Lugo
#Ya lo modifique hoy 16 de abril de 2026
#ESTE ES UN NUEVO COMENTARIO
#otro comentario
#algo
cn=0
cj=0
ca=0
cv=0
sn=0
sj=0
sa=0
sv=0
for i in range(1, 5+1):
    edad= int(input(f"Ingrese la edad de la persona: {i} "))
    peso = float(input("Ingrese el peso de la persona "))
    if edad>=0 and edad<=12:
        sn = sn+peso
        cn = cn+1
    elif edad>=13 and edad<=29:
        sj = sj+peso
        cj = cj+1
    elif edad>=30 and edad<=59:
        sa =  sa+peso
        ca = ca+1
    else:
        sv = sv+peso
        cv= cv+1
print("El promedio de edad de los niños es ", sn/cn)
    
