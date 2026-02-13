from services import service02oracledepartamentos as sv

print("------ DEPARTAMENTOS ------")
mostrar = sv.ServiceDepartamentos()
lista = mostrar.listaDepartamentos()
for dept in lista:
    print(f"{dept.numeroDept} - {dept.nombreDept} - {dept.localidadDept}")

print("------ INSERTAR DEPARTAMENTO ------")
servicio = sv.ServiceDepartamentos()
numero = int(input("Numero de Dpto: "))
nombre = input("Nombre de Dpto: ")
localidad = input("Localidad: ")

reg = servicio.insertarDepartamento(numero, nombre, localidad)
print(f"Insertados {reg} registros.")


print("------ ELIMINAR DEPARTAMENTO ------")
servicio = sv.ServiceDepartamentos()
id = int(input("Num. Departamento a eliminar: "))

reg = servicio.eliminarDepartamento(id)
print(f"{reg} registros eliminados.")

print("------ MODIFICAR DEPARTAMENTO ------")
servicio = sv.ServiceDepartamentos()
numero = int(input("Numero de Dpto a Modificar: "))
numeroMod = int(input("Numero de Dpto Nuevo: "))
nombreMod = input("Nombre de Dpto Nuevo: ")
localidadMod = input("Localidad Nueva: ")

reg = servicio.modificarDepartamento(numeroMod, nombreMod, localidadMod, numero)
print(f"{reg} registros modificado.")

print("------ CONSULTA DEPARTAMENTO ------")
servicio = sv.ServiceDepartamentos()
consulta = int(input("NUMERO DEPARTAMENTO: "))
datos = servicio.consultaDepartamento(consulta)
print(f"Nombre: {datos.nombreDept} - Localidad: {datos.localidadDept}")





