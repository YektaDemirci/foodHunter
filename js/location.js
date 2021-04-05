/* 
 * Reference: 
 * https://developers.google.com/maps/documentation/javascript/geolocation#maps_map_geolocation-javascript
 * https://www.w3schools.com/w3css/tryit.asp?filename=tryw3css_slideshow_rr
 */

function init() {
  sessionStorage.clear();

  automatic_sample_slideshow();

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
    // ask for permission to get geolocation
    initGeolocation();
    initLocationModal();
  })
}


function initLocationModal() {
  // Get the modal
  const modal = document.getElementById("location-modal");
  // Get the button that opens the modal
  const btn = document.getElementById("location-button");
  // Get the <span> element that closes the modal
  const span = document.getElementById("location-modal-close");

  // Open the modal at the beginning
  showModal();

  // When the user clicks the button, open the modal 
  btn.onclick = function() {
    showModal();
  }

  // When the user clicks on <span> (x), close the modal
  span.onclick = function() {
    hideModal();
  }

  // When the user clicks anywhere outside of the modal, close it
  window.onclick = function(event) {
    if (event.target == modal) {
      hideModal();
    }
  }

  function showModal() {
    modal.style.display = "block";
  }
  function hideModal() {
    modal.style.display = "none";
  }
}


function initGeolocation() {
  const myMap = document.getElementById("location-map");
  const statusDiv = document.getElementById("location-status");

  // Try HTML5 geolocation.
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        const pos = {
          lat: position.coords.latitude,
          lon: position.coords.longitude
        };
        setSessionGeolocation(pos.lat,pos.lon);
        // show geolocation on map
        myMap.src = MAPS_EMBED_API_URL+"&q=+"+pos.lat+"+,+"+pos.lon+"+";
        myMap.style.display = "block";
        // no status message
        statusDiv.innerHTML = "";
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

function initLocationSearch() {
  const myMap = document.getElementById("location-map");
  const statusDiv = document.getElementById("location-status");
  const input = document.getElementById("location-input");
  
  // limit to Canada & US
  const options = {
    componentRestrictions: { country: ["ca","us"] }
  };
  const autocomplete = new google.maps.places.Autocomplete(input, options);
  google.maps.event.addListener(autocomplete, 'place_changed', function () {
    let place = autocomplete.getPlace();
    setSessionGeolocation(place.geometry.location.lat(),place.geometry.location.lng());
    // show geolocation on map
    let placeAddress = place.formatted_address.replace(/ /g, "%20");
    console.log(place.name);
    myMap.src = MAPS_EMBED_API_URL+"&q="+placeAddress;
    myMap.style.display = "block";
    // no status message
    statusDiv.innerHTML = "";
  });
}


function automatic_sample_slideshow() {
  var slide_index_val = 0;
  var all_example_slides = document.getElementsByClassName("exampleInputSlide");

  for (var iterator = 0; iterator < all_example_slides.length; iterator++) {
    all_example_slides[iterator].style.display = "none";  
  }
  slide_index_val++;
  if (slide_index_val > all_example_slides.length) {
    slide_index_val = 1;
  } 

  all_example_slides[slide_index_val-1].style.display = "block";  
  setTimeout(automatic_sample_slideshow, 4000);
}