const $url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$(function () {
  $.get($url, function (data) {
    $('div#hello').text(data.hello);
  });
});
