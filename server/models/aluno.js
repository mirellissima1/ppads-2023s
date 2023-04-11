const mongoose =require('mongoose')


var schema = new mongoose.Schema({
    name:{
        type:String,
        required: true
    }
})

const Alunodb = mongoose.model('alunodb', schema);

module.exports = Alunodb;