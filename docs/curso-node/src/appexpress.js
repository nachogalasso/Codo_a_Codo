// RECORDAR QUE LOS CAMBIOS EN EL SERVIDOR SON LOS QUE REQUIEREN QUE PAREMOS EL MISMO Y LO VOLVAMOS
// A LEVANTAR PARA QUE PODAMOS VER LOS MISMOS.

// req = request -> petición del cliente
// res = response -> es la respuesta del servidor
// cliente = navegador

// ARMAMOS UN SERVIDOR CON EXPRESS
// EXPRESS es una estructura para node, lo que hace es interactuar con nuestro módulo HTTP, nos evita escribir
// mucho más código. Nos facilita poder crear el servidor.
// No es un modulo que viene por defecto, por lo tanto lo tenemos que INSTALAR -> "npm install express"
// vamos a usar EXPRESS cuando el cliente interactue con nuestro servidor
// recordar que como el anterior, aquí también tendremos que crear nuestra variable

// const express = require("express");
import express from 'express';
// express tiene la particularidad de que lo tenemos ejecutarlo para que nos devuelva el objeto que contiene toda
// la información del framework. Lo normal es poner el comando const app = express(), con el fin de que lo ejecute
// como una función. De tal modo tenemos todo el objeto de express, junto a propiedades y métodos dentro de la
// variable app. Luego lo tratamos como el HTTP
const app = express();
// ya no es necesario el createServer, solamente con el .listen() el servidor comienza a correr, recordar que
// dentro del mismo también tenemos que indicarle el número de servidor y luego la función de lo que debe hacer
// el servidor está a la espera del cliente. Ahora veremos los métodos de respuesta que tiene nuestro servidor
// ellos son: GET, POST, PUT y DELETE (son los verbos de conexion que existen)
// como esperamos una conexion por la URL utilizamos GET, la cual lleva 2 parámetros, el 1ro le indicamos por
// dónde van a entrar los datos, '/' equivale al localhost y luego la función que queremos que se ejecute, al
// igual que con HTTP, aquí es donde viene (req, res)

//  RECORDAR QUE CON CTRL + C PARAMOS EL SERVIDOR
// Ahora lo traemos desde routes/index.routes.
// app.get('/', (req, res) => {
//    res.send('La conexion ha sido correcta')
// })

// De la siguiente forma estamos importando nuestro archivo con la ruta desde 'index.routes.js', con el fin de que
// nuestro servidor funcione
// const routes = require("./routes/index.routes");
// puedo utilizar router o routes para importar nuestro index.routes
import routes from './routes/index.routes.js'
// Ahora tenemos que indicarle a express que lo utilice
app.use(routes);
// también podemos utilizar app.use(require('./routes/index.routes'));
// como el archivo app ahora está dentro de la carpeta 'src' tenemos que indicarle a node al momento de levantar
// el servidor -> node src/app
// app.use(require('./routes/index.routes'));

// CUANDO ENVIAMOS ARCHIVOS ESTÁTICOS
// Volvemos a crear una function app.use(), pero ahora le agregamos nuestra ruta de la web estática
// app.use((req, res) => {})

// RUTES FOR STATIC FILES
// tenemos que usar la function que nos proporciona express app.use(express.static('')). Tener en cuenta que las
// rutas no funcionan solamente con poner './public' o '../public'. Lo que tenemos que usar son rutas ABSOLUTAS
// __dirname es una constante que ya tenemos en node. Nos indica la ruta en donde estamos y por ello la podemos
// utilizar para indicarle a Node dónde se encuentra nuestran nuestros archivos 'statics'.
// tenemos que usar también el módulo const path = require('path') que se encarga de normalizar las rutas ya que
// las / no son todas iguales en los distintos sistemas operativos
// const path = require('path')

// ESTO ES LO QUE DEBO AGREGAR PARA PODER LLAMAR A LAS RUTAS ABSOLUTAS
import path from 'path' // con esto normalizamos las rutas
import { fileURLToPath } from 'url'
const __dirname = path.dirname(fileURLToPath(import.meta.url))

// PARA UTILIZAR PUG
// ahora express-node está configurado para utilizar el motor de plantillas de pug
app.set('view engine', 'pug')
// le indicamos dónde es encuentra la carpeta
app.set('views', path.join(__dirname, '/views'))

app.use(express.static(path.join(__dirname, '../public')))
// acá le indicamos donde se ejecuta app y dónde tiene que buscar las archivos estáticos

