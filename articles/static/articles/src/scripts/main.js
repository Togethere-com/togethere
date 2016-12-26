var Headroom = require('headroom.js');

function DOMContentLoaded() {
  var tinymceTextarea = document.querySelector('.tinymce'),
      id_text = document.getElementById('id_text'),
      filterFormResetButton = document.getElementById('filter-form-reset-button'),
      siteHeader = document.querySelector('.site-header'),
      articleForm = document.querySelector('.article-form');

  var siteHeaderHeadroom  = new Headroom(siteHeader, {
    'offset': 80,
    'tolerance': 8,
    classes : {
      // when element is initialized
      initial : 'site-header',
      // when scrolling up
      pinned : 'site-header--pinned',
      // when scrolling down
      unpinned : 'site-header--unpinned',
      // when above offset
      top : 'site-header--top',
      // when below offset
      notTop : 'site-header--not-top',
      // when at bottom of scroll area
      bottom : 'site-header--bottom',
      // when not at bottom of scroll area
      notBottom : 'site-header--not-bottom'
    }
  });
  siteHeaderHeadroom.init();

  if (id_text) {
    id_text.removeAttribute('required');
  }
  // .tinymce element is not present on all pages so check for it
  if (tinymceTextarea) {
    var tinymceConf = {
      selector: '.tinymce',
      inline: true,
      theme: 'inlite',
      selection_toolbar: 'undo redo | h2 h3 | bold italic | bullist numlist | blockquote | removeformat',
      insert_toolbar: false,
      menubar: false,
      statusbar: false,
      schema: 'html5',
      max_height: 500,
      max_width: 500,
      min_height: 100,
      min_width: 400,
      content_css: '/static/articles/build/css/tinymce.css',
    }
    tinymce.remove();
    tinymce.init(tinymceConf);
  }

  if (articleForm) {
    articleForm.onsubmit = function() {
      var textarea = document.getElementById('id_text'),
          div = document.getElementById('article-text-input');
      textarea.value = div.innerHTML;
      return true;
    }
  }

  if (filterFormResetButton) {
    filterFormResetButton.addEventListener('click', function (event) {
      event.preventDefault();
      var filterForm = document.getElementById('filter-form'),
        inputs = filterForm.getElementsByTagName('input');
      Array.prototype.forEach.call(inputs, function(input) {
        if (input.type==='checkbox') {
          input.checked = false;
        }
      });
      // TODO maybe not submit yet?
      filterForm.submit();
    });
  }
}

document.addEventListener('DOMContentLoaded', DOMContentLoaded);
