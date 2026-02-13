from models import mascota

# Vamos a tener un simple metodo para llamarlo desde el main
def getSaludo():
    return "Hoy es juernes"

def getMascota():
    pez = mascota.Mascota()
    pez.nombre = "Flounder"
    pez.raza = "Pez"
    pez.edad = 22
    return pez

