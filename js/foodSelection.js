function food_selection(value) {

    value = value.replace("[single-quote]", "'");
    var value_split = value.split("??");
    var selection_str = "<div class=\"selection-div-class\">" + value_split[0] + " from " + value_split[1] + " located at " + value_split[2] + "</div>";
    var selections = document.getElementById('selections').innerHTML;

    if(!selections.includes(selection_str)){
        selections += selection_str;
        document.getElementById('selections').innerHTML = selections;
    }
}

function clear_selections(value){
    document.getElementById('selections').innerHTML = "";
}