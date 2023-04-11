const express = require('express');
const route = express.Router();

const services = require('../services/render')

const controllerTurma = require('../controllers/turmaController')

const controllerAluno = require('../controllers/alunoController')

const controllerProfessor = require('../controllers/professorController')

const controllerDisciplina = require('../controllers/disciplinaController')


/**
 * @description Root Route
 * @method GET
 */
route.get('/', services.homeRoutesT);

route.get('/', services.homeRoutesD);


route.get('/add-turma', services.add_turma)

route.get('/add-disciplina', services.add_disciplina)

route.get('/add-professor', services.add_professor)

route.get('/add-aluno', services.add_aluno)


route.get('/update-turma', services.update_turma)
route.get('/update-aluno', services.update_aluno)

route.get('/update-professor', services.update_professor)

route.get('/update-disciplina', services.update_disciplina)

//API

route.post('/api/turmas', controllerTurma.create);
route.get('/api/turmas', controllerTurma.find);
route.put('/api/turmas/:id', controllerTurma.update);
route.delete('/api/turmas/:id', controllerTurma.delete);

route.post('/api/alunos', controllerAluno.create);
route.get('/api/alunos', controllerAluno.find);
route.put('/api/alunos/:id', controllerAluno.update);
route.delete('/api/alunos/:id', controllerAluno.delete);

route.post('/api/disciplinas', controllerDisciplina.create);
route.get('/api/disciplinas', controllerDisciplina.find);
route.put('/api/disciplinas/:id', controllerDisciplina.update);
route.delete('/api/disciplinas/:id', controllerDisciplina.delete);

route.post('/api/professores', controllerProfessor.create);
route.get('/api/professores', controllerProfessor.find);
route.put('/api/professores/:id', controllerProfessor.update);
route.delete('/api/professores/:id', controllerProfessor.delete);



module.exports = route;