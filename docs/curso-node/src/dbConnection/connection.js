// Aquí para instalar mongoose tendremos que hacer lo mismo que hacemos con todos los paquetes
import mongoose from 'mongoose'

// Una vez que lo tenemos ya lo podemos conectar, le tendremos que pasar 2 parámetros:
// 1. el sitio dónde se conecta la base de datos, por lo general es uri y tiene que ir como una variable por fuera
// creamos las variables
// la pass de la BD
const password = "qWrko7J5d0bW88ot";
// nombre que le asignamos a nuestra base de datos
const dbname = "pokedex";
// ruta de acceso a nuestra BD, recordar que conviene utilizar el template literal string ``
const uri = `mongodb+srv://imgalasso:${password}@cluster0.cwir3tp.mongodb.net/${dbname}?retryWrites=true&w=majority`;

// probamos algo
// main().catch(err => console.log(err))

// async function main() {
//    await mongoose.connect("mongodb://localhost:3000/test");
// }

// si colocamos mongoose.connect(uri), nos va a funcionar pero tendremos muchos problemas
// por si hace falta {useNewUrlParser: true, useUnifiedTopology: true}
async function main() {
   try {
      await mongoose.connect(uri);
   }catch(error) {
      handleError(error)
   }
}
// ESTO LO TENEMOS QUE UTILIZAR EN NUESTRO index.controller, para que se conecte a la base de datos. por eso necesitamos exportarlo

export default main
// export default connection
// otra forma
// const connection = () => {
//    try {
//       await mongoose.connect(uri);
//    }catch(error){
//       handleError(error)
//    }
// }