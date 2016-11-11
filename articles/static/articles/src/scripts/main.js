var Pjax = require('pjax'),
    switches = require('pjax/lib/switches');

document.addEventListener("DOMContentLoaded", DOMContentLoaded);

function DOMContentLoaded() {

    var $ = require('jquery');
    var $e = $('.tinymce');
    // .tinymce element is not present on all pages so check for it
    if ($e.length != 0) {
      if ($e.data('mce-conf').length != 0) {
        var tinymceConf = $e.data('mce-conf');
      } else {
        var tinymceConf = {
          theme: "modern",
          toolbar: "undo redo | bold italic | bullist numlist | blockquote | removeformat",
          menubar: False,
          statusbar: False,
          schema: "html5",
          max_height: 500,
          max_width: 500,
          min_height: 100,
          min_width: 400,
          content_css: '/static/articles/build/css/tinymce.css',
        }
      }
      document.getElementById('id_text').removeAttribute("required");
      tinymce.remove();
      tinymce.init(tinymceConf);
    }

}

function customSwitch(oldEl, newEl, pjaxRequestOptions, switchesClasses) {
  oldEl.classList.add('pjax','pjax--forward');
  newEl.classList.add('pjax','pjax--backward');
  setTimeout(function () {
    oldEl.outerHTML = newEl.outerHTML
  }, 300);
  this.onSwitch( console.log("onswitch") );
}

new Pjax({
    elements: "a",
    selectors: ["title", ".site-header", ".content"],
    switches: {
      "title": customSwitch,
      ".site-header": customSwitch,
      ".content": customSwitch
    }
})

document.addEventListener("pjax:success", DOMContentLoaded)

var pfx = ["webkit", "moz", "MS", "o", ""];
function PrefixedEvent(element, type, callback) {
	for (var p = 0; p < pfx.length; p++) {
		if (!pfx[p]) type = type.toLowerCase();
		element.addEventListener(pfx[p]+type, callback, false);
	}
}
PrefixedEvent(document, "AnimationEnd", AnimationListener);
function AnimationListener() {
  console.log("animation end event fired");
}
