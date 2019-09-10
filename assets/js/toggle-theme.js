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
      if (!e[i].classList.contains("is-size-6")) {
        e[i].classList.add((light ? "has-text-dark" : "has-text-grey"));
        e[i].classList.remove((light ? "has-text-grey" : "has-text-dark"));
      }
    }
  }
}

if (localStorage && localStorage.getItem("theme") === "dark") {
  setTheme();
}
