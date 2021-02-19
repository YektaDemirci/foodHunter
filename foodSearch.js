function food_search() {

    let input = document.getElementById('search-bar-id').value
    document.getElementById('results').innerHTML  = "loading"; 

    let result_list_str = "";

    input = input.toLowerCase();
    input = input.replaceAll(" ", "")

    let input_split = input.split(",");
    let input_split_len = input_split.length;

    $.getJSON("data_food_sample.json", function(jsonFood) {

        if (!input || input == null) {
            result_list_str = "you forgot to type something into the search bar!";
        }

        else {

            for (i = 0; i < jsonFood.length; i++) {
            
                var ingredient_list_despaced = jsonFood[i].ingredients.replaceAll(" ", "");
                var ingredient_list = ingredient_list_despaced.split(",");

                var foodTag_list_despaced = jsonFood[i].tags.replaceAll(" ", "");
                var foodTag_list = foodTag_list_despaced.split(",");

                var ingredient_count = 0;
                
                input_split.forEach(function (ingredientVal) {

                    if(ingredient_list.indexOf(ingredientVal) >= 0 || foodTag_list.indexOf(ingredientVal) >= 0){
                        ingredient_count++;
                    }

                });

                if(ingredient_count == input_split_len){
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