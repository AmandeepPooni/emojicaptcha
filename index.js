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



// fetch("http://localhost:8080/emotion", {
// method: "POST",
// headers: {
//     'Content-Type': 'application/json'
// },
// body: JSON.stringify({imgurl:"https://firebasestorage.googleapis.com/v0/b/emojicaptcha.appspot.com/o/tests%2Fhappy2.webp?alt=media&token=9a277a07-3a82-4edf-9dff-b076cd1958df"})
// })
// .then((resp) => resp.json())
// .then((resp) => console.log(resp))
// .catch((error) => {
//     console.log(error);
//     return null
// });