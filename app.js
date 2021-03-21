// create an express app
const express = require("express")
const app = express()

// use the express-static middleware
app.use(express.static("public"))

// define the first route
app.get("/", function (req, res) {
  res.sendFile(__dirname+"/main.html");})

app.post("/", function(req, res){
  //YEKTA//
  // You need to append <form> to main.html to be able to get the input
  // Then you can quickly update the followings if we decide to use implement a dynamic arch
// document.getElementById('results').innerHTML  = result_list_str;
//
//
//  var input = _.words([req.body.search.toLowerCase()], /[^,.;]+/g);
//  console.log(input);
//  Restaurant.find({ tags: { $all: input } }, function (err, foundList) {
//     if(!err){
//       if(foundList.length == 0){
//         result_list_str = "We could not find anything, sorry.";
//       } else{
//         for(i = 0; i < jsonFood.length; i++) {
//         result_list_str = result_list_str + foundList[i].product + " at " + foundList[i].restaurant + "<br>";
//         }
//       }
//     } else {
//       console.log(err);
//     }
//   });
//   res.send(result_list_str);
//   // res.render{"matches", { foundItems:result_list_str }};
//   // document.getElementById('results').innerHTML  = result_list_str;
//
//
// });

// start the server listening for requests
app.listen(process.env.PORT || 3000,
	() => console.log("Server is running..."));
