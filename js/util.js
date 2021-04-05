const API_KEY = "AIzaSyCh_nAkklDfea8cKEhEmplXqXz7yxl2yGA";
const CUSTOM_SEARCH_API_KEY = "AIzaSyCirdwEElfje7ztIAtG0WWG6UMv1mOGfXU";
const MAPS_EMBED_API_URL = "https://www.google.com/maps/embed/v1/place?key="+API_KEY;
const MAPS_JS_API_URL = "https://maps.googleapis.com/maps/api/js?key="+API_KEY;
const GEOCODE_API_URL = "https://maps.googleapis.com/maps/api/geocode/json?key="+API_KEY;


function setSessionGeolocation(lat, lng) {
    sessionStorage.setItem("geo_lat", lat);
    sessionStorage.setItem("geo_lng", lng);
}

function getSessionGeolocation() {
    return {
        lat: sessionStorage.getItem("geo_lat"),
        lng: sessionStorage.getItem("geo_lng")
    };
}

