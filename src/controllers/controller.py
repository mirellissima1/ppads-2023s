# from flask.views import MethodView
# from flask import request,render_template, redirect 
# from src.db import mysql


# class InsertTurmaController(MethodView):
#     def get(self):
#         with mysql.cursor() as cur:
#             cur.execute("SELECT * FROM turmas")
#             data = cur.fetchall()
#         return render_template('public/index.html', data=data)
    
#     def post(self):
#         nome_turma = request.form['nome_turma']
    
#         with mysql.cursor() as cur:
#             cur.execute("INSERT INTO turmas(nome_turma) VALUES(%s)", (nome_turma))
#             cur.connection.commit()
#             return redirect('/')

# class DeleteTurmaController(MethodView):
 
#     def post(self, id_turma):
#         with mysql.cursor() as cur:
#             cur.execute("DELETE FROM turmas WHERE id_turma =%s", (id_turma))
#             cur.connection.commit()
#             return redirect('/')
    
# class UpdateTurmaController(MethodView):
#     def get(self, id_turma):
#         with mysql.cursor() as cur:
#             cur.execute("SELECT * FROM turmas WHERE id_turma =%s", (id_turma,))
#             turmas = cur.fetchone()
#             cur.connection.commit()
#             return render_template('public/updateTurma.html', turmas=turmas)
    
#     def post(self,id_turma):
#         nome_turma = request.form['nome_turma']
#         with mysql.cursor() as cur:
#             cur.execute("UPDATE turmas SET nome_turma =%s where id_turma = %s", (nome_turma, id_turma))
#             cur.connection.commit()
#             return redirect('/')

# class InsertDisciplinaController(MethodView):
#     def get(self):
#         with mysql.cursor() as cur:
#             dataD = cur.execute("SELECT * FROM disciplina")
#         return render_template('public/index.html', dataD=dataD)
    
#     def post(self):
#         nome_disciplina = request.form['nome_disciplina']
#         horario = request.form['horario']
    
#         with mysql.cursor() as cur:
#             cur.execute("INSERT INTO disciplina(nome_disciplina, horario) VALUES(%s, %s)", (nome_disciplina, horario))
#             cur.connection.commit()
#             return redirect('/')

# class DeleteDisciplinaController(MethodView):
 
#     def post(self, id_disciplina):
#         with mysql.cursor() as cur:
#             cur.execute("DELETE FROM disciplina WHERE id_disciplina =%s", (id_disciplina,))
#             cur.connection.commit()
#             return redirect('/')
    
# class UpdateDisciplinaController(MethodView):
#     def get(self, id_disciplina):
#         with mysql.cursor() as cur:
#             cur.execute("SELECT * FROM disciplina WHERE id_disciplina =%s", (id_disciplina,))
#             dataD = cur.fetchone()
#             cur.connection.commit()
#             return render_template('public/updateDisciplina.html', dataD=dataD)
    
#     def post(self,id_disciplina):
#         nome_disciplina = request.form['nome_disciplina']
#         horario = request.form['horario']

#         with mysql.cursor() as cur:
#             cur.execute("UPDATE disciplina SET nome_disciplina =%s and horario =%s  where id_disciplina = %s", (nome_disciplina, horario, id_disciplina))
#             cur.connection.commit()
#             return redirect('/')
