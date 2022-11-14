const numbers = [1, 2, 3, 4, 5]

// console.log(numbers)
numbers.forEach(number => console.log(number * 2))

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