from flask.views import MethodView
from flask import request,render_template, redirect 
from src.db import mysql


class InsertProfessoresController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM professores")
            professores = cur.fetchall()
        return render_template('public/index.html', professores=professores)

    def post(self):
        nome = request.form['nome_professores']
        # id_professores = request.form['id_professores']

        with mysql.cursor() as cur:
            cur.execute("INSERT INTO professores(nome_professores) VALUES(%s)", (nome))
            cur.connection.commit()
            return redirect('/')
        

class DeleteProfessoresController(MethodView):
    def post(self, id_professores):
        with mysql.cursor() as cur:
            cur.execute("DELETE FROM professores WHERE id_professores =%s", (id_professores))
            cur.connection.commit()
            return redirect('/')

        
class UpdateProfessoresController(MethodView):
    def get(self, id_professores):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM professores WHERE id_professores =%s", (id_professores,))
            professores = cur.fetchone()
            cur.connection.commit()
            return render_template('public/updateProfessores.html', professores=professores)
    
    def post(self,id_professores):
        # professores_id = request.form['id_professores']
        nome_professores = request.form['nome_professores']
        with mysql.cursor() as cur:
            cur.execute("UPDATE professores SET nome_professores =%s where id_professores = %s", (nome_professores, id_professores))
            cur.connection.commit()
            return redirect('/')
        
