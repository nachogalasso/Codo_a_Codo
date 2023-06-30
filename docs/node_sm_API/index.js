const express = require('express');
const app = express();
const mongoose = require('mongoose');
const helmet = require('helmet');
const morgan = require('morgan');
const dotenv =require('dotenv');
const port = 8800

// Routes
const userRouter = require('./routes/users')
const authRouter = require('./routes/auth')

dotenv.config();
// app.listen(port, () => {
//     console.log(`El server tiene el port: ${port}`)
// })

// middleware
app.use(express.json());
app.use(helmet());
app.use(morgan("common"));

app.use('/api/users', userRouter);
app.use('/api/auth', authRouter);

// get pages, pero las vamos a crear en la carpeta routes
// app.get('/', (req, res) => {
//     res.send('Hello World')
// })


// conecting to database
mongoose.connect(process.env.MONGO_URI).then(() => {
    console.log('Conectado a Mongo')
    app.listen(port, () => {
        console.log(`El server tiene el port: ${port}`)
    })
}).catch((err) => {
    console.log(err);
})