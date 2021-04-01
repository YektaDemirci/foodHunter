function food_selection(value) {

    value = value.replace("[single-quote]", "'");
    var value_split = value.split("??");
    var selection_str = "<div class=\"selection-div-class\">" + value_split[0] + " from " + value_split[1] + " located at " + value_split[2] + "<br>";
    value = value.replace("'", "");
    selection_str += "<button class=\"submitLeftNext btn btn-light\" type=\"submit\" onclick=\"order_now('" + value + "')\">Place Order <i class=\"fas fa-shopping-cart\"></i></button>";
    selection_str += "</div>";
    console.log(selection_str);
    var selections = document.getElementById('selections').innerHTML;
    var check_if_selected = selections.includes(value_split[0]) && selections.includes(value_split[1]) && selections.includes(value_split[2]);

    if(!check_if_selected){
        selections += selection_str;
        document.getElementById('selections').innerHTML = selections;
    }
}

function clear_selections(value){
    document.getElementById('selections').innerHTML = "";
}