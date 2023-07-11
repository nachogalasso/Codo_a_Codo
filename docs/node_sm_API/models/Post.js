// Son las modelos de bases de datos vamos a utilizar

const mongoose = require('mongoose')

// Este es nuestro esquema al cual dentro vamos a establecer las propiedades
const PostSchema = mongoose.Schema(
    {
        userId: {
            type: String,
            required: true,
        },
        desc: {
            type: String,
            max: 500,
        },
        image: {
            type: String,
        },
        likes: {
            type: Array,
            default: [],
        }
    },
        {timestamps: true}
)

// este Schema la tenemos que exportar para poder usarlo en auth.js
module.exports = mongoose.model('Post', PostSchema)