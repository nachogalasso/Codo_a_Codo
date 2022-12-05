import ReviewsDAO from '../dao/reviewsDAO.js'
import mongoose from 'mongoose';

export default class ReviewsController {

   // POST DATA
   static async apiPostReview(req, res, next) {
      try {
         const movieId = parseInt(req.body.movieId);
         const review = req.body.review;
         const user = req.body.user;

         const movieResponse = await ReviewsDAO.addReview(
            movieId,
            user,
            review
         )
         res.json({status: "success"})
      }catch(e) {
         res.status(500).json({error: e.message})
      }
   }

   // GET DATA
   static async apiGetReview(req, res, next) {
      try{
         // this comes from router.route('/:id') in reviews.route.js
         let id = mongoose.Types.ObjectId(req.params.id.trim()) || {}
         // let id = req.params.id || {};
         let review = await ReviewsDAO.getReview(id);
         if (!review) {
            res.status(404).json({ error: "Not Found" });
            return;
         }
         res.json(review);
      }catch(e){
         console.log(`api, ${e}`);
         res.status(500).json({error: e});
      }
   }

   // UPDATE DATA
   static async apiUpdateReview(req, res, next) {
      try {
         // here the data is from the params
         const reviewId = mongoose.Types.ObjectId(req.params.id);
         // here the data is from the body
         const review = req.body.review;
         const user = req.body.user;

         // information we pass, the response comes from mongodb
         const reviewResponse = await ReviewsDAO.updateReview(
            reviewId,
            user,
            review
         )

         // Two ways to inform if there is an error
         var {error} = reviewResponse;
         if(error) {
            res.status(404).json({error})
         }
         // this is when no change happens
         if(reviewResponse.modifiedCount === 0) {
            throw new Error("Unable to update the review")
         }
         // If there is no error, all went fine then
         res.json({status: 'success'})
      }catch (e) {
         res.status(500).json({error: e.message})
      }
   }

   // DELETE DATA
   static async apiDeleteReview(req, res, next) {
      try {
         // get data from params
         const reviewId = mongoose.Types.ObjectId(req.params.id);
         const reviewResponse = await ReviewsDAO.deleteReview(reviewId);
         res.json({status: "success"});
      }catch (e) {
         res.status(500).json({error: e.message})
      }
   }

   // GET LIST of all REVIEWS
   static async apiGetReviews(req, res, next) {
      try {
         // let id = req.params.id || {};
         let reviews = await ReviewsDAO.getReviewsByMovieId(id)
         // if there are no reviews
         if(!reviews) {
            res.status(404).json({error: "Not Found"})
            return
         }
         // the response if the program found the reviews
         res.json(reviews)
      }catch (e) {
         // if it found an other error
         console.log(`api, ${e}`);
         res.status(500).json({error: e})
      }
   }

} // End of ReviewsController