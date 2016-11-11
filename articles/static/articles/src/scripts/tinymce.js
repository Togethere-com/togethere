var $ = require('jquery'),
    $e = $('.tinymce'),
    tinymceConf = {
  theme: "modern",
  toolbar: "undo redo | bold italic | bullist numlist | blockquote | removeformat",
  menubar: false,
  statusbar: false,
  schema: "html5",
  max_height: 500,
  max_width: 500,
  min_height: 100,
  min_width: 400,
  content_css: '/static/articles/build/css/tinymce.css',
};
//if #id_text doesn't exist, no worries
document.getElementById('id_text').removeAttribute("required");
// .tinymce element is not present on all pages so check for it
if ($e.length != 0) {
  tinymce.remove();
}
tinymce.init(tinymceConf);
