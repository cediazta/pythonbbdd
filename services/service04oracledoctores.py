import oracledb
from models import doctores as doct

class ServiceDoctores:
    def __init__(self):
        self.connection = oracledb.connect(user="system", 
                                          password="oracle",
                                          dsn="LOCALHOST/FREEPDB1")
        
    def mostrarDoctor(self):
        cursor = self.connection.cursor()
        sql = "select * from DOCTOR"
        cursor.execute(sql)
        listaDoctores = []
        for row in cursor:
            doctor = doct.Doctores()
            doctor.idHosp = row[0]
            doctor.idDoct = row[1]
            doctor.apellidoDoct = row[2]
            doctor.especialidadDoct = row[3]
            doctor.salarioDoct = row[4]
            listaDoctores.append(doctor)
        cursor.close()
        return listaDoctores
    
    def añadirDoctor(self, hospCod, apellido, especialidad, salario):
        cursor = self.connection.cursor()
        sql = "select max(DOCTOR_NO) + 1 as MAXIMO from DOCTOR"
        cursor.execute(sql)
        row = cursor.fetchone()
        id = row[0]
        sql = "insert into DOCTOR VALUES (:cod, :num, :ape, :esp, :sal)"
        cursor.execute(sql, (hospCod, id, apellido, especialidad, salario,))
        self.connection.commit()
        cursor.close()

    def modificarDoctor(self, hospCod, docCod, apellido, especialidad, salario):
        cursor = self.connection.cursor()
        sql = "update DOCTOR set HOSPITAL_COD=:cod, APELLIDO=:ape, ESPECIALIDAD=:esp, SALARIO=:sal where DOCTOR_NO=:num"
        cursor.execute(sql, (hospCod, apellido, especialidad, salario, docCod,))
        self.connection.commit()
        cursor.close()

    def deleteDoctor(self, docCod):
        cursor = self.connection.cursor()
        sql = "delete from DOCTOR where DOCTOR_NO=:num"
        cursor.execute(sql, (docCod,))
        self.connection.commit()
        cursor.close()
