// PRIMEROS PASOS
// Recordar que con 'npm init' se crea el archivo json y si usamos 'npm init --yes' nos evitamos las preguntas.
// const numbers = [1, 2, 3, 4, 5]

// console.log(numbers)
// numbers.forEach(number => console.log(number * 2)) recordar que se imprime en la terminal

// código para imprimir con colores en la consola
// console.log('\x1b[36m%s\x1b[0m', 'I am cyan')
// numbers.forEach((number) => console.log("\x1b[36m%s\x1b[0m", number * 2));

// RECORDAR QUE CADA VEZ QUE QUIERA UTILIZAR EL NODE TENGO QUE IR A LA CARPETA!!!

// TENER EN CUENTA QUE NODE TODAVÍA NO SOPORTA LOS MODULES Y POR ELLO NO PODEMOS USAR LOS IMPORT
// la versión antigua es usar el 'require'
// const chalk = require('chalk')
// import chalk from 'chalk';
// console.log(chalk.red("Hello world!"));


// si queremos ver nuestro proyecto en la terminal, tenemos que abrir una y utilizar la palabra node + nombre del 
// archivo, sin el .js por lo tanto si tenemos algo en el console.log veremos que nos sale en la terminal
// Recordar que el nombre de las carpetas tiene que ser sin espacios y en minúsculas, de lo contrario tendremos
// errores. Podemos usar el -
// Para iniciar un paquete JSON en la terminal tendremos que usar el comando "npm init" y luego responder una
// serie de preguntas. En la versión por defecto sale la 1.0.0 que viene de lo siguiente => 
// Semantinc versioning = MAJOR.MINOR.PATH
// PATH => último valor, refiere a cambios pequeños o menores de algo que no funcionaba
// MINOR => valor del medio, cambio menor que no debería causar conflictos con otras versiones
// MAJOR => primer valor, cuando se realiza un cambio grande en nuestra app, puede traer problemas de versiones
// descripción se refiere a explicar lo que hace o es nuestro proyecto
// El entrypoint es el punto de inicio del proyecto.  

// const numbers sería una dependencia de producción ya que todos la pueden ver, pero eso no va en el package.json
// allí es donde colocamos las dependencias. Por ejemplo una dependencia de producción sería React, necesitamos
// que esté ese código para poder utilizarlo. En una dependencia de desarrollo podría ser autoprefixed, con el 
// de agregar los prefijos de cada navegador.
// Si queremos instalar esas dependencias tenemos que usar el "npm install + el nombre de la dependencia". Con
// YARN funciona de otra forma

// chalk es una libreria que nos permite simplificar las cosas
// npm i = a escribir npm 'install' es la forma reducida colocar solamente la i
// si en el package.json dice 'dependencias' se refiere solamente a la producción, pero si nos aparece como
// 'devDependencies' entonces hace referencia a las de desarrollo. Siempre nos indica en que versión se encuentra
// que en todo caso de ser necesario se tendría que actualizar
// veremos que en la web nos indica cómo utilizar una librería y los comandos que tenemos que utilizar para que
// funcione.

// Cuando instalamos un módulo, lo que hace también node es leer las dependencias de ese módulo e instalarlas 
// también, pero lo único que se instala son las dependencias de desarrollo, no las de producción. Entender que
// node va a recorrer todas las ramas hasta instalar las necesarias, de lo que nosotros necesitamos. Recordar que 
// nos instala las dependencias de producción, no las de desarrollo. Lo que se nos instala, por lo general no 
// tenemos que tocarlo, pero eso no significa que lo tenemos que ignorar.
// 'node_modules' es una carpeta que NUNCA tenemos que subir o compartir. Además es la carpeta que más pesa del
// proyecto. Mientras que package-lock es un archivo de seguimiento de las dependencias.

// En la documentación de Node, podemos ver todas las librerias que tenemos instaladas y a las cuales no es
// necesario realizar un 'npm install'. Para el caso del servidor vamos a utilizar la HTTP

// Si tengo que desinstalar algo puedo utilizar 'npm uninstall + nombre del archivo'
// también el siguiente comando 'npx rimraf + nombre del archivo o carpeta'

// HACIENDO UN SERVIDOR - utilizando ctrl + c detenemos nuestro servidor
// 1ro requerimos el modulo
import http from 'http';

// 2do guardamos el server en una variable
// createServer es una función que recibe como parámetro otra función y por ello es createServer(() => {})
// los servidores requieren de 2 parámetros que son muy importantes, siempre vamos a necesitar ambos:
// req = request -> petición del cliente
// res = response -> es la respuesta del servidor
// cliente = navegador
const server = http.createServer((req, res) => {
   // para saber si el servidor funciona podemos hacer un console.log
   console.log('Un cliente se ha conectado')
   // para el UTF-8 podemos colocar el siguiente comando
   res.writeHead(200, {"Content-type": "text/html; charset=utf-8"});
   res.write("La conexión ha sido correcta");
   res.end()
})

// Tenemos que indicarle a nuestro servidor que se prepare para recibir conexiones y lo hacemos con listen()
// esta función recibe 2 parámetros también, el 1ro es el puerto y normalmente es el 3000 y lo 2do es una función
// que se va a ejecutar cuando el servidor esté listo para recibir conexiones
// server.listen(3000, () => {})
server.listen(3000, () => {
   console.log('Servidor a la espera de conexiones')
})

// de esta manera veremos que hay conexion pero el navegador se quedará esperando una respuesta, por ello tenemos
// que enviarle algo desde nuestro servidor, eso lo hacemo en la función 1ra al indicarle el 'res.end()' da la 
// conexión como satisfactoria y concluye la misma, podemos poner un mensaje dentro de los ()
// LOS MÁS NORMAL ES UTILIZAR EXPRESS