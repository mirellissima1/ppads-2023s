const mongoose =require('mongoose')


var schema = new mongoose.Schema({
    name:{
        type:String,
        required: true
    }
})

const Professordb = mongoose.model('professordb', schema);

module.exports = Professordb;