require('dotenv').config();
const express = require('express');
const app = express();
const cors = require('cors');
const axios = require('axios').default;

const PORT = process.env.PORT || 8080;


app.use(express.json());
app.use(cors());


var cachedSessions = {};

function generateSequence(size,space=2){

    let sequence = "";
    for(let i = 0; i<size; i++){
        sequence += Math.floor(Math.random() * space) + 1;
    }

    return sequence;
    
}


app.get('/:size/:space', async (req, res) => {

    let sequence = generateSequence(req.params.size, req.params.space);

    res.send(sequence);

});



app.listen(PORT, () => {
    console.log(`App listening at http://localhost:${PORT}`)
});