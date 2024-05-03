from flask import *
from models.MahasiswaModel import *

class MahasiswaView():

    @staticmethod
    def index():
        data = MahasiswaModel().all()
        return render_template('mahasiswa_index.html', data=data)
    
    @staticmethod
    def create():
        return render_template('mahasiswa_create.html')
    
    @staticmethod
    def store():
        mahasiswa_obj=MahasiswaModel()
        post = request.form
        mahasiswa_obj.nim = post['nim']
        mahasiswa_obj.nama = post['nama']
        mahasiswa_obj.prodi = post['prodi']
        MahasiswaModel.store(mahasiswa_obj)
        return redirect('/mahasiswa')
    
    @staticmethod
    def edit(mahasiswa_id):
        obj = MahasiswaModel().find(mahasiswa_id)
        return render_template('Mahasiswa_edit.html', obj=obj)
    
    @staticmethod
    def update(mahasiswa_id):
        data = MahasiswaModel().find(mahasiswa_id)
        if data :
            post = request.form
            mahasiswa_obj = MahasiswaModel()
            mahasiswa_obj.nim = post['nim']
            mahasiswa_obj.nama = post['nama']
            mahasiswa_obj.prodi = post['prodi']
            MahasiswaModel.update(mahasiswa_id, mahasiswa_obj)
            return redirect('/mahasiswa')
        else :
            return redirect(request.referre)
    
    @staticmethod
    def delete(mahasiswa_id):
        data = MahasiswaModel.find(mahasiswa_id)
        if data :
            MahasiswaModel.delete(mahasiswa_id)
            return redirect(request.referrer)