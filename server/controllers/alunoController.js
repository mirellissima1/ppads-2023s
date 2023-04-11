var Alunodb = require('../models/aluno');

//create and save

exports.create = (req, res) =>{
    if(!req.body){
        res.status(400).send({ message : "Content can not be empty!"});
        return;
    }

    const aluno = new Alunodb({
        name: req.body.name,
    })

    //salvar aluno no bd

    aluno
        .save(aluno)
        .then(data => {
            //res.send(data)
            res.redirect('/add-turma');
        })
        .catch(err =>{
                    res.status(500).send({
                        message : err.message || "Some error occurred while creating a create operation"
                    });
                });
}

//return todas os alunos e uma somente

exports.find = (req, res) =>{

    if(req.query.id){
        const id = req.query.id;

       Alunodb.findById(id)
            .then(data =>{
                if(!data){
                    res.status(404).send({ message : "Not found aluno with id "+ id})
                }else{
                    res.send(data)
                }
            })
            .catch(err =>{
                res.status(500).send({ message: "Erro retrieving aluno with id " + id})
            })

    }else{
        Alunodb.find()
            .then(aluno => {
                res.send(aluno)
            })
            .catch(err => {
                res.status(500).send({ message : err.message || "Error Occurred while retriving aluno information" })
            })
    }
}

//Update Aluno

exports.update = (req, res) =>{
    if(!req.body){
        return res
            .status(400)
            .send({ message : "Data to update can not be empty"})
    }

    const id = req.params.id;
    Alunodb.findByIdAndUpdate(id, req.body, { useFindAndModify: false})
        .then(data => {
            if(!data){
                res.status(404).send({ message : "Cannot Update aluno with ${id}. Maybe turma not found!"})
            }else{
                res.send(data)
            }
        })
        .catch(err =>{
            res.status(500).send({ message : "Error Update aluno information"})
        })
}

//Delete Aluno

exports.delete = (req, res) =>{
    const id = req.params.id;
    Alunodb.findByIdAndDelete(id)
    .then(data => {
        if(!data){
            res.status(404).send({ message : "Cannot Delete with id ${id}. Maybe id is wrong"})
        }else{
            res.send({
                message : "aluno was deleted successfully!"
            })
        }
    })
    .catch(err =>{
        res.status(500).send({
            message: "Could not delete aluno with id=" + id
        });
    });
}