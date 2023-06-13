// 1.- console.log('Hello world') Para correrlo creamos en el package.json en la parte de scripts el comando para correr
// sin inconvenientes nuestro arhivo con el comando npm run serve

// 2.- Tenemos que instalar express en nuestro proyecto => npm i express
// (no olvidar visitar la doc npmjs.com y expressjs.com)
// recordar que para los cambios tenemos que cerrar y abrir el server

// 3.- SE RECOMIENDA USAR POSTMAN, tambien instalar nodemon para no tener que andar recargando el server x cambios
// luego tenemos que crear en el JSON un comando para correr el server desde nodemon => npm run dev

const password = require('./node_API_pass')
const express = require('express');
// para conectar con mongodb
const mongoose = require('mongoose');
const app = express();
const port = 3000

// importamos el modelo Product para poder trabajar con él
const Product = require('./models/productModel')

// tenemos que utilizar un middleware para que nuestro API pueda entender los JSON. Veremos que el método POST
// funciona sin inconvenientes
app.use(express.json())
// utilizamos otro tipo de codificación para modificar nuestros productos
app.use(express.urlencoded({ extended: false}));
// ahora tenemos que crear nuestra app
// Con app.get le especificamos al ruta que queremos que utilice para que se pueda ver en nuestro navegador
// req = request => es lo que nos solicita el cliente
// res = response => es lo que responde nuestro server al req del cliente
app.get('/', (req, res) => {
    res.send('Hello world');
})

app.get('/prueba', (req, res) => {
    res.send('Probamos el nodemon, guachin');
})

// ahora traemos los datos de nuestra base
app.get('/products', async (req, res) => {
    try {
        // al colocar .find({}) llamamos a todos los productos.
        const products = await Product.find({})
        res.status(200).json(products)
    } catch (err) {
        res.status(500).json({message: err.message});
    }
})

// para obtener el producto mediante el id
app.get('/products/:id', async (req, res) => {
    try {
        // para obtener el id de nuestros productos
        const {id} = req.params;
        const product = await Product.findById(id);
        res.status(200).json(product)
    } catch (err) {
        res.status(500).json({message: err.message});
    }
})

// Ahora tratamos resolvermos el ingreso de datos del usuario para que se almacene en la base de datos.
// app.post('/product', (req, res) => {
//     console.log(req.body)
//     // no olvidar poner la respuesta
//     res.send(req.body);
// })
// Ahora utilizamos un formulario
app.post('/products', async (req, res) => {
    try {
        const product = await Product.create(req.body);
        res.status(200).json(product);

    } catch (err) {
        console.log(err.message);
        res.status(500).json({message: err.message});
    }
})

// Vamos a crear un update y delete de los productos en nuestra base de mongodb
app.put('/products/:id', async (req, res) => {
    try {
        const {id} = req.params;
        // acá tenemos que pasar 2 datos, uno es el id y el otro es el req.body para modificar todo completo
        const product = await Product.findByIdAndUpdate(id, req.body);
        // luego tenemos que confirmar si el producto fué modificado o no
        if(!product) {
            return res.status(404).json({message: `No encontramos el producto con ID: ${id}, guachin`})
        }
        // para que actualice de una
        const updateProduct = await Product.findById(id);
        res.status(200).json(updateProduct);
    } catch (err) {
        res.status(500).json({message: err.message});
    }
})

// Para eliminar un producto
app.delete('/products/:id', async (req, res) => {
    try {
        const {id} = req.params;
        const product = await Product.findByIdAndDelete(id);
        if(!product) {
            return res.status(404).json({message: `No encontramos el producto con ID: ${id}, guachin`})
        }
        res.status(200).json(product);
    } catch (err) {
        res.status(500).json({message: err.message});
    }
})

// Con app.listen, le estamos indicando el puerto que tiene que utilizar el port, lo podemos hacer variable para que
// luego se pueda modificar sin inconvenientes
// app.listen(port, () => {
//     console.log(`El server tiene el port: ${port}`)
// })

mongoose.
connect(`mongodb+srv://admin:${password}@cluster0.ml7fvj6.mongodb.net/CRUD-API_NODE?retryWrites=true&w=majority`)
.then(() => {
    console.log('Conectado a Mongo')
    app.listen(port, () => {
        console.log(`El server tiene el port: ${port}`)
    })
}).catch((err) => {
    console.log(err);
})

// 4.- CONECTAMOS MONGODB
// Para conectar con mongodb tenemos que utilizar mongoose npm i mongoose (no olvidar detener el server)
// veremos que en la web de npmjs nos indica cómo debemos crear la instancia para conectarlo.
// mongodb+srv://admin:<password>@cluster0.ml7fvj6.mongodb.net/?retryWrites=true&w=majority
// Replace <password> with the password for the admin user

// mongoose.
// connect('mongodb+srv://admin:nakio789@cluster0.ml7fvj6.mongodb.net/CRUD-API_NODE?retryWrites=true&w=majority')
// .then(() => {
//     console.log('Conectado a Mongo')
// }).catch((err) => {
//     console.log(err);
// })
// Como queremos que se conecte antes del listen lo vamos a pasar arriba.

// 5.- Ahora que hacemos nuestro modelo de base de datos vamos a crear la carpeta model y en ella creamos un archivo.js
// en este archivo tendremos que incluir tambien a mongoose