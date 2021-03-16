/* 
 * Reference: 
 * https://developers.google.com/maps/documentation/javascript/geolocation#maps_map_geolocation-javascript
 */

 function init() {
  // hide map
  const myMap = document.getElementById("location-map");
  myMap.style.display = "none";

  // enable google maps api for autocomplete
  let autocompleteScript = document.createElement("script");
  autocompleteScript.src = MAPS_JS_API_URL
      +"&callback=initLocationSearch&libraries=places&v=weekly";
  autocompleteScript.async = "async";
  document.head.appendChild(autocompleteScript);

  $(document).ready(function() {
    // ask for permission to get geolocation (lat&lng)
    initGeolocation();
  })
}

/*
 * Get user geolocation (lat&lng) if user permitted;
 * otherwise, display error message.
 */
function initGeolocation() {
  const myMap = document.getElementById("location-map");
  const statusDiv = document.getElementById("status");

  // Try HTML5 geolocation.
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        const pos = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };
        setSessionGeolocation(pos.lat,pos.lng);
        // no status message
        statusDiv.innerHTML = "";
        // show geolocation on map
        myMap.src = MAPS_EMBED_API_URL+"&q=+"+pos.lat+"+,+"+pos.lng+"+";
        myMap.style.display = "block";
      },
      () => {
        handleLocationError(true);
      }
    );
  } else {
    // Browser doesn't support Geolocation
    handleLocationError(false);
  }

  function handleLocationError(browserHasGeolocation) {
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
}

/*
 * Initialize Autocomplete for location search
 */
function initLocationSearch() {
  const myMap = document.getElementById("location-map");
  const input = document.getElementById("location-input");
  // limit to Canada & US
  const options = {
    componentRestrictions: { country: ["ca","us"] }
  };
  // Place API for autocomplete: allow user to set location
  const autocomplete = new google.maps.places.Autocomplete(input, options);
  google.maps.event.addListener(autocomplete, 'place_changed', function () {
    let place = autocomplete.getPlace();
    setSessionGeolocation(place.geometry.location.lat(),place.geometry.location.lng());
    // show geolocation on map
    let placeAddress = place.formatted_address.replace(/ /g, "%20");
    console.log(place.name);
    myMap.src = MAPS_EMBED_API_URL+"&q="+placeAddress;
    myMap.style.display = "block";
  });
}