// We need to install mongoose through <npm i mongoose>, a tool to access mongoDB via node
const mongoose = require('mongoose');

// id:foodHunter
// pw:1hunt1
mongoose.connect("mongodb+srv://foodHunter:1hunt1@cluster0.t1di3.mongodb.net/foodHunterDB",{useNewUrlParser: true});

// The schema according to our json file
const restaurantSchema = {
  restaurant: String,
	product: String,
	ingredients: String,
	tags: String,
	address: String
};

const Restaurant = mongoose.model("Restaurant", restaurantSchema);


const rest1 = new Restaurant({
  restaurant: "McDonald's",
	product: "Big Mac",
	ingredients: "beef, lettuce, mayo, cheese, bread",
	tags: "nonveg, fast food",
	address: "362 King St N, Waterloo, ON N2J 2Z2"
});

const rest2 = new Restaurant({
  restaurant: "McDonald's",
	product: "Chicken McNuggets",
	ingredients: "chicken",
	tags: "nonveg, fast food",
	address: "362 King St N, Waterloo, ON N2J 2Z2"
});

const defaultRest = [rest1,rest2];

Restaurant.insertMany(defaultRest, function(err){
  if(err){
    console.log(err);
  } else{
    console.log("Successfully saved the default items to DBs");
  }
});
