from connection import get_db
from interfaces.DosenInterface import *

class DosenModel(DosenInterface):

    @staticmethod
    def all ():
        connection = get_db()
        cursor = connection.cursor()

        query = "select * from dosen"
        cursor.execute(query)
        results = cursor.fetchall()

        cursor.close()
        connection.close()

        return results
    
    @staticmethod
    def find(dosen_id):
        connection = get_db()
        cursor = connection.cursor()

        query = "select * from dosen where id = %s LIMIT 1"
        cursor.execute(query, (dosen_id))
        results = cursor.fetchone()

        cursor.close()
        connection.close()

        return results
    
    @staticmethod
    def store(dosen_obj):
        connection = get_db()
        cursor = connection.cursor()

        query = "insert into dosen (nidn, nama, bidang) values (%s, %s, %s)"
        cursor.execute(query, (dosen_obj.nidn, dosen_obj.nama, dosen_obj.bidang))

        connection.commit()
        cursor.close()
        connection.close()
    
    @staticmethod
    def update(dosen_id, dosen_obj):
        connection = get_db()
        cursor = connection.cursor()

        query = "update dosen set nidn = %s, nama = %s, bidang = %s where id = %s"
        cursor.execute(query, (dosen_obj.nidn, dosen_obj.nama, dosen_obj.bidang,  dosen_id))

        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def delete(dosen_id):
        connection = get_db()
        cursor = connection.cursor()

        query = "delete from dosen where id = %s"
        cursor.execute(query, (dosen_id))

        connection.commit()
        cursor.close()
        connection.close()