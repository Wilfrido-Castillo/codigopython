class persona: #se crea la clase persona con sus atributos
    nombre = ""
    apellido = ""
    escuela = ""

    def __init__(self, nombrex,apellido, escuela): #se crea el constructor 
        self.nombre = nombrex
        self.apellido = apellido
        self.escuela = escuela


    def saludar(self):
        saludo = "Hola, mi nombre es: " +  self.nombre+ " " + self.apellido

        return saludo
    
p1 = persona("Wilfrido", "Castillo", "Bonfil")
print(p1.saludar())
