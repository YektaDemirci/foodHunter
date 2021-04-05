function food_selection(value) {

    console.log("Getting count");
    var count = document.querySelectorAll('#selections .selection-div-class').length;
    console.log(count);
    value = value.replace("[single-quote]", "'");
    var value_split = value.split("??");
    var selection_str = "<div class=\"selection-div-class\" id=\"number-"+count+"\">" + value_split[0] + " from " + value_split[1] + " located at " + value_split[2] + "<br>";
    value = value.replace("'", "");
    selection_str += "<button class=\"submitLeftNext btn btn-light\" type=\"submit\" onclick=\"order_now('" + value + "')\">Place Order <i class=\"fas fa-shopping-cart\"></i></button>";
    selection_str += "<button class=\"submitLeftNext btn btn-light\" id=\"clear-button\" type=\"submit\" onclick=\"clear_selection('number-" + count + "')\">Clear selection <i class=\"fas fa-trash\"></i></button>";
    selection_str += "</div>";
    console.log(selection_str);
    var selections = document.getElementById('selections').innerHTML;
    var check_if_selected = selections.includes(value_split[0]) && selections.includes(value_split[1]) && selections.includes(value_split[2]);

    if(!check_if_selected){
        selections += selection_str;
        document.getElementById('selections').innerHTML = selections;
    }
}

function clear_selection(id){
    document.getElementById(id).outerHTML = "";
}
function clear_selections(value){
    document.getElementById('selections').innerHTML = "";
}