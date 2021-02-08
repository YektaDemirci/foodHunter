// Reference: https://developers.google.com/maps/documentation/javascript/geolocation#maps_map_geolocation-javascript
// Note: This example requires that you consent to location sharing when
// prompted by your browser. If you see the error "The Geolocation service
// failed.", it means you probably did not give permission for the browser to
// locate you.

const API_key = "AIzaSyCh_nAkklDfea8cKEhEmplXqXz7yxl2yGA";
const embed_map_url_key = "https://www.google.com/maps/embed/v1/place?key="+API_key;

function init() {
  // hide map
  const myMap = document.getElementById("location-map");
  myMap.style.display = "none";
  $(document).ready(function() {
    // ask for permission to get geolocation
    initGeolocation();
  })
}

/********** My geolocation **********/

function initGeolocation() {
  const myMap = document.getElementById("location-map");
  const statusDiv = document.getElementById("status");

  // Try HTML5 geolocation.
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        const pos = {
          lat: position.coords.latitude,
          lng: position.coords.longitude,
        };
        // no status message
        statusDiv.innerHTML = "";
        // show geolocation on map
        myMap.src = "https://www.google.com/maps/embed/v1/place?key="+API_key
          +"&q=+"+pos.lat+"+,+"+pos.lng+"+";
        myMap.style.display = "block";
      },
      () => {
        handleLocationError(true, statusDiv, myMap);
      }
    );
  } else {
    // Browser doesn't support Geolocation
    handleLocationError(false, statusDiv, myMap);
  }
}

function handleLocationError(browserHasGeolocation, statusDiv, myMap) {
  // show error message
  statusDiv.innerHTML = 
    browserHasGeolocation
      ? "Error: The Geolocation service failed."
      : "Error: Your browser doesn't support geolocation."
  ;
  // hide map
  myMap.style.display = "none";
  myMap.src = "";
}

function initSearch() {
  const myMap = document.getElementById("location-map");
  const input = document.getElementById("location-input");
  const options = {
    componentRestrictions: { country: ["ca","us"] }
  };
  const autocomplete = new google.maps.places.Autocomplete(input, options);
  google.maps.event.addListener(autocomplete, 'place_changed', function () {
    let place = autocomplete.getPlace();
    //console.log(place.name, place.geometry.location.lat(),place.geometry.location.lng());
    //myMap.src = "https://www.google.com/maps/embed/v1/place?key="+API_key
    //  +"&q=+"+lat+"+,+"+lng+"+";
    // show geolocation on map
    let placeAddress = place.formatted_address.replace(/ /g, "%20");
    console.log(place.name);
    myMap.src = embed_map_url_key+"&q="+placeAddress;
    myMap.style.display = "block";
  });
}

/********** Restaurant location **********/

function initRestaurant() {
  $(document).ready(function() {
    $.getJSON("../data_food_sample.json", function(result) {
      let i = 4;
      // get restaurant name and address
      let businessName = result[i].restaurant;
      let businessAddress = result[i].address;

      const restContainer = document.getElementById("restaurant-container");
      let restName = document.createElement("p");
      let restMap = document.createElement("iframe");
      restMap.frameborder = "0";
      restContainer.appendChild(restName);
      restContainer.appendChild(restMap);
      // show restaurant name
      restName.innerHTML = businessName;
      // show restaurant on map
      businessName = businessName.replace(/ /g, "%20");
      businessAddress = businessAddress.replace(/ /g, "%20");
      restMap.src = embed_map_url_key+"&q="+businessAddress+"+("+businessName+")";
    });
  });
}