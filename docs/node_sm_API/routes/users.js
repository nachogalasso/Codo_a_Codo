// tenemos que usar express, pero con routes y luego exportar
const router = require('express').Router()
const bcrypt = require('bcrypt')
const User = require('../models/User')

// router.get('/', (req, res) => {
//     res.send('User page')
// })

// UPDATE user
router.put('/:id', async (req, res) => {
    if(req.body.userId === req.params.id || req.body.isAdmin) {
        // password
        if(req.body.password) {
            try {
                const salt = await bcrypt.genSalt(10);
                req.body.password = await bcrypt.hash(req.body.password, salt);
            }catch(error){
                return res.status(500).json(error);
            }
        }

        try {
            const user = await  User.findByIdAndUpdate(req.params.id, {$set: req.body,});
            res.status(200).json('Account has been updated');
        }catch(error){
            return res.status(500).json(error);
        }

    }else{
        return res.status(403).json('You can only update your account')
    }
})
// DELETE user
router.delete('/:id', async (req, res) => {
    if(req.body.userId === req.params.id || req.body.isAdmin) {
        try {
            const user = await User.findByIdAndDelete(req.params.id);
            res.status(200).json('Account has been deleted');
        }catch(error) {
            return res.status(500).json(error);
        }
    }else{
        return res.status(403).json('You can only delete your account')
    }
})
// GET a user
// FOLLOW user
// UNFOLLOW user


// estoy en el minuto 48
// https://www.youtube.com/watch?v=ldGl6L4Vktk&t=39s&ab_channel=LamaDev

module.exports = router