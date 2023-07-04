const router = require('express').Router()

const User = require('../models/User')
// para encriptar las passwords
const bcrypt = require('bcrypt')

// router.get('/', (req, res) => {
//     res.send('Auth page')
// })
// router.get('/register', async (req, res) => {
//     const user = await new User({
//         username: 'john',
//         email: 'john@example.com',
//         password: '123456'
//     })

//     await user.save()
//     res.send('ok')
// })

// REGISTER
router.post('/register', async (req, res) => {

    try {
        // create password
        const salt = await bcrypt.genSalt(10);
        const hashedPassword = await bcrypt.hash(req.body.password, salt);

        // create new user
        const newUser = new User({
            username: req.body.username,
            email: req.body.email,
            password: hashedPassword,
        })

        // save user and return response
        const user = await newUser.save()
        res.status(200).json(user)
    }catch(error) {
        // console.log(error)
        res.status(500).json(error)
    }
})


// LOGIN
router.post('/login', async (req, res) => {
    // buscamos el usuario
    try {
        const user = await User.findOne({email: req.body.email});
        if(!user) {
            return res.status(404).json('user not found');
        } 

        const validPassword = await bcrypt.compare(req.body.password, user.password);
        !validPassword && res.status(404).json('wrong password');

        res.status(200).json(user)
    }catch(error){
        // console.log(error)
        res.status(500).json(error)
    }

})

module.exports = router

// estoy en el minuto 14
// https://www.youtube.com/watch?v=ldGl6L4Vktk&t=39s&ab_channel=LamaDev