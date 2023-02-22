$(function () {
  const URL = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.get(URL, function (data, textStatus) {
    if (textStatus === 'sucess') {
      $('div#hello').text(data.hello);
    }
  });
});
