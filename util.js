const API_KEY = "AIzaSyCh_nAkklDfea8cKEhEmplXqXz7yxl2yGA";
const MAPS_EMBED_API_URL = "https://www.google.com/maps/embed/v1/place?key="+API_KEY;
const MAPS_JS_API_URL = "https://maps.googleapis.com/maps/api/js?key="+API_KEY;


function setSessionGeolocation(lat, lon) {
    sessionStorage.setItem("geo_lat", lat);
    sessionStorage.setItem("geo_lon", lon);
}

function getSessionGeolocation() {
    return {
        lat: sessionStorage.getItem("geo_lat"),
        lon: sessionStorage.getItem("geo_lon")
    };
}