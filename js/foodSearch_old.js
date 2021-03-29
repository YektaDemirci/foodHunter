// MongoDB monitoring API keys
// obsrznpk
// c7c8f044-05c1-4e4d-b415-60ecc38bc22e
//
// bgyjtoen
// 274c01fa-351e-4f70-aefb-79ac9494d2d9
function food_search() {

    document.getElementById('yek').innerHTML  = "Sikerim";
    var MongoClient = require('mongodb').MongoClient;
    document.getElementById('yek').innerHTML  = "Sokarim";

    let input = document.getElementById('search-bar-id').value;
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

    console.log(user_geolocation);

    $.getJSON("data_food_sample.json", function(jsonFood) {
        // check ingredient input
        if (!input || input == null) {
            result_list_str = "you forgot to type something into the search bar!";
            document.getElementById('message_submit').innerHTML = "No input found";
        }
        // check location input
        else if (user_geolocation.lat==undefined || user_geolocation.lon==undefined) {
            result_list_str = "you forgot to enter your location!";
        }
        else {
            result_list_str = "";
            document.getElementById('message_submit').innerHTML = "";

            for (i = 0; i < jsonFood.length; i++) {

                var ingredient_list_despaced = jsonFood[i].ingredients.replaceAll(" ", "");
                var ingredient_list = ingredient_list_despaced.split(",");

                var foodTag_list_despaced = jsonFood[i].tags.replaceAll(" ", "");
                var foodTag_list = foodTag_list_despaced.split(",");

                var ingredient_count = 0;

                input_split.forEach(function (ingredientVal) {

                    if(ingredient_list.indexOf(ingredientVal) >= 0 || foodTag_list.indexOf(ingredientVal) >= 0){
                        ingredient_count++;
                    }

                });

                if(ingredient_count == input_split_len){
                    result_list_str = result_list_str + "<div class=\"result-div\">" + jsonFood[i].product + "<br>Location: " + jsonFood[i].restaurant + "<br>Address: " + jsonFood[i].address +  "<br><button type='button' onclick='food_selection(\"" + jsonFood[i].product + "??" + jsonFood[i].restaurant.replace("'", "[single-quote]") + "??" + jsonFood[i].address  + "\")'>Select Option</button></div>";
                }
            }
        }

        if(result_list_str.length == 0){
            result_list_str = "we could not find anything, sorry.";
        }

        document.getElementById('results').innerHTML  = result_list_str;

    });




}
