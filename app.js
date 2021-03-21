// create an express app
const express = require("express")
const bodyParser = require("body-parser");
const _ = require("lodash");
const mongoose = require('mongoose');

mongoose.connect("mongodb+srv://foodHunter:1hunt1@cluster0.t1di3.mongodb.net/fhDB",{useNewUrlParser: true});

const restaurantSchema = {
  restaurant: String,
	product: String,
	tags: [String],
	address: String
};


const Restaurant = mongoose.model("Restaurant", restaurantSchema);

const app = express()
app.use(bodyParser.urlencoded({extended: true}));

// use the express-static middleware
app.use(express.static("public"))

// define the first route
app.get("/", function (req, res) {
  res.sendFile(__dirname+"/main.html");})

// to get the input from the client and search the database
app.post("/", function(req,res){
    // The input is turned into lowerCase then parsed, based on comma, semicolumn, dot {\s for space}
    // The tests are "chicken,beef,PArsley" & "PARSLEY.chicKEn"
    // I can populate the tests
    var input = _.words([req.body.search.toLowerCase()], /[^,.;]+/g);
    console.log(input);
     // Restaurant.find({ ingredients: input}, function (err, foundList) {
     //   if(!err){
     //     console.log(foundList);
     //   } else {
     //     console.log(err);
     //   }
     // });


  });

// start the server listening for requests
app.listen(process.env.PORT || 3000,
	() => console.log("Server is running..."));
