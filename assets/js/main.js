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
    document.body.classList.toggle("dark");
  }
}

if (localStorage && localStorage.getItem("theme") === "dark") {
  setTheme();
}

function openMenu() {
  document.getElementById("navbar").classList.toggle("show");
}
