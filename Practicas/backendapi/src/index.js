// THIS IS SIMILAR A 'appexpress'
// import http from 'http';
// const server = http.createServer((req, res) => {
//    console.log('Un cliente se ha conectado');
//    res.writeHead(200, {"Content-type": "text/html; charset=utf-8"});
//    res.write('La conexion ha sido correcta')
//    res.end()
// })

// server.listen(3000, () => {
//    console.log('servidor a la espera de conexiones')
// })

// HERE IS WHERE WE ARE GONNA MAKE OUR DATABASE CODE
// username = movieapi
// password = s0ToAgULEktowNB7
// uri = mongodb+srv://movieapi:<password>@cluster0.hegsdaj.mongodb.net/?retryWrites=true&w=majority
// REMEMBER TO STORE THE PASS AND URI IN A VARIABLE

// NOW WE IMPORT OUR SERVER
import app from './server.js';
import mongoose from 'mongoose';
import mongodb from 'mongodb';
import ReviewsDAO from './dao/reviewsDAO.js'; // Interacting with the data base

// but we need to send the database connection to the ReviewsDAO and we will do it after the .then and before
// the app.listen


// DAO = Data Acces Object
const MongoClient = mongodb.MongoClient
const password = "s0ToAgULEktowNB7";
const dbname = "";
const uri = `mongodb+srv://movieapi:${password}@cluster0.hegsdaj.mongodb.net/${dbname}?retryWrites=true&w=majority`;
const port = 8000;

// MongoClient.connect( async (req, res) => {
//    try {
//       await main(),
//        {
//          maxPoolSize: 50, // max people connected at one time
//          wtimeoutMS: 2500, // time how long to try to connect before time got out
//          useNewURLParser: true 
//        }
//    }catch(err){
//       console.error(err.stack)
//       process.exit(1)
//    }
// })

MongoClient.connect(
   uri,
   {
      maxPoolSize: 50,
      wtimeoutMS: 2500,
      useNewURLParser: true
   })
   .catch(err => {
      console.error(err.stack);
      process.exit(1)
   })
   .then(async client => {
      // the function injectDB()
      await ReviewsDAO.injectDB(client)
      app.listen(port, () => {
         console.log(`listening on port ${port}`)
      })
   })