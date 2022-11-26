// AQUI TAMBIÉN TENEMOS QUE USAR A MONGOOSE
import mongoose from "mongoose";
// luego tendremos que utilizar el 'Schema', o sea que de mongoose extrae el 'Schema' y lo destructura
const { Schema } = mongoose; // es lo mismo que poner const Schema = mongoose.Schema
// Una vez que tenemos eso podemos crear nuestro modelo de datos, el cual podemos colocar el nombre que querramos
// Como buena práctica se suele poner los Schema con el modelo de CamelCase
// Con const PokeModel = new Schema({}) lo que estamos haciendo es crear una function que recibe como parámetro
// el objeto que va a ser nuestra estructura de datos. Dentro de ella tenemos que poner el modelo con el que hemos
// armado nuestra base de datos, en nuestro caso teníamos una sola que era name: String
const PokeSchema = new Schema({
   name: String
})

// luego tenemos que crear el modelo para poder exportarlo, para ello tenemos que usar mongoose.model()
// esta function recibe 2 parámetros. El 1ro es el nombre de nuestra colección y es importante que sea el mismo
// igual al nombre que utilizamos para llamar a nuestra colección que en nuestro caso fué 'pokemons'.
// El 2do parámetro es el Schema del modelo, en este caso es 'PokeSchema'
// Esto lo que hace es crear el modelo tomando como base la creada en mongo con el nombre 'pokemons'
// y utiliza el modelo que creamos con Schema
const PokeModel = mongoose.model('pokemons', PokeSchema)

// Ahora solamente nos queda exportarlo
export default PokeModel

// teniendo esto tenemos que usarlo en nuesto index.controller con el fin de que realice la petición