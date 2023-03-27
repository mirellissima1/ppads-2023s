from flask.views import MethodView
from flask import request,render_template, redirect 
from src.db import mysql


class InsertDisciplinaController(MethodView):
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM disciplina")
            data = cur.fetchall()
        return render_template('public/index.html', data=data)
    
    def post(self):
        nome = request.form['nome_disciplina']
        # id_disciplina = request.form['id_disciplina']
    
        with mysql.cursor() as cur:
            cur.execute("INSERT INTO disciplina(nome_disciplina) VALUES(%s)", (nome))
            cur.connection.commit()
            return redirect('/')

class DeleteDisciplinaController(MethodView):
    def post(self, id_disciplina):
        with mysql.cursor() as cur:
            cur.execute("DELETE FROM disciplina WHERE id_disciplina =%s", (id_disciplina))
            cur.connection.commit()
            return redirect('/')
    
class UpdateDisciplinaController(MethodView):
    def get(self, id_disciplina):
        with mysql.cursor() as cur:
            cur.execute("SELECT * FROM disciplina WHERE id_disciplina =%s", (id_disciplina,))
            disciplina = cur.fetchone()
            cur.connection.commit()
            return render_template('public/updateDisciplina.html', disciplina=disciplina)
    
    def post(self,id_disciplina):
        # disciplina_id = request.form['id_disciplina']
        nome_disciplina = request.form['nome_disciplina']
        with mysql.cursor() as cur:
            cur.execute("UPDATE disciplina SET nome_disciplina =%s where id_disciplina = %s", (nome_disciplina, id_disciplina))
            cur.connection.commit()
            return redirect('/')

