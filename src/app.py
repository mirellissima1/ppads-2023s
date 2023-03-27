from flask import Flask
from src.routes.routes import *

app = Flask(__name__)

app.add_url_rule(routes["index_route"], view_func=routes["indexcontroller"])

app.add_url_rule(routes["delete_turma_route"], view_func=routes["delete_turma_controller"])

app.add_url_rule(routes["update_turma_route"], view_func=routes["update_turma_controller"])

app.add_url_rule(routes["insert_disciplina_route"], view_func=routes["insertdisciplinacontroller"])

app.add_url_rule(routes["delete_disciplina_route"], view_func=routes["delete_disciplina_controller"])

app.add_url_rule(routes["update_disciplina_route"], view_func=routes["update_disciplina_controller"])

app.add_url_rule(routes["insert_professores_route"], view_func=routes["insert_professores_controller"])

app.add_url_rule(routes["delete_professores_route"], view_func=routes["delete_professores_controller"])

app.add_url_rule(routes["update_professores_route"], view_func=routes["update_professores_controller"])

app.add_url_rule(routes["insert_alunos_route"], view_func=routes["insert_alunos_controller"])

app.add_url_rule(routes["delete_alunos_route"], view_func=routes["delete_alunos_controller"])

app.add_url_rule(routes["update_alunos_route"], view_func=routes["update_alunos_controller"])

app.register_error_handler(routes["not_found"],routes["not_found_controller"])
