// Reference: https://developers.google.com/maps/documentation/javascript/geolocation#maps_map_geolocation-javascript
// Note: This example requires that you consent to location sharing when
// prompted by your browser. If you see the error "The Geolocation service
// failed.", it means you probably did not give permission for the browser to
// locate you.

const API_key = "AIzaSyCh_nAkklDfea8cKEhEmplXqXz7yxl2yGA"

/********** My geolocation **********/
let locButton, myMap, statusDiv;

function initMap() {
  locButton = document.getElementById("location-button");
  myMap = document.getElementById("my-map");
  statusDiv = document.getElementById("status");
  
  // hide map
  myMap.style.display = "none";

  locButton.addEventListener("click", () => {
    // Try HTML5 geolocation.
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude,
          };
          myMap.src = "https://www.google.com/maps/embed/v1/place?key="+API_key
            +"&q=+"+pos.lat+"+,+"+pos.lng+"+";
          myMap.style.display = "block";
          statusDiv.innerHTML = "";
        },
        () => {
          handleLocationError(true, statusDiv);
        }
      );
    } else {
      // Browser doesn't support Geolocation
      handleLocationError(false, statusDiv);
    }
  });
}

function handleLocationError(browserHasGeolocation) {
  statusDiv.innerHTML = 
    browserHasGeolocation
      ? "Error: The Geolocation service failed."
      : "Error: Your browser doesn't support geolocation."
  ;
  locButton.disabled = true;
  myMap.style.display = "none";
  myMap.src = "";
}

/********** Restaurant location **********/

function initRestaurant() {
    let businessName = "McDonald's";
    let address = "362 King St N, Waterloo, ON N2J 2Z2";

    let restName = document.getElementById("restaurant-name");
    let restMap = document.getElementById("restaurant-map");

    restName.innerHTML = businessName;

    businessName = businessName.replace(/ /g, "%20");
    address = address.replace(/ /g, "%20");
    restMap.src = "https://www.google.com/maps/embed/v1/place?key="+API_key
        +"&q="+address+"+("+businessName+")";
}