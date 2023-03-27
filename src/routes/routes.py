from src.controllers.errors import *
from src.controllers.turmaController import *
from src.controllers.disciplinaController import *
from src.controllers.professoresController import *
from src.controllers.alunosController import *

routes = {
    "index_route": "/","indexcontroller": InsertTurmaController.as_view("home"),
    "delete_turma_route": "/delete/turmas/<int:id_turma>","delete_turma_controller": DeleteTurmaController.as_view("delete"),
    "update_turma_route": "/update/turmas/<int:id_turma>","update_turma_controller": UpdateTurmaController.as_view("update"),
    "insert_disciplina_route": "/insertDisciplina","insertdisciplinacontroller": InsertDisciplinaController.as_view("InsertDisc"),
    "delete_disciplina_route": "/delete/disciplinas/<int:id_disciplina>","delete_disciplina_controller": DeleteDisciplinaController.as_view("deleteDisc"),
    "update_disciplina_route": "/update/disciplinas/<int:id_disciplina>","update_disciplina_controller": UpdateDisciplinaController.as_view("updateDisc"),
    
     "insert_professores_route": "/InsertProfessor","insert_professores_controller": InsertProfessoresController.as_view("insertProf"),
    "delete_professores_route": "/delete/professores/<int:id_professores>","delete_professores_controller": DeleteProfessoresController.as_view("deleteProf"),
    "update_professores_route": "/update/professores/<int:id_professores>","update_professores_controller": UpdateProfessoresController.as_view("updateProf"),
    
    "insert_alunos_route": "/InsertAluno","insert_alunos_controller": InsertAlunosController.as_view("insertAluno"),
    "delete_alunos_route": "/delete/alunos/<int:id_alunos>","delete_alunos_controller": DeleteAlunosController.as_view("deleteAluno"),
    "update_alunos_route": "/update/alunos/<int:id_alunos>","update_alunos_controller": UpdateAlunosController.as_view("updateAluno"),
    "not_found": 404, "not_found_controller": NotFoundController.as_view("not_found"),
}