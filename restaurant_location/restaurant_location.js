var dict = null;
var total_rest = 0;
var processed = 0;
var failed = 0;

function init() {
    dict  = {};
    var total = 0;
    var progress = 0;
    //data_food_sample.json
    $.getJSON("../data_food_sample.json", function(data) {
        total = data.length;
        total_rest = 0;
        processed = 0;
        failed = 0;
        document.getElementById("num_total").innerHTML = total;
        document.getElementById("num_progress").innerHTML = progress;
        document.getElementById("num_rest").innerHTML = total_rest;
        document.getElementById("num_processed").innerHTML = processed;
        document.getElementById("num_failed").innerHTML = failed;
        document.getElementById("status").innerHTML = "Loading...";
        var i;
        for (i = 0; i < data.length; i++) {
            progress++;
            showProgress();
            let key = data[i].address;
            if(!(key in dict)){
                total_rest++;
                dict[key] = null;
            }
        }
        document.getElementById("num_progress").innerHTML = progress;
        document.getElementById("num_rest").innerHTML = total_rest;
        i = 0;
        for(var key in dict){
            i++;
            if(i % 10 == 0){
                wait(1900);
            }
            wait(100);
            getGeolocation(key);
        }
    });

    function showProgress(){
        console.log(progress);
        let percentage3 = parseInt(progress/total*1000);
        if(percentage3 % 10 == 0) {
            document.getElementById("num_progress").innerHTML = progress;
        }
    }
}

function wait(ms) {
    var start = Date.now(),
        now = start;
    while (now - start < ms) {
      now = Date.now();
    }
}

// Geocode API: convert address to geolocation (lat&lng)
function getGeolocation(address) {
    let geocode_json_url = GEOCODE_API_URL
        +"&address="+address.replace(/ /g, "+");
    $.getJSON(geocode_json_url, function(response) {
        processed++;
        showProcessed();
        if (response.status !== "OK") {
            failed++;
            document.getElementById("num_failed").innerHTML = failed;
            console.log(failed, address, "Error-geocode: " + response.status);
        } else {
            // get restaurant geolocation (lat&lng)
            dict[address] = response.results[0].geometry.location;
        }
        if(processed == total_rest){
            saveData();
            console.log('Completed');
        }
    });

    function showProcessed(){
        console.log(processed,address);
        let percentage3 = parseInt(processed/total_rest*1000);
        if(percentage3 % 10 == 0) {
            document.getElementById("num_processed").innerHTML = processed;
        }
    }
}

/*
 * https://stackoverflow.com/questions/2897619/using-html5-javascript-to-generate-and-save-a-file
 */
function saveData() {
    document.getElementById("status").innerHTML = "Completed";
    var dictstring = JSON.stringify(dict);

    document.getElementById("link-div").style.display = "block";

    var link = document.getElementById('link');
    link.setAttribute('href', 
        'data:text/plain;charset=utf-8,' + encodeURIComponent(dictstring));
}