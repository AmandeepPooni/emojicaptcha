require('dotenv').config();
const express = require('express');
const app = express();
const cors = require('cors');
const axios = require('axios').default;

const PORT = process.env.PORT || 8080;


app.use(express.json());
app.use(cors());


var cachedSessions = {};


app.get('/api', async (req, res) => {
    res.send("frrrrrrrrrrrrr frf rf frrrrrrrrrrrrrrrrrr");
});



app.listen(PORT, () => {
    console.log(`App listening at http://localhost:${PORT}`)
});