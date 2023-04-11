var professor = require('../models/professor');

//create and save

exports.create = (req, res) =>{
    if(!req.body){
        res.status(400).send({ message : "Content can not be emtpy!"});
        return;
    }

    const professor = new professor({
        name : req.body.name,

    })

    // save professor in the database
    professor
        .save(professor)
        .then(data => {
            res.send(data)
            // res.redirect('/add-professor');
        })
        .catch(err =>{
            res.status(500).send({
                message : err.message || "Some error occurred while creating a create operation"
            });
        });
}

//return todos professores e uma somente

exports.find = (req, res) =>{

    if(req.query.id){
        const id = req.query.id;

       professor.findById(id)
            .then(data =>{
                if(!data){
                    res.status(404).send({ message : "Not found professor with id "+ id})
                }else{
                    res.send(data)
                }
            })
            .catch(err =>{
                res.status(500).send({ message: "Erro retrieving professor with id " + id})
            })

    }else{
        professor.find()
            .then(professor => {
                res.send(professor)
            })
            .catch(err => {
                res.status(500).send({ message : err.message || "Error Occurred while retriving professor information" })
            })
    }
}

//Update professor

exports.update = (req, res) =>{
    if(!req.body){
        return res
            .status(400)
            .send({ message : "Data to update can not be empty"})
    }

    const id = req.params.id;
    professor.findByIdAndUpdate(id, req.body, { useFindAndModify: false})
        .then(data => {
            if(!data){
                res.status(404).send({ message : "Cannot Update professor with ${id}. Maybe turma not found!"})
            }else{
                res.send(data)
            }
        })
        .catch(err =>{
            res.status(500).send({ message : "Error Update professor information"})
        })
}

//Delete Professor

exports.delete = (req, res) =>{
    const id = req.params.id;
    professor.findByIdAndDelete(id)
    .then(data => {
        if(!data){
            res.status(404).send({ message : `Cannot Delete with id ${id}. Maybe id is wrong`})
        }else{
            res.send({
                message : "professor was deleted successfully!"
            })
        }
    })
    .catch(err =>{
        res.status(500).send({
            message: "Could not delete professor with id=" + id
        });
    });
}