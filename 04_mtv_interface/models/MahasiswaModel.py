from connection import get_db
from interfaces.MahasiswaInterface import *

class MahasiswaModel(MahasiswaInterface):

    @staticmethod
    def all ():
        connection = get_db()
        cursor = connection.cursor()

        query = "select * from mahasiswa"
        cursor.execute(query)
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return results
    
    @staticmethod
    def find(mahasiswa_id):
        connection = get_db()
        cursor = connection.cursor()

        query = "select * from mahasiswa where id = %s LIMIT 1"
        cursor.execute(query, (mahasiswa_id))
        results = cursor.fetchone()

        cursor.close()
        connection.close()

        return results
    
    @staticmethod
    def store(mahasiswa_obj):
        connection = get_db()
        cursor = connection.cursor()

        query = "insert into mahasiswa (nim, nama, prodi) values (%s, %s, %s)"
        cursor.execute(query, (mahasiswa_obj.nim, mahasiswa_obj.nama, mahasiswa_obj.prodi))

        connection.commit()
        cursor.close()
        connection.close()
    
    @staticmethod
    def update(mahasiswa_id, mahasiswa_obj):
        connection = get_db()
        cursor = connection.cursor()

        query = "update mahasiswa set nim = %s, nama = %s, prodi = %s where id = %s"
        cursor.execute(query, (mahasiswa_obj.nim, mahasiswa_obj.nama, mahasiswa_obj.prodi,  mahasiswa_id))

        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def delete(mahasiswa_id):
        connection = get_db()
        cursor = connection.cursor()

        query = "delete from mahasiswa where id = %s"
        cursor.execute(query, (mahasiswa_id))

        connection.commit()
        cursor.close()
        connection.close()