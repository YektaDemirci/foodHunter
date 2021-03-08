/* 
 * Reference: 
 * https://developers.google.com/maps/documentation/javascript/distancematrix
 */

const user_geolocation = getSessionGeolocation();
var total_count = 0;
var current_count = 0;
var rest_objects = null;

function initRestaurant() {
    // Error: user geolocation is unavailable
    if(user_geolocation.lat==undefined || 
        user_geolocation.lng==undefined) {
        alert("Sorry, your geolocation is not available. Please select a location.");
        return;
    }
    $(document).ready(function() {
        $.getJSON("../data_food_sample.json", function(result) {
            console.log("original_data:",result)
            // initialize distance data status
            total_count = result.length;
            current_count = 0;
            // restaurant objects for restaurant.html
            rest_objects = result.map(x => {
                return {
                    name: x.restaurant,
                    address: x.address,
                    distance: null
                };
            });
            console.log("rest_objects:",rest_objects)
            // get distance for each restaurant
            for(let i = 0; i < total_count; i++){
                // Geocode API: convert address to geolocation (lat&lng)
                geocode_json_url = GEOCODE_API_URL
                    +"&address="+rest_objects[i].address.replace(/ /g, "+");
                $.getJSON(geocode_json_url, function(response) {
                    if (response.status !== "OK") {
                        console.log(i, "Error-geocode: " + response.status);
                        updateDistanceDataStatus();
                    } else {
                        //console.log(i,"geocode_response:",response.results);
                        // get restaurant geolocation (lat&lng)
                        restGeolocation = response.results[0].geometry.location;
                        // get distance from user geolocation to restaurant geolocation
                        getDistance(restGeolocation, i);
                    }
                });
            }
        });
    });
}

function updateDistanceDataStatus(){
    // processed a restaurant object
    current_count++;
    // display top restaurants when done
    if(current_count == total_count){
        displayTopRestaurants();
    }
}

/*
 * Get distance from origin (user geolocation) to destination (restaurant geolocation)
 */
function getDistance(destinationGeolocation, index) {
    if(user_geolocation.lat==undefined || 
        user_geolocation.lng==undefined) { return; }
    // origin: user geolocation
    let origin = new google.maps.LatLng(
        user_geolocation.lat, user_geolocation.lng);
    // destination: restaurant geolocation
    let destination = new google.maps.LatLng(
        destinationGeolocation.lat, destinationGeolocation.lng);
    // Distance API: get distance from origin to destination
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
            rest_objects[index].distance = response.rows[0].elements[0].distance.value;
        }
        updateDistanceDataStatus();
    });
}

/*
 * Display top 3 restaurants sorted by distance
 */
function displayTopRestaurants() {
    // Error: distance data is unavailable
    const statusDiv = document.getElementById("status");
    if(rest_objects.every(x => x.distance == null)){
        statusDiv.innerHTML = "Error: Cannot obtain distance data."
        return;
    }
    // sort restaurants based on distance
    rest_objects.sort(x => x.distance);
    // display top 3 restaurants
    const container = document.getElementById("restaurant-container");
    for(let i = 0; i < 3; i++){
        let restDiv = document.createElement("div");
        container.appendChild(restDiv);
        displayRestaurant(restDiv, i)
    }

    /*
    * Display restaurant's name & distance in labels,
    * address on google embed map
    */
    function displayRestaurant(restContainer, index) {
        let nameLabel = document.createElement("p");
        let distanceLabel = document.createElement("p");
        let map = document.createElement("iframe");
        map.frameborder = "0";
        restContainer.appendChild(nameLabel);
        restContainer.appendChild(distanceLabel);
        restContainer.appendChild(map);
        // show restaurant name & distance
        nameLabel.innerHTML = rest_objects[index].name;
        distanceLabel.innerHTML = rest_objects[index].distance!=null ?
            (rest_objects[index].distance/1000).toFixed(2)+" km" : "";
        // show restaurant on map
        map.src = MAPS_EMBED_API_URL
            +"&q="+rest_objects[index].address.replace(/ /g, "%20")
            +"+("+rest_objects[index].name.replace(/ /g, "%20")+")";
    }
}