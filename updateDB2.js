// We need to install mongoose through <npm i mongoose>, a tool to access mongoDB via node
const mongoose = require('mongoose');
const fs = require('fs');
const _ = require("lodash");


// id:foodHunter
// pw:1hunt1
mongoose.connect("mongodb+srv://foodHunter:1hunt1@cluster0.t1di3.mongodb.net/fhDB",{useNewUrlParser: true});

let jsonFood = fs.readFileSync('public/data_food_sample.json');
let restaurants = JSON.parse(jsonFood);



// The schema according to our json file
const restaurantSchema = {
  restaurant: String,
	product: String,
	tags: [String],
	address: String
};

const Restaurant = mongoose.model("Restaurant", restaurantSchema);


const rests = [];

for (const rest of restaurants){

  var parsedIngredients = _.words([rest.ingredients.toLowerCase()], /[^,.;]+/g);
  var parsedTags = _.words([rest.tags.toLowerCase()], /[^,.;]+/g);

  parsedTags=parsedTags.concat(parsedIngredients);

  const rest1 = new Restaurant({
    restaurant: rest.restaurant,
  	product: rest.product,
  	tags: parsedTags,
  	address: rest.address
  });
  rests.push(rest1);
}

Restaurant.insertMany(rests, function(err){
  if(err){
    console.log(err);
  } else{
    console.log("Successfully saved the default items to DBs, please close the execution with CTRL+C");
  }
});

// db.restaurants.find(
//     {$or:[
//         {ingredients:{ $in :["chicken"]}},
//         {tags:{ $in:["nonveg"]}}
//     ]}
// )
