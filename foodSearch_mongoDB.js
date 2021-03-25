

    /* let input = document.getElementById('search-bar-id').value;
    document.getElementById('results').innerHTML  = "loading"; 
    
    let input_selections = document.getElementById('selected-ingredients');
    let input_vert_list = input; //.replaceAll(",","<br>");
    input_selections.innerHTML = "You're Looking For...<br>" + input_vert_list;

    let result_list_str = "";

    input = input.toLowerCase();
    input = input.replaceAll(" ", "")

    let input_split = input.split(",");
    let input_split_len = input_split.length;

    let user_geolocation = getSessionGeolocation();

    console.log(user_geolocation); */



      var testVal = ["["];
    

      var MongoClient = require('mongodb').MongoClient;
      var url = "mongodb+srv://foodHunter:1hunt1@cluster0.t1di3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority";

      MongoClient.connect(url, function(err, db) {
          if (err) throw err;
          var dbo = db.db("foodHunterDB");
          //Find all documents in the customers collection:
          dbo.collection("restaurants").find({}).toArray(function(err, result) {
            if (err) throw err;
            console.log(result);

            for(i=0; i < result.length; i++){
              testVal +=  JSON.stringify(result[i]) + ",";
            }

            testVal = testVal.slice(0,-1);
            
            testVal += ']';

            var fs = require('fs');

            fs.writeFile('test_mongodb_data.json', testVal, function (err) {
              if (err) throw err;
              console.log('Extracted data from MongoDB');
            });

            db.close();
          });
      });


    const http = require('http');

    const hostname = '127.0.0.1';
    const port = 3000;

    const server = http.createServer((req, res) => {
      res.statusCode = 200;
      res.setHeader('Content-Type', 'application/jsonp');
      res.setHeader('Access-Control-Allow-Origin', 'http://localhost');
      res.setHeader('Access-Control-Allow-Methods', 'GET,POST')
      res.end(testVal);
    });

    server.listen(port, hostname, () => {
      console.log(`Server running at http://${hostname}:${port}/`);
    });

   

    


