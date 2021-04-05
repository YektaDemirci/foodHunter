function order_now(value){

    // citation:
    // https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_modal

    var modal = document.getElementById("order_modal");
    modal.style.display = "block";

    // selections
    var selectionBox = document.getElementById("final-selections");
    var selectionsFinal = "";

    // selection-div-class
    var selectionList = document.getElementsByClassName("selection-div-class");

    console.log(selectionList);

    // citation - https://stackoverflow.com/questions/3010840/loop-through-an-array-in-javascript
    for (var i = 0; i < selectionList.length; i++) {
        console.log(selectionList[i].innerText);
        selectionsFinal += "<p>" + selectionList[i].innerText + "</p>";
    }

    selectionBox.innerHTML = selectionsFinal;

    // Get the <span> element that closes the modal
    var span = document.getElementById("order-modal-close");

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }


}