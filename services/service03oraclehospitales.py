import oracledb
from models import hospital as models

class ServiceHospitales:
    def __init__(self):
        self.connection = oracledb.connect(user="system", 
                                          password="oracle",
                                          dsn="LOCALHOST/FREEPDB1")

    # Metodo para recuperar todos los hospitales
    def getHospitales(self):
        cursor = self.connection.cursor()
        sql = "select * from HOSPITAL"
        cursor.execute(sql)
        listaHospitales = []
        for row in cursor:
            hospital = models.Hospital()
            hospital.idHosp = row[0]
            hospital.nombreHosp = row[1]
            hospital.direccionHosp = row[2]
            hospital.telefonoHosp = row[3]
            hospital.camasHosp = row[4]
            listaHospitales.append(hospital)
        cursor.close()
        return listaHospitales
    
    def insertarHospital(self, id, nombre, dir, tlf, camas):
        cursor = self.connection.cursor()
        sql = "insert into HOSPITAL values (:id, :nom, :dir, :tlf, :cam)"
        cursor.execute(sql, (id, nombre, dir, tlf, camas,))
        self.connection.commit()
        cursor.close()
    
    def updateHospital(self, id, nombre, dir, tlf, camas):
        cursor = self.connection.cursor()
        sql = "update HOSPITAL set NOMBRE=:nom, DIRECCION=:dir, TELEFONO=:tlf, NUM_CAMA=:cam where HOSPITAL_COD=:id"
        cursor.execute(sql, (nombre, dir, tlf, camas, id,))
        self.connection.commit()
        cursor.close()

    def deleteHospital(self, id):
        cursor = self.connection.cursor()
        sql = "delete from HOSPITAL where HOSPITAL_COD=:id"
        print(id)
        cursor.execute(sql, (id,))
        self.connection.commit()
        cursor.close()


