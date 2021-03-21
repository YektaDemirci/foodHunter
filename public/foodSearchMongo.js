//YEKTA//
// It is not possible to connect to mongoDB from client's browser, therefore this approach will not work
// However, I am keeping this code as a reference in case if we decide to implement a dynamic webpage

function food_search(){
  document.getElementById('testYek').innerHTML  = "test1";
  var MongoClient = require('mongodb').MongoClient;
  document.getElementById('testYek').innerHTML  = "test2";
  var url = "mongodb+srv://foodHunter:1hunt1@cluster0.t1di3.mongodb.net";
  document.getElementById('testYek').innerHTML  = "test3";


  // document.getElementById('testYek').innerHTML  = "loading";


  let result_list_str = "";

  let input = ["chicken","nonveg"];
  // let input = document.getElementById('search-bar-id').value
  // input = input.toLowerCase();
  // input = input.replaceAll(" ", "")
  // let input_split = input.split(",");


  if (false) {
      result_list_str = "you forgot to type something into the search bar!";
      document.getElementById('message_submit').innerHTML  = "No input found";
  } else{

      MongoClient.connect(url, {useUnifiedTopology: true}, function(err, db) {
      var dbo = db.db("fhDB");
      dbo.collection("restaurants").find({ tags: { $all: input } }).toArray(function(err, result) {
        if (err) throw err;
        if(result.length == 0){
          result_list_str = "We could not find anything, sorry.";
        } else{
            for(i = 0; i < result.length; i++) {
              result_list_str = result_list_str + result[i].product + " at " + result[i].restaurant + "<br>";
            }
            document.getElementById('results').innerHTML  = result_list_str;
            // console.log(result_list_str);
          }
        db.close();
      });
    });

  }
}
