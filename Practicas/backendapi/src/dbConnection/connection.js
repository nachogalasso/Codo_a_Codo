import mongoose from "mongoose";

const password = "s0ToAgULEktowNB7";
const dbname = "";
const uri = `mongodb+srv://movieapi:${password}@cluster0.hegsdaj.mongodb.net/${dbname}?retryWrites=true&w=majority`;

async function main() {
   try {
      await mongoose.connect(uri);
   }catch(err){
      handleError(err)
   }
}

export default main