const express = require('express');
const mysql = require('mysql');
const app = express();

const db = mysql.createConnection({
    host: 'localhost',
    user: 'your_username',
    password: 'your_password',
    database: 'public_data'
});

db.connect();

app.get('/api/data', (req, res) => {
    db.query('SELECT * FROM api_data', (error, results) => {
        if (error) throw error;
        res.json(results);
    });
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
