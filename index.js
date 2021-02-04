//There is a bit repition here, needs an update

// If you click to submit on the welcoming page, it moves to suggestions page
document.querySelector(".submitLeftNext").addEventListener("click" , function(){
  var left = document.querySelector(".left");
  left.style.width = "10%";
  left.style.backgroundColor = "#335d2d";
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
  left.style.backgroundColor = "#335d2d";
  var mid = document.querySelector(".mid");
  mid.style.width = "10%";
  mid.style.backgroundColor = "#335d2d";
  var right = document.querySelector(".right")
  right.style.width = "80%";
  right.style.backgroundColor = "#f4f5db";
});

// If you click to back on the ordering page, it moves to suggestion page
document.querySelector(".submitLeftBack").addEventListener("click" , function(){
  var left = document.querySelector(".left");
  left.style.width = "10%";
  left.style.backgroundColor = "#335d2d";
  var mid = document.querySelector(".mid");
  mid.style.width = "80%";
  mid.style.backgroundColor = "#f4f5db";
  var right = document.querySelector(".right")
  right.style.width = "10%";
  right.style.backgroundColor = "#f8dc81";
});

///////////////////////////////////////////////////////////////////////////

// Responsive Navbar (Copied from above)
const footerIDSteps = ['step1', 'step2', 'step3'];
function updateFooter(activeStepID) {
    footerIDSteps.forEach(step => {
      if(step == activeStepID){
        let stepNode = document.getElementById(step);
        stepNode.className = "col-md current-step";
      } 
      else {
        let stepNode = document.getElementById(step);
        stepNode.className = "col-md bg-step";
      }
    })
  }

// If you click to submit on the welcoming page, it moves to suggestions page
document.querySelector(".submitLeftNext").addEventListener("click", function() {
  updateFooter("step2"); });
// If you click to back on the suggestion page, it goes back to welcoming page
document.querySelector(".submitMidBack").addEventListener("click", function() {
  updateFooter("step1"); });
// // If you click to next on the suggestion page, it moves to ordering page
document.querySelector(".submitMidNext").addEventListener("click", function() {
  updateFooter("step3"); });
// // If you click to back on the ordering page, it moves to suggestion page
document.querySelector(".submitLeftBack").addEventListener("click", function() {
  updateFooter("step2"); });