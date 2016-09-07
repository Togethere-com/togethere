document.addEventListener("DOMContentLoaded", DOMContentLoaded);

function DOMContentLoaded() {

    var $ = jQuery;
    var $e = $('.tinymce');
    // .tinymce element is not present on all pages so check for it
    if ($e.length != 0) {
      var tinymceConf = $e.data('mce-conf');
      tinymce.remove();
      tinymce.init(tinymceConf);
    }

}

new Pjax({
  elements: "a",
  selectors: ["title", ".site-header", ".content"]
})

document.addEventListener("pjax:success", DOMContentLoaded);
