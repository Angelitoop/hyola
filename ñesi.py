class Futbolista:
    def __init__(self, nombre, edad, pais):
        self._nombre = nombre
        self._edad = edad
        self._pais = pais

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad

    @property
    def pais(self):
        return self._pais

    @pais.setter
    def pais(self, nuevo_pais):
        self._pais = nuevo_pais

    def __str__(self):
        return f'Futbolista(nombre={self._nombre}, edad={self._edad}, pais={self._pais})'


p = Futbolista("Messi", 18, "Argentina")
print(p)


  
  


