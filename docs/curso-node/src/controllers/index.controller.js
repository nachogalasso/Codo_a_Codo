// Aqui construimos nuestra función controladora. Para ello vamos a tomar el (req, res) de la función .get() de
// nuestro archivo index.routes. 
// Para los controladores tenemos que crear un objeto que podamos exportar, sera el que contenga todas
// las funcionalidades para controlar el index.routes

const controller = {}

// Para PUG
// recordar del texto colocarlo como string
const title = "INDEX DESDE EL SERVIDOR con pug Y una VARIABLE";

// controller.name = 'Pepe'; - Aqui le asignamos una propiedad
// controller.saludar = () => console.log('Hola'); - Aquí le asignamos un método
// controller.saludar() - si ejecutamos eso veremos que nos sale un Hola en la consola
// ahora construimos nuestra función:
controller.index = (req, res) => {
   // res.send('La conexión ha sido correcta desde index.controller')
   // ahora vamos a renderizar el mensaje con la plantilla de pug
   // res.render('index'), pero ahora le vamos a agregar las variables que lo hacemos mediante un objeto
   res.render('index', {title}) // podemos colocar tambien {title:title}

};
// (req, res) => {
//    res.send('La conexión ha sido correcta')
// }

// Ahora lo exportamos y lo importamos en index.routes
export default controller

// Cambiamos la respuesta por el index creado con la plantilla de pug. Al utilizar res.render(), express ya sabe
// dónde tiene que buscar, debido a que se lo indicamos con app.set en appexpress.js, por lo tanto no es necesaria
// colocar toda la ruta, pero si le tenemos que indicar que archivo debe abrir y por ello es el que le indicamos
// dentro de los ('') de render. Hasta aqui estamos utilizando un motor de plantillas, pero no tenemos contenido
// dinámico. Esto también lo podriamos haber hecho con HTML.
// Para hacerlo dinámico tenemos que abrir un objeto e indicarle las variables.
// app.render('index', {variables})
// Las variables las podemos crear por fuera con la sintaxis misma de JS. Luego en index.pug le tenemos que 
// indicar dónde vamos a utilizar esa variable. 
// En pug entonces en h1 colocamos => hi title... es importante dejar el espacio, al igual que la indentación, 
// sino tendremos conflictos.