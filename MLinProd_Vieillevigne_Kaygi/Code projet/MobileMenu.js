function myFunction() {
  var x = document.getElementById("myBarMenu");
  if (x.className === "BarMenu") {
    x.className += " responsive";
  } else {
    x.className = "BarMenu";
  }
}