function food_search() {
    // get user geolocation
    let user_geolocation = getSessionGeolocation();
    let error_status = false;
    // Error: user geolocation is unavailable
    if(user_geolocation.lat==undefined || user_geolocation.lng==undefined) {
        document.getElementById('results').innerHTML =
            "Sorry, your geolocation is not available. Please select a location.";
        error_status = true;
    }

    // get user input for ingredients
    let input = document.getElementById('search-bar-id').value;
    // Error: no user input for ingredients
    if (!input || input == null) {
        document.getElementById('results').innerHTML =
            "you forgot to type something into the search bar!";
        document.getElementById('message_submit').innerHTML =
            "No input found";
        error_status = true;
    }
    if(error_status)    return;

    document.getElementById('results').innerHTML = "loading";

    document.getElementById('selected-ingredients').innerHTML =
        "You're Looking For...<br>" + input;
    input = input.toLowerCase();
    input = input.replaceAll(" ", "")
    let input_split = input.split(",");
    
    // get food data
    $.getJSON("data_food_sample.json", function(jsonFood) {
        document.getElementById('message_submit').innerHTML = "";
        processData(jsonFood, input_split);
        // no food that matches ingredient input
        if(food_objects.length == 0){
            document.getElementById('results').innerHTML =
                "Sorry, we could not find anything.";
        }
        // sort food by restaurant distance and display them
        else{
            sortFoodObjectsByDistance();
        }
    });
}


// global variables for asynchronous calls to retrieve distance data
var food_objects = null;
var total_count = 0;
var current_count = 0;


function processData(data, input_ingredients){
    //let result = "";
    food_objects = [];

    for (i = 0; i < data.length; i++) {

        var ingredient_list_despaced = data[i].ingredients.replaceAll(" ", "");
        var ingredient_list = ingredient_list_despaced.split(",");

        var foodTag_list_despaced = data[i].tags.replaceAll(" ", "");
        var foodTag_list = foodTag_list_despaced.split(",");

        var ingredient_count = 0;

        input_ingredients.forEach(function (ingredientVal) {
            if(ingredient_list.indexOf(ingredientVal) >= 0 || foodTag_list.indexOf(ingredientVal) >= 0){
                ingredient_count++;
            }
        });

        // ingredients match
        if(ingredient_count == input_ingredients.length){
            //result = result + data[i].product + " at " + data[i].restaurant + "<br>";
            food_objects.push({
                product: data[i].product,
                restaurant: data[i].restaurant,
                address: data[i].address,
                distance: null
            });
        }
    }
    // return result;
}


function sortFoodObjectsByDistance(){
    let user_geolocation = getSessionGeolocation();
    if(user_geolocation.lat==undefined || user_geolocation.lng==undefined) {
        return;
    }
    total_count = food_objects.length;
    current_count = 0;
    // Temporary for now: disable distance when there are 50 or more objects
    if(total_count >= 50) {
        console.log('Too much data: distance feature is disabled.');
        displayFoodObjects();
        return;
    }
    // get distance for the restaurant of each food
    for(let i = 0; i < total_count; i++){
        // Geocode API: convert address to geolocation (lat&lng)
        let geocode_json_url = GEOCODE_API_URL
            +"&address="+food_objects[i].address.replace(/ /g, "+");
        $.getJSON(geocode_json_url, function(response) {
            if (response.status !== "OK") {
                console.log(i, "Error-geocode: " + response.status);
                updateStatusForDistanceData();
            } else {
                //console.log(i,"geocode_response:",response.results);
                // get restaurant geolocation (lat&lng)
                restGeolocation = response.results[0].geometry.location;
                // get distance from user geolocation to restaurant geolocation
                getDistance(user_geolocation, restGeolocation, i);
            }
        });
    }
}


function updateStatusForDistanceData(){
    // processed a food object
    current_count++;
    // display food objects when done
    if(current_count == total_count){
        // Error: distance data is unavailable
        if(food_objects.every(x => x.distance == null)){
            console.log("Error: Cannot obtain distance data.")
            return;
        }
        // sort food objects based on distance
        food_objects.sort((a,b) => a.distance-b.distance);
        console.log(food_objects);
        // display
        displayFoodObjects();
    }
}


/*
 * Get distance from origin (user geolocation) to destination (restaurant geolocation)
 */
/**
        CITATION (IEEE FORMATTED)
        Google Maps Platform, Geolocation: Displaying User or Device Position on Maps. N/A: Google Maps Platform, N/A. [webpage].
        Link: https://developers.google.com/maps/documentation/javascript/geolocation#maps_map_geolocation-javascript
**/
/**
        CITATION (IEEE FORMATTED)
        Google Maps Platform, Distance Matrix Service. N/A: Google Maps Platform, N/A. [webpage].
        Link: https://developers.google.com/maps/documentation/javascript/distancematrix
**/
function getDistance(originGeolocation, destinationGeolocation, index) {
    // convert geolocation(lat&lng) to google maps LatLng
    let origin = new google.maps.LatLng(
        originGeolocation.lat, originGeolocation.lng);
    let destination = new google.maps.LatLng(
        destinationGeolocation.lat, destinationGeolocation.lng);
    // Distance API: get distance from source to destination
    let service = new google.maps.DistanceMatrixService;
    service.getDistanceMatrix({
        origins: [origin],
        destinations: [destination],
        travelMode: google.maps.TravelMode.DRIVING,
        unitSystem: google.maps.UnitSystem.METRIC,
        avoidHighways: false,
        avoidTolls: false
    }, function(response, status) {
        if (status !== google.maps.DistanceMatrixStatus.OK) {
            console.log(index, "Error-distance: " + status);
        } else {
            /*distanceLabel.innerHTML = "distance = "+response.rows[0].elements[0].distance.text
                + ", duration = " + response.rows[0].elements[0].duration.text;*/
            //console.log(index,"distance_response:",response)
            food_objects[index].distance = response.rows[0].elements[0].distance.value;
        }
        updateStatusForDistanceData();
    });
}


/*
 * Display food objects sorted by distance
 */
function displayFoodObjects() {
    // display top N restaurants
    let N = food_objects.length;    // display all the object for now
    let result = "";

    for(let i = 0; i < N; i++){
        let distanceText = (food_objects[i].distance != null) ?
            "<br>Distance: " + (food_objects[i].distance/1000).toFixed(2)+" km" : "";
        result += "<div class=\"result-div\">"
            + food_objects[i].product
            + "<br>Location: " + food_objects[i].restaurant
            + "<br>Address: " + food_objects[i].address
            + distanceText
            + "<br><button type='button' class='btn btn-light selection-button' onclick='food_selection(\""
            + food_objects[i].product + "??" 
            + food_objects[i].restaurant.replace("'", "[single-quote]") + "??" 
            + food_objects[i].address  + "\")'>Select</button></div>";
                
    }
    document.getElementById('results').innerHTML = result;
}
