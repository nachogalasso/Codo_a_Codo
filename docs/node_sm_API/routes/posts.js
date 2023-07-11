const router = require('express').Router();
const Post = require('../models/Post')
// router.get('/', (req, res) => {
//     console.log('Acá van los posteos guachin')
// })

// CREATE A POST
router.post('/', async (req, res) => {
    const newPost = new Post(req.body)
    try {
        const savedPost = await newPost.save();
        res.status(200).json(savedPost);
    }catch(error){
        return res.status(500).json(error);
    }
})

// UPDATE A POST
router.put('/:id', async (req, res) => {
    try {

        const post = await Post.findById(req.params.id);
        if(post.userId === req.body.userId) {
            await post.updateOne({$set: req.body});
            res.status(200).json('Post updated')
        }else{
            res.status(403).json('You can only update your posts')
        }

    }catch(error){
        return res.status(500).json(error);
    }
})

// DELETE A POST
router.delete('/:id', async (req, res) => {
    try {

        const post = await Post.findById(req.params.id);
        if(post.userId === req.body.userId) {
            await post.deleteOne();
            res.status(200).json('Post Deleted')
        }else{
            res.status(403).json('You can only delete your posts')
        }

    }catch(error){
        return res.status(500).json(error);
    }
})
// LIKE A POST
// GET A POST
// TIMELINE POSTS

module.exports = router