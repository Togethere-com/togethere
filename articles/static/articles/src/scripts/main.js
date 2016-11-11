var Pjax = require('pjax');

function DOMContentLoaded() {

  new Pjax({
    elements: "a",
    selectors: [".content"],
    switches: {
      ".content": customSwitch
    }
  })
}

function customSwitch(oldEl, newEl, pjaxRequestOptions, switchesClasses) {
  oldEl.classList.add('pjax','pjax--forward');
  newEl.classList.add('pjax','pjax--backward');
  setTimeout(function () {
    oldEl.outerHTML = newEl.outerHTML
  }, 300);
  this.onSwitch( console.log("onswitch") );
}

document.addEventListener("DOMContentLoaded", DOMContentLoaded)

var pfx = ["webkit", "moz", "MS", "o", ""];
function PrefixedEvent(element, type, callback) {
  for (var p = 0; p < pfx.length; p++) {
	if (!pfx[p]) type = type.toLowerCase();
	element.addEventListener(pfx[p]+type, callback, false);
  }
}
PrefixedEvent(document, "AnimationStart", AnimationListener);
function AnimationListener() {
  console.log("animation start event fired");
}
