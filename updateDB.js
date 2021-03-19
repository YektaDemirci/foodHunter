// We need to install mongoose through <npm i mongoose>, a tool to access mongoDB via node
const mongoose = require('mongoose');
const fs = require('fs');

// id:foodHunter
// pw:1hunt1
mongoose.connect("mongodb+srv://foodHunter:1hunt1@cluster0.t1di3.mongodb.net/foodHunterDB",{useNewUrlParser: true});

let rawdata = fs.readFileSync('public/data_food_sample.json');
let restaurants = JSON.parse(rawdata);

// The schema according to our json file
const restaurantSchema = {
  restaurant: String,
	product: String,
	ingredients: String,
	tags: String,
	address: String
};

const Restaurant = mongoose.model("Restaurant", restaurantSchema);
const rests = []

for (const rest of restaurants){
  const rest1 = new Restaurant({
    restaurant: rest.restaurant,
  	product: rest.product,
  	ingredients: rest.ingredients,
  	tags: rest.tags,
  	address: rest.address
  });
  rests.push(rest1);
}

console.log("End of for loop");

//The following will save all to the DB
Restaurant.insertMany(rests, function(err){
  if(err){
    console.log(err);
  } else{
    console.log("Successfully saved the default items to DBs, please close the execution with CTRL+C");
  }
});



// const mongoose = require("mongoose");
// mongoose.connect("mongodb+srv://foodHunter:1hunt1@cluster0.t1di3.mongodb.net/foodHunterDB",{useNewUrlParser: true});
//
// const restaurantSchema = {
//   restaurant: String,
//   product: String,
//   ingredients: String,
//   tags: String,
//   address: String
// };
//
// const Post = mongoose.model("Post", postSchema);
//
// Post.find(function(err, rest){
//   if (err) {
//     console.log(err);
//   } else {
//      console.log(rest);
//   }
