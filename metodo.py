class Alumno:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def getnombre(self):
        return self._nombre    
    
    def getedad(self):
        return self._edad

a1 = Alumno("Maria", 20)
a2 = Alumno("Angel", 18)
a3 = Alumno("Juan", 21)
a4 = Alumno("Ana", 19)

edad_mayor = 0

if a1.getedad() > edad_mayor:
    edad_mayor = a1.getedad()
    alumno_mayor = a1.getnombre()
if a2.getedad() > edad_mayor:
    edad_mayor = a2.getedad()
    alumno_mayor = a2.getnombre()
if a3.getedad() > edad_mayor:
    edad_mayor = a3.getedad()
    alumno_mayor = a3.getnombre()
if a4.getedad() > edad_mayor:
    edad_mayor = a4.getedad()
    alumno_mayor = a4.getnombre()

print(f'El alumno mayor es {alumno_mayor} y tiene {edad_mayor} años de edad')
alumnos= [a1,a2,a3,a4]
edad_menor=999
for alum in alumnos:
    if alum.getedad() < edad_menor:
        edad_menor= alum.getedad()
        alumno_menor= alum.getnombre()
print(f'El alumno menor es {alumno_menor} y tiene {edad_menor} años de edad')        

suma_edades=0
for alum in alumnos:
    suma_edades+-alum.getedad()

print(f' la suma total de las edades es :{suma_edades}')    