// Aquí necesitamos importar express y luego en app tendremos que utilizar un módulo que nos proporciona express
import express from 'express'
// const express = require('express')
// para utilizar el módulo de las rutas utilizamos express.Router() en vez de la función completa de express()
const router = express.Router()
// traemos el controller del index.controller
import controller from '../controllers/index.controller.js'
// const controller = require('../controllers/index.controller.js')


// Ahora configuramos la función de requerimiento y respuesta. A diferencia del anterior que usabamos app, ahora
// utilizamos nuestra constante 'router'
// RECORDAR QUE LA FUNCIÓN SE ESCRIBE DE LA SIGUENTE MANERA:
// element.get('ruta/', (function) => {}); --- ruta: '/' y function: (req, res)

// router.get('/', (req, res) => {
//    res.send(`La conexión ha sido correcta desde index.routes`);
// })
// La función ahora estará en el index.controller ->
router.get('/', controller.index);

// Una vez que tenemos esto, lo tenemos que conectar con nuestro archivo app. Para ello tenemos que exportar
// nuestra constante 'router'
// module.exports = router;
export default router
// lo que estamos haciendo es que todo lo que esté en router se pueda exportar y se pueda utilizar en cualquier
// otro archivo. En ese otro archivo que lo exportemos tendremos que indicarle la ruta donde se encuentra nuestro
// archivo de conexión tenemos que ponerlo dentro de una constante
// const routes = require('./routes/index.routes')
// Luego tenemos que decirle a express que lo utilice.

// PARA EXPORTAR NUESTRO ARCHIVO Y PODER USARLO EN OTROS LUGARES TENEMOS QUE UTILIZAR EL COMANDO:
// "export default router"