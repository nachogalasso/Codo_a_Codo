import express from 'express';
import cors from 'cors';
import router from './api/reviews.route.js'
import reviews from './api/reviews.route.js'

// access to express
const app = express();

// now we use middleware with app.use
app.use(cors());
// Allows the server to accept JSON files.
app.use(express.json());
// 
app.use(router)

// now we configure the routes to send and recieve information app.use("/api/v1/reviews", reviews)
// we can use any url. The route indicates, the folder 'api', 'v1' refers to the volumen. The 2nd argument is to
// tell node to use the route from the import reviews
app.use('/api/v1/reviews', reviews)

// now we configure a backup route. This is because we are gonna use different files
app.use('*', (req, res) => {
   res.status(404).json({error: 'not found'})
})

// we export our app as a module
export default app