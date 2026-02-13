from services import service01prueba

print("Soy un Main")
texto = service01prueba.getSaludo()
print(texto)

pez = service01prueba.getMascota()
print(f"Nombre: {pez.nombre} - Raza: {pez.raza} - Edad: {pez.edad}")


