const express = require('express')
require('./config')
const app = express()
const port = 5000
app.set("view engine", "ejs");
app.get('/', (req, res) => {
  res.render('visitorID.ejs')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})

/*const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const app = express();

// Middleware
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/registration', {
    useNewUrlParser: true,
    useUnifiedTopology: true
});
const db = mongoose.connection;

// Define User Schema
const userSchema = new mongoose.Schema({
    username: String,
    email: String,
    contact: String
});
const User = mongoose.model('User', userSchema);

// Routes
app.post('/register', (req, res) => {
    const { username, email, contact } = req.body;
    const newUser = new User({ username, email, contact });
    newUser.save((err, user) => {
        if (err) {
            res.status(500).send('Error registering new user.');
        } else {
            res.status(200).send('User registered successfully.');
        }
    });
});

// Start server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});*/