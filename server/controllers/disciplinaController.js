var Disciplinadb = require('../models/disciplina');
//create and save

exports.create = (req, res) =>{
    if(!req.body){
        res.status(400).send({ message : "Content can not be emtpy!"});
        return;
    }

    const disciplina = new Disciplinadb({
        name : req.body.name,
        horario: req.body.horario
    })

    // save disciplina in the database
    disciplina
        .save(disciplina)
        .then(data => {
            res.send(data)
            // res.redirect('/add-disciplina');
        })
        .catch(err =>{
            res.status(500).send({
                message : err.message || "Some error occurred while creating a create operation"
            });
        });
}

//return todas as disciplinas e uma somente

exports.find = (req, res) =>{
    
    if(req.query.id){
        const id = req.query.id;

        Disciplinadb.findById(id)
            .then(data =>{
                if(!data){
                    res.status(404).send({ message : "Not found disciplina with id "+ id})
                }else{
                    res.send(data)
                }
            })
            .catch(err =>{
                res.status(500).send({ message: "Erro retrieving disciplina with id " + id})
            })

    }else{
        Disciplinadb.find()
            .then(disciplina => {
                res.send(disciplina)
            })
            .catch(err => {
                res.status(500).send({ message : err.message || "Error Occurred while retriving disciplina information" })
            })
    }
}

//Update disciplina

exports.update = (req, res) =>{
    if(!req.body){
        return res
            .status(400)
            .send({ message : "Data to update can not be empty"})
    }

    const id = req.params.id;
    Disciplinadb.findByIdAndUpdate(id, req.body, { useFindAndModify: false})
        .then(data => {
            if(!data){
                res.status(404).send({ message : `Cannot Update disciplina with ${id}. Maybe turma not found!`})
            }else{
                res.send(data)
            }
        })
        .catch(err =>{
            res.status(500).send({ message : "Error Update disciplina information"})
        })
}

//Delete disciplina

exports.delete = (req, res) =>{
    Disciplinadb.findByIdAndDelete(id)
    .then(data => {
        if(!data){
            res.status(404).send({ message : `Cannot Delete with id ${id}. Maybe id is wrong`})
        }else{
            res.send({
                message : "disciplina was deleted successfully!"
            })
        }
    })
    .catch(err =>{
        res.status(500).send({
            message: "Could not delete disciplina with id=" + id
        });
    });
}