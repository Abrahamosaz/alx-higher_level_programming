$(function () {
  const URL = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.get(URL, function (data, textStatus) {
    if (textStatus === 'succces') {
      $('div#character').text(data.name);
    }
  });
});
