const mongoose =require('mongoose')

var schema = new mongoose.Schema({
    name:{
        type:String,
        required: true
    }
})

const Turmadb = mongoose.model('turmadb', schema);

module.exports = Turmadb;