const $url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$(function () {
  $.get($url, function (data) {
    for (item of data.results) {
      $('ul#list_movies').append('<li>' + item.title + '</li>');
    }
  });
});
