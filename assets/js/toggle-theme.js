'use strict';
function toggleTheme() {
  if (localStorage && localStorage.getItem("theme") === "dark") {
    localStorage.setItem("theme", "default");
  } else if (localStorage) {
    localStorage.setItem("theme", "dark");
  }
  setTheme();
}

function setTheme() {
  if (localStorage) {
    var light = localStorage.getItem("theme") === "default";

    document.getElementById("theme").setAttribute("href", "/css/" + (light ? "light" : "dark") + ".css");
    document.getElementById("nav-logo").setAttribute("src", "/img/logo-" + (light ? "white" : "grey") + ".min.svg");

    var e = document.getElementsByClassName((light ? "has-text-grey" : "has-text-dark"));
    for (var i = 0; i < e.length; i++) {
      e[i].className = (light ? "has-text-dark" : "has-text-grey");
    }
  }
}

if (localStorage && localStorage.getItem("theme") === "dark") {
  setTheme();
}
