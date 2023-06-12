// Aquí es donde hacemos los modelos de nuestra app, también tendremos que importar a mongoose
const mongoose = require('mongoose')

// Tendremos que crear el Schema de nuestra app, el objeto que mantiene nuestra base. Para el update podemos usar el 
// timestamps, rastrea los cambios en los datos.
const productSchema = mongoose.Schema(
    {
        name: {
            type: String,
            required: [true, "Por favor ingrese un producto"]
        },
        quantity: {
            type: Number,
            required: true,
            defaultValue: 1
        },
        price: {
            type: Number,
            required: true,
        },
        image: {
            type: String,
            required: false,
        }
    },
    {
        timestamps: true
    }
)

// Con el Schema creado, podemos hacer los productos y le pasamos nuestro Schema
const Product = mongoose.model('Product', productSchema);
// con esto ya lo podemos exportar con el comando module.exports
// Lo que nos permite es colocar datos dentro de nuestra base de datos.
module.exports = Product;

