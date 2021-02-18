/* 
 * Reference: 
 * https://developers.google.com/maps/documentation/javascript/distancematrix
 */

const origin_geolocation = getSessionGeolocation();

function initRestaurant() {
    if(origin_geolocation.lat==undefined || origin_geolocation.lon==undefined) {
        alert("Error: Your geolocation is not available.");
    }

    $(document).ready(function() {
        $.getJSON("../data_food_sample.json", function(result) {
            let i = 1;
            // get restaurant name and address
            let restName = result[i].restaurant;
            let restAddress = result[i].address;
            displayRestaurant(restName, restAddress);
        });
    });
}
  
function displayRestaurant(name, address) {
    const restContainer = document.getElementById("restaurant-container");
    let nameLabel = document.createElement("p");
    let distanceLabel = document.createElement("p");
    let map = document.createElement("iframe");
    map.frameborder = "0";
    restContainer.appendChild(nameLabel);
    restContainer.appendChild(distanceLabel);
    restContainer.appendChild(map);
    // show restaurant name
    nameLabel.innerHTML = name;
    // get distance to restaurant
    getDistance(address, distanceLabel);
    // show restaurant on map
    name = name.replace(/ /g, "%20");
    address = address.replace(/ /g, "%20");
    map.src = MAPS_EMBED_API_URL+"&q="+address+"+("+name+")";
}
  
// get distance from origin (user geolocation) to destination (restaurant address)
function getDistance(destinationAddress, distanceLabel) {
    if(origin_geolocation.lat==undefined || origin_geolocation.lon==undefined) { return; }
    // origin: user geolocation
    let origin = new google.maps.LatLng(origin_geolocation.lat, origin_geolocation.lon);
    // destination: restaurant address
    let destination = destinationAddress.replace(/ /g, "%20");

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
            console.log("Error: " + status);
        } else {
            console.log(response)
            distanceLabel.innerHTML = "distance = "+response.rows[0].elements[0].distance.text
                + ", duration = " + response.rows[0].elements[0].duration.text;
        }
    });
}