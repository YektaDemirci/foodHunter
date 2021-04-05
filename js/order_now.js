function place_order(query){
    query = query.replace(/\s+/g, '+');
    const settings = {
	"async": true,
	"crossDomain": true,
	"url": "https://google-search3.p.rapidapi.com/api/v1/crawl/q=" + query+"+skipthedishes",
	"method": "GET",
	"headers": {
		"x-rapidapi-key": "85aacae061msh922097c3dec337ep1dcfd2jsn640aefd48d9f",
		"x-rapidapi-host": "google-search3.p.rapidapi.com"
	}
};
console.log(settings);
$.ajax(settings).done(function (response) {
	console.log(response);
	var link = response["results"][0]["link"];
    console.log(link);
    var redirectWindow = window.open(link, '_blank');
    redirectWindow.location;
});

}

function order_now(value){

    /**
        CITATION (IEEE FORMATTED)
        w3schools, Modal Example. N/A: w3schools, N/A. [webpage].
        Link: https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_modal

    **/

    var modal = document.getElementById("order_modal");
    modal.style.display = "block";

    // selections
    var selectionBox = document.getElementById("final-selections");
    var selectionsFinal = "";

    // selection-div-class
    var selectionList = document.getElementsByClassName("selection-div-class");

    console.log(selectionList);

    /**
        CITATION (IEEE FORMATTED)
        C. C. Salvado and P. Mortensen, Loop through an array in JavaScript. N/A: stakoverflow, 2010. [webpage].
        Link: https://stackoverflow.com/questions/3010840/loop-through-an-array-in-javascript

    **/

    for (var i = 0; i < selectionList.length; i++) {
        console.log(selectionList[i].innerText);
        selectionsFinal += "<p>" + selectionList[i].innerText + "</p>";
    }

    selectionBox.innerHTML = selectionsFinal;

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // citation:
    // https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_modal
    console.log("HERE ORDER YES");

    console.log(value);
    var value_split = value.split("??");
    q = value_split[1] + " " + value_split[2];
    place_order(q);


//    var modal = document.getElementById("order_modal");
//    modal.style.display = "block";
//
//    // selections
//    var selectionBox = document.getElementById("final-selections");
//    var selectionsFinal = "";
//
//    // selection-div-class
//    var selectionList = document.getElementsByClassName("selection-div-class");
//
//    console.log(selectionList);
//
//    // citation - https://stackoverflow.com/questions/3010840/loop-through-an-array-in-javascript
//    for (var i = 0; i < selectionList.length; i++) {
//        console.log(selectionList[i].innerText);
//        selectionsFinal += "<p>" + selectionList[i].innerText + "</p>";
//    }
//
//    selectionBox.innerHTML = selectionsFinal;
//
//    // Get the <span> element that closes the modal
//    var span = document.getElementsByClassName("close")[0];
//
//    // When the user clicks on <span> (x), close the modal
//    span.onclick = function() {
//    modal.style.display = "none";
//    }
//
//    // When the user clicks anywhere outside of the modal, close it
//    window.onclick = function(event) {
//        if (event.target == modal) {
//            modal.style.display = "none";
//        }
//    }


}

function callbackFunc(response) {
    // do something with the response
    console.log(response);
}