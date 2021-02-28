// Repetition is fixed.
const footerIDSteps = ["step1", "step2", "step3"];

function updateFooter(activeStepID, activeBox) {
    footerIDSteps.forEach(step => {
      if(step < activeStepID){
        let stepNode = document.querySelectorAll("."+step);
        stepNode[0].className = "box doneBox "+step;
        stepNode[1].className = "done-step "+step;
      }
      else if (step == activeStepID){
        let stepNode = document.querySelectorAll("."+step);
        stepNode[0].className = "box activeBox "+step;
        stepNode[1].className = "current-step "+step;
      }
      else {
          let stepNode = document.querySelectorAll("."+step);
          stepNode[0].className = "box undoneBox "+step;
          stepNode[1].className = "undone-step "+step;
      }
    })
  }

  function removeGifs(){
    document.getElementById("box-step2").style.backgroundImage = "none"; 
    document.getElementById("box-step3").style.backgroundImage = "none";
  }

// If you click to submit on the welcoming page, it moves to suggestions page
document.querySelector(".submitLeftNext").addEventListener("click", function() {
  updateFooter("step2");
  removeGifs(); });
// If you click to back on the suggestion page, it goes back to welcoming page
document.querySelector(".submitMidBack").addEventListener("click", function() {
  updateFooter("step1"); });
// // If you click to next on the suggestion page, it moves to ordering page
document.querySelector(".submitMidNext").addEventListener("click", function() {
  updateFooter("step3"); });
// // If you click to back on the ordering page, it moves to suggestion page
document.querySelector(".submitRightBack").addEventListener("click", function() {
  updateFooter("step2"); });
