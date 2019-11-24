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

This file is based on code from the writeFreely project. You can find the
source code at <https://github.com/writeas/writefreely>
*/
var $composer = document.getElementById('composer');
var $wordcount = document.getElementById('word-count');
var typingTimer;
var typingInterval = 200;
function updateWordCount() {
  var words = 0;
  var content = $composer.value.trim();
  if (content != '') {
    words = content.replace(/\s+/gi, ' ').split(' ').length;
  }
  $wordcount.textContent = words + " word" + (words != 1 ? "s" : "");
}
function loadContents() {
	var content = localStorage.getItem('content');
	if (content != null) {
		$composer.value = content;
	}
}
var updateContents = function() {
  localStorage.setItem('content', $composer.value);
  updateWordCount();
}
var resetTimer = function() {
  clearTimeout(typingTimer);
  typingTimer = setTimeout(updateContents, typingInterval);
}
function downloadData(filename, text) {
  var text = localStorage.getItem('content');
  if (text != null && text != '') {
    var tmpElement = document.createElement('a');
    tmpElement.setAttribute('href', 'data:text/markdown;charset=utf-8,' + encodeURIComponent(text));
    tmpElement.setAttribute('download', 'contents.md');
    tmpElement.style.display = 'none';

    document.body.appendChild(tmpElement);
    tmpElement.click();
    document.body.removeChild(tmpElement);
  }
}
var saveOrResetTimer = function(event) {
  if (event.keyCode == 83 && (event.metaKey || event.ctrlKey)) {
    event.preventDefault();
    updateContents();
    downloadData();
  }
  clearTimeout(typingTimer);
  typingTimer = setTimeout(updateContents, typingInterval);
}

$composer.addEventListener('keyup input', resetTimer);
$composer.addEventListener('keydown', saveOrResetTimer);
$composer.addEventListener('input', resetTimer);
window.addEventListener('beforeunload', updateContents);
loadContents();
updateWordCount();
