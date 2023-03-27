from flask.views import MethodView
from flask import request,render_template, redirect 
from src.db import mysql


class InsertAlunosController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM alunos")
            alunos = cur.fetchall()
        return render_template('public/index.html', alunos=alunos)
    
    def post(self):
        nome = request.form['nome_alunos']
        # id_alunos = request.form['id_alunos']
    
        with mysql.cursor() as cur:
            cur.execute("INSERT INTO alunos(nome_alunos) VALUES(%s)", (nome))
            cur.connection.commit()
            return redirect('/')


class DeleteAlunosController(MethodView):
    def post(self, id_alunos):
        with mysql.cursor() as cur:
            cur.execute("DELETE FROM alunos WHERE id_alunos =%s", (id_alunos))
            cur.connection.commit()
            return redirect('/')


class UpdateAlunosController(MethodView):
    def get(self, id_alunos):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM alunos WHERE id_alunos =%s", (id_alunos,))
            alunos = cur.fetchone()
            cur.connection.commit()
            return render_template('public/updateAlunos.html', alunos=alunos)
    
    def post(self,id_alunos):
        # alunos_id = request.form['id_alunos']
        nome_alunos = request.form['nome_alunos']
        with mysql.cursor() as cur:
            cur.execute("UPDATE alunos SET nome_alunos =%s where id_alunos = %s", (nome_alunos, id_alunos))
            cur.connection.commit()
            return redirect('/')

