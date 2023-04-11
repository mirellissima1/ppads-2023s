const mongoose =require('mongoose')

var schema = new mongoose.Schema({
    name:{
        type:String,
        required: true
    },
    horario:{
        type:String,
        required: false
    }
})

const Disciplinadb = mongoose.model('disciplinadb', schema);

module.exports = Disciplinadb;