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

// LIKE / DISLIKE A POST
router.put('/:id/like', async (req, res) => {
    try {
        const post = await Post.findById(req.params.id);
        if(!post.likes.includes(req.body.userId)) {
            await post.updateOne({$push:{likes:req.body.userId}});
            res.status(200).json("The post has been liked");
        }else{
            await post.updateOne({$pull:{likes:req.body.userId}})
            res.status(200).json("Post disliked")
        }

    }catch(error){
        res.status(500).json(error);
    }
})

// GET A POST
router.get('/:id', async (req, res) => {
    try {
        const post = await Post.findById(req.params.id);
        res.status(200).json(post)
    }catch(error){
        res.status(500).json(error);
    }
})

// TIMELINE POSTS
router.get('/timeline/all', async (req, res) => {
    // let postArray = [];
    try {
        const currentUser = await User.findById(req.body.userId);
        const userPost = await Post.find({ userId: currentUser._id });
        const friendPosts = await Promise.all(
            currentUser.followings.map((friendId) => {
                return Post.find({ userId: friendId});
            })
        );
        res.json(userPost.concat(...friendPosts));
    }catch(error){
        res.status(500).json(error);
    }
})


module.exports = router