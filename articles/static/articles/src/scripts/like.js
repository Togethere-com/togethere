var koekjes = require('js-cookie');

function DOMContentLoaded() {
  var heartButton = document.getElementById('heart-button'),
  articleId = heartButton.dataset.articleId,
  url = 'article-like/' + articleId + '/',
  csrftoken = koekjes.get('csrftoken');

  heartButton.addEventListener('click', function() {
    httpGetAsync(url, function(data) {
      document.getElementById('likes__count').textContent = data;
      // switch the liked data attribute
      if (heartButton.dataset.liked == 'true') {
        heartButton.dataset.liked = 'false';
      } else {
        heartButton.dataset.liked = 'true';
      }
    });
  });

  function httpGetAsync(theUrl, callback) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() {
      if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
      callback(xmlHttp.responseText);
    }
    xmlHttp.open("POST", theUrl, true); // true for asynchronous
    xmlHttp.setRequestHeader("X-CSRFToken", csrftoken);
    xmlHttp.send();
  }
}

document.addEventListener('DOMContentLoaded', DOMContentLoaded);
