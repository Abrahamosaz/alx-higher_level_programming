const $url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$(function () {
  $.ajax($url, {
    method: 'GET',
    dataType: 'json',
    success: function (data, status, jqxhr) {
      $('div#character').text(data.name);
    }
  });
});
