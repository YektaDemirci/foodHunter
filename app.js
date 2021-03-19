// create an express app
const express = require("express")
const bodyParser = require("body-parser");
const _ = require("lodash");


const app = express()
app.use(bodyParser.urlencoded({extended: true}));

// use the express-static middleware
app.use(express.static("public"))

// define the first route
app.get("/", function (req, res) {
  res.sendFile(__dirname+"/main.html");})

app.post("/", function(req,res){
    // The input is turned into lowerCase then parsed, based on comma, space, semicolumn, dot
    // The tests are "chicken,beef PArsley" & "PARSLEY chicKEn"
    // I can populate the tests
    var input = _.words([req.body.search.toLowerCase()], /[^,.\s;]+/g);
    // console.log(input);

  });

// start the server listening for requests
app.listen(process.env.PORT || 3000,
	() => console.log("Server is running..."));
