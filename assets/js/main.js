/*
Copyright (C) 2019 Oscar Benedito

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
*/
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
