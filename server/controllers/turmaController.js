var Turmadb = require('../models/turma');

//create and save

exports.create = (req, res) =>{
    if(!req.body){
        res.status(400).send({ message : "Content can not be emtpy!"});
        return;
    }

    const turma = new Turmadb({
        name : req.body.name,
    
    })

    // save turma in the database
    turma
        .save(turma)
        .then(data => {
            // res.send(data)
            res.redirect('/add-turma');
        })
        .catch(err =>{
            res.status(500).send({
                message : err.message || "Some error occurred while creating a create operation"
            });
        });
}

//return todas as turmas e uma somente

exports.find = (req, res) =>{
    
    if(req.query.id){
        const id = req.query.id;

       Turmadb.findById(id)
            .then(data =>{
                if(!data){
                    res.status(404).send({ message : "Not found turma with id "+ id})
                }else{
                    res.send(data)
                }
            })
            .catch(err =>{
                res.status(500).send({ message: "Erro retrieving turma with id " + id})
            })

    }else{
        Turmadb.find()
            .then(turma => {
                res.send(turma)
            })
            .catch(err => {
                res.status(500).send({ message : err.message || "Error Occurred while retriving turma information" })
            })
    }
}

//Update Turma

exports.update = (req, res) =>{
    if(!req.body){
        return res
            .status(400)
            .send({ message : "Data to update can not be empty"})
    }

    const id = req.params.id;
    Turmadb.findByIdAndUpdate(id, req.body, { useFindAndModify: false})
        .then(data => {
            if(!data){
                res.status(404).send({ message : `Cannot Update turma with ${id}. Maybe turma not found!`})
            }else{
                res.send(data)
            }
        })
        .catch(err =>{
            res.status(500).send({ message : "Error Update turma information"})
        })
}

//Delete Turma

exports.delete = (req, res) =>{
    const id = req.params.id;
    Turmadb.findByIdAndDelete(id)
    .then(data => {
        if(!data){
            res.status(404).send({ message : `Cannot Delete with id ${id}. Maybe id is wrong`})
        }else{
            res.send({
                message : "turma was deleted successfully!"
            })
        }
    })
    .catch(err =>{
        res.status(500).send({
            message: "Could not delete turma with id=" + id
        });
    });
}