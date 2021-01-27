function food_search() {

    let input = document.getElementById('search-bar-id').value
    document.getElementById('results').innerHTML  = "loading"; 

    let result_list_str = "";

    input = input.toLowerCase();

    $.getJSON("data_food_sample.json", function(jsonFood) {

        if (!input) {
            result_list_str = "you forgot to type something into the search bar!";
        }
        
        else {

            for (i = 0; i < jsonFood.length; i++) {
            
                var ingredient_list = jsonFood[i].ingredients.split(",");

                if(ingredient_list.indexOf(input) >= 0){
                    result_list_str = result_list_str + jsonFood[i].product + " at " + jsonFood[i].restaurant + "<br>";
                }
            }
        }

        if(result_list_str.length == 0){
            result_list_str = "we could not find anything, sorry.";
        }

        document.getElementById('results').innerHTML  = result_list_str;

    });

    


}