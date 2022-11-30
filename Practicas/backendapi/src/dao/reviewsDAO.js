// Here we connect to the database with mongodb
// So first we need to import mongodb
import mongodb from 'mongodb';
import mongoose from 'mongoose';
// from mongodb we want to access the id
const ObjectID = mongodb.ObjectId;

let reviews

export default class ReviewsDAO {
   // function to inject the data
   static async injectDB(conn) {
      if(reviews) {
         return
      }
      try {
         // the 1st value is the name of the database, so we can name it the way we want and the 2nd is one 
         // part of that db, we can have various collections
         reviews = await conn.db('reviews').collection('reviews');
      }catch (e) {
         console.error(`Unable to establish collection handles in userDAO: ${e}`)
      }
   }

   // ADD REVIEW to DB
   static async addReview(movieId, user, review) {
      try {
         // here we create our document object
         const reviewDoc = {
            movieId: movieId,
            user: user,
            review: review
         }
         // insertOne() is a mongodb command and is how we insert data
         return await reviews.insertOne(reviewDoc)
      }catch (e) {
         console.error(`Unable to post review: ${e}`)
         return {error: e}
      }
   }

   // GET REVIEW
   static async getReview(reviewId) {
      try {
         // is common to search by id, because it is unique
         return await reviews.findeOne({_id: ObjectID(reviewId)})
      }catch (e) {
         console.error(`Unable to get review: ${e}`)
      }
   }

   // UPDATE REVIEW
   static async updateReview(reviewId, user, review) {
      try {
         const updateResponse = await reviews.updateOne(
            { _id: ObjectID(reviewId)},
            // command from mongodb to set new data
            { $set: { user: user, review: review}}
         )
         return updateResponse
      }catch (e) {
         console.error(`Unable to update review: ${e}`)
         return  {error: e}
      }
   }

   // DELETE REVIEW
   static async deleteReview(reviewId) {
      try {
         const deleteResponse = await reviews.deleteOne({ _id: ObjectID(reviewId)})
         return deleteResponse
      }catch (e) {
         console.error(`Unable to delete review: ${e}`);
         return {error: e}
      }
   }

   // GET ALL REVIEWS
   static async getReviewsByMovieId(movieId) {
         console.log("mov", movieId);
         try {
            const cursor = await reviews.find({ movieId: parseInt(movieId)})
            return cursor.toArray()
         }catch (e) {
            console.error(`Unable to get review: ${e}`);
            return {error: e}
         }
   }
} // End of ReviewsDAO