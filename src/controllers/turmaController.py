from flask.views import MethodView
from flask import request,render_template, redirect 
from src.db import mysql


class InsertTurmaController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM turmas")
            data = cur.fetchall()
        return render_template('public/index.html', data=data)
    
    def post(self):
        nome_turma = request.form['nome_turma']
    
        with mysql.cursor() as cur:
            cur.execute("INSERT INTO turmas(nome_turma) VALUES(%s)", (nome_turma))
            cur.connection.commit()
            return redirect('/')

class DeleteTurmaController(MethodView):
 
    def post(self, id_turma):
        with mysql.cursor() as cur:
            cur.execute("DELETE FROM turmas WHERE id_turma =%s", (id_turma))
            cur.connection.commit()
            return redirect('/')
    
class UpdateTurmaController(MethodView):
    def get(self, id_turma):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM turmas WHERE id_turma =%s", (id_turma,))
            turmas = cur.fetchone()
            cur.connection.commit()
            return render_template('public/updateTurma.html', turmas=turmas)
    
    def post(self,id_turma):
        nome_turma = request.form['nome_turma']
        with mysql.cursor() as cur:
            cur.execute("UPDATE turmas SET nome_turma =%s where id_turma = %s", (nome_turma, id_turma))
            cur.connection.commit()
            return redirect('/')