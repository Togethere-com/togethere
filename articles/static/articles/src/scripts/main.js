document.addEventListener("DOMContentLoaded", DOMContentLoaded);

function DOMContentLoaded() {

    var $ = jQuery;
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

new Pjax({
    elements: "a",
    selectors: ["title", ".site-header", ".content"],
    switches: {
      "title": Pjax.switches.sideBySide,
      ".site-header": Pjax.switches.sideBySide,
      ".content": Pjax.switches.sideBySide
    },
    switchesOptions: {
      classNames: {
        // class added on the element that will be removed
        remove: "pjax, pjax--remove",
        // class added on the element that will be added
        add: "pjax, pjax-add",
        // class added on the element when it go backward
        backward: "pjax--backward",
        // class added on the element when it go forward (used for new page too)
        forward: "pjax--forward"
      }
    }
})

document.addEventListener("pjax:success", DOMContentLoaded)
