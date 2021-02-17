function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}



function myFunction1(x) {
  if (x.matches) { // If media query matches
    
  document.getElementById("col-8").classList.remove("col-8")
  document.getElementById("col-4").classList.remove("col-4") 
  } else {

  document.getElementById("col-8").classList.add("col-8")
  document.getElementById("col-4").classList.add("col-4") 
  
  }
}

var x = window.matchMedia("(max-width: 700px)")
myFunction1(x) // Call listener function at run time
x.addListener(myFunction1) // Attach listener function on state changes