// OTRA Forma
// app.get('css/style.css', (req, res) => {
//    res.sendFile(path.join(__dirname, 'public', 'css', 'style.css'))
// })

// es importante indicarle la ruta del HTML. La misma tiene que ser absoluta. Estas rutas se realizan de una
// forma especial. Tenemos que crear una ruta para los archivos estáticos
// res.sendFile('index-html')
app.use('/', (req, res) => {
   // res.sendFile('../public/index.html');
   // PARA QUE FUNCIONE TENGO QUE PONER EL COMENDO SIGUIENTE
   res.sendFile(path.join(__dirname, '../public/404.html'))
   // OTRA OPCION
   // res.status(404).sendFile(path.join(__dirname, 'index.html'))
})

app.listen(3000, () => {
   console.log("Servidor a la espera de conexiones");
});

// Normalmente el tema de las rutas no se tiene en el app, sino que se modulariza y se tiene por separado y luego
// se tiene que estructurar. Para ello creamos una carpeta con el nombre "src"que es la que va a contener todo el
// código fuente de nuestro servidor. Luego creamos unas carpetas para las rutas y otras para las funciones que se
// van a ejecutar. Dentro de 'src' creamos las carpetas 'ROUTES' y la otra 'CONTROLLERS'. Una vez que las tenemos
// debemos separar el app y la función en 2 archivos distintos. En 'routes' creamos el archivo "index.routes.js".
// Podemos colocarle el nombre que querramos, pero por convención conviene usar ese. Si usamos ruotes para una
// página de contacto en todo caso entonces utilizamos "contacts.routes.js" y así con las demás, especificando al
// principio a cual página se refieren, si tenemos un problema con una ruta o un controlador sabemos dónde mirar.


// PARA RENDERIZAR UNA WEB, TENEMOS QUE CREAR UNA CARPETA POR FUERA DE SRC QUE SE LLAME 'PUBLIC'
// EN ELLA ES DONDE PONDREMOS LOS ARCHIVOS DE CSS, IMÁGENES, MUSICA O HTML, PERO EN ELLA COLOCAMOS
// TODOS AQUELLOS ARCHIVOS QUE NO VAN A CAMBIAR, O SEA, NO SON DINÁMICOS. SI LAS COSAS SE VAN A 
// MODIFICAR EN TIEMPO REAL, EN ESOS CASOS UTILIZAMOS UN MOTOR DE PLANTILLAS

// Los motores de plantillas nos permiten generar contenido HTML de manera dinámica, podemos usar condicionales,
// bucles, variables y todas esas cosas que en HTML no se pueden usar. Con Node y los motores de plantillas
// podremos generar contenido dinámico, enviando información desde el servidor al cliente. Esto nos permite por
// ejemplo recuperar unos datos de un base de datos y presentarlos al cliente de forma de HTML. RECORDAR QUE
// Tenemos que elegir algunos de los motores de plantillas, uno de ellos es PUG, para ello tenemos que instalarlo
// en nuestro proyecto => 'npm install pug' (indispensable que sea dependencia de producción). Ya que vamos a
// generar el HTML en función de lo que nos solicite el cliente, no vamos a tener todo armado. Entonces lo que nos
// pida, generamos el HTML y se lo enviamos. 
// Una vez instalado el pug, le tenemos que indicar a Node que lo utilize, para ello utilizamos app.set()
// con app.set('view engine') le asignamos un motor de plantillas y luego separado con una coma, le indicamos
// el que vamos a utilizar, que en este caso es pug => app.set('view engine', 'pug'). Si usamos otro tendremos que
// indicarlo así como lo hicimos con pug.
// AHORA DENTRO DE LA CARPETA SRC, creamos la carpeta 'VIEWS', aquí es donde vamos a guardar las views que
// se van a renderizar cuando el cliente nos las pida. No olvidar que le tenemos que indicar a express dónde se
// encuentra para que así la pueda utilizar. app.set('views'), el "views" no se refiere a la carpeta, sino que es 
// el parámetro para asignar las vistas, ese primer parámetro no se puede cambiar, pero el nombre de la carpeta si
// luego le indicamos dónde tiene esa carpeta que es en path.join(__dirname, 'views'). De esta manera le indicamos
// la ruta de la carpeta. Ahora dentro de ella creamos un index.pug. Luego emmet nos genera la plantilla básica. 
// Una vez que tenemos esto le tenemos que indicar a nuestro controlador que renderize este elemento.
// Para ello vamos a index.controller, que como antes enviábamos un mensaje, ahora lo cambiamos para que renderize
// nuestra plantilla de pug dentro de views