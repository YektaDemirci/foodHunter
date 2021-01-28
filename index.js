//There is a bit repition here, needs an update

// If you click to submit on the welcoming page, it moves to suggestions page
document.querySelector(".submitLeftNext").addEventListener("click" , function(){
  var left = document.querySelector(".left");
  left.style.width = "10%";
  left.style.backgroundColor = "#96bb7c";
  var mid = document.querySelector(".mid")
  mid.style.width = "80%";
  mid.style.backgroundColor = "#f4f5db";
  var right = document.querySelector(".right")
  right.style.width = "10%";
  right.style.backgroundColor = "#f8dc81";

});

// If you click to back on the suggestion page, it goes back to welcoming page
document.querySelector(".submitMidBack").addEventListener("click" , function(){
  var left = document.querySelector(".left");
  left.style.width = "80%";
  left.style.backgroundColor = "#f4f5db";
  var mid = document.querySelector(".mid")
  mid.style.width = "10%";
  mid.style.backgroundColor = "#f8dc81";
  var right = document.querySelector(".right")
  right.style.width = "10%";
  right.style.backgroundColor = "#f8dc81";

});

// If you click to next on the suggestion page, it moves to ordering page
document.querySelector(".submitMidNext").addEventListener("click" , function(){
  var left = document.querySelector(".left");
  left.style.width = "10%";
  left.style.backgroundColor = "#96bb7c";
  var mid = document.querySelector(".mid");
  mid.style.width = "10%";
  mid.style.backgroundColor = "#96bb7c";
  var right = document.querySelector(".right")
  right.style.width = "80%";
  right.style.backgroundColor = "#f4f5db";
});

// If you click to back on the ordering page, it moves to suggestion page
document.querySelector(".submitLeftBack").addEventListener("click" , function(){
  var left = document.querySelector(".left");
  left.style.width = "10%";
  left.style.backgroundColor = "#96bb7c";
  var mid = document.querySelector(".mid");
  mid.style.width = "80%";
  mid.style.backgroundColor = "#f4f5db";
  var right = document.querySelector(".right")
  right.style.width = "10%";
  right.style.backgroundColor = "#f8dc81";
});
