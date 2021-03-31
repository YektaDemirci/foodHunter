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
    var vanishedText = document.getElementsByClassName("vanished-text");
    var arrows = document.getElementsByClassName('arrow');
    for (var i=0; i<vanishedText.length;i++) { vanishedText[i].style.display="block";}
    for (var i=0; i<arrows.length;i++) { arrows[i].style.display="inline-block";}
  }

  function pulseArrow(pulse){
    if (pulse==true){
      document.getElementById("step2-right-arrow-button").style.animation = "pulse 3s infinite";
      document.getElementById("step2-right-arrow-button").style.animationDelay = '5s';
    }
    else {
      document.getElementById("step2-right-arrow-button").style.animation = "None";
    }
  }

  function showStep3Options(){
    document.getElementById("clear").style.display="inline-block";
    document.getElementById("review").style.display="inline-block";
  }

// If you click to submit on the welcoming page, it moves to suggestions page
document.querySelector(".submitLeftNext").addEventListener("click", function() {
  updateFooter("step2");
  removeGifs(); 
  showStep3Options();
  pulseArrow(true);
});
// If you click to back on the suggestion page, it goes back to welcoming page
document.querySelector(".submitMidBack").addEventListener("click", function() {
  updateFooter("step1");
  pulseArrow(false); 
});
// // If you click to next on the suggestion page, it moves to ordering page
document.querySelector(".submitMidNext").addEventListener("click", function() {
  updateFooter("step3"); 
  pulseArrow(false);
});
// // If you click to back on the ordering page, it moves to suggestion page
document.querySelector(".submitRightBack").addEventListener("click", function() {
  updateFooter("step2"); 
  pulseArrow(false);
});
