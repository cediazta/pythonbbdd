import oracledb
from models import departamento

class ServiceDepartamentos:
    def __init__(self):
        self.connection = oracledb.connect(user="system", 
                                          password="oracle",
                                          dsn="LOCALHOST/FREEPDB1")
        
    def insertarDepartamento(self, numero, nombre, localidad):
        cursor = self.connection.cursor()
        sql = "insert into DEPT values (:num, :nom, :loc)"
        cursor.execute(sql, (numero, nombre, localidad,))
        self.connection.commit()
        registros = cursor.rowcount
        cursor.close()
        return registros
    
    def eliminarDepartamento(self, id):
        cursor = self.connection.cursor()
        sql = "delete from DEPT where DEPT_NO = :id"
        cursor.execute(sql, (id,))
        self.connection.commit()
        registros = cursor.rowcount
        cursor.close()
        return registros

    def modificarDepartamento(self, numeroMod, nombreMod, localidadMod, numero):
        cursor = self.connection.cursor()
        sql = "update DEPT set DEPT_NO = :numMod, DNOMBRE = :nomMod, LOC = :locMod where DEPT_NO = :num" 
        cursor.execute(sql, (numeroMod, nombreMod,localidadMod, numero,))
        self.connection.commit()
        registros = cursor.rowcount
        cursor.close()
        return registros
    
    def mostrarDepartamentos(self):
        cursor = self.connection.cursor()
        sql = "select * from DEPT"
        cursor.execute(sql)
        for row in cursor:
            print(f"Codigo: {row[0]} - Nombre: {row[1]} - Localidad: {row[2]}")
        cursor.close()

    def consultaDepartamento(self, consulta):
        cursor = self.connection.cursor()
        sql = "select DEPT_NO, DNOMBRE, LOC from DEPT where DEPT_NO=:cons"
        cursor.execute(sql, (consulta,))
        row = cursor.fetchone()
        dept = departamento.departamento()
        dept.numeroDept = row[0]
        dept.nombreDept = row[1]
        dept.localidadDept = row[2] 
        cursor.close()
        return dept
    
    def listaDepartamentos(self):
        cursor = self.connection.cursor()
        sql = "select * from DEPT"
        cursor.execute(sql)
        # Necesitamos una lista para guardar cada departamento.
        listaDepartamentos = []
        # por cada fila, creamos un objeto Departamento
        for row in cursor:
            dept = departamento.departamento()
            dept.numeroDept = row[0]
            dept.nombreDept = row[1]
            dept.localidadDept = row[2]
            # añadimos a la lista cada departamento
            listaDepartamentos.append(dept)
        cursor.close()
        return listaDepartamentos
                